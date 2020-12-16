import base64
import sys
from io import BytesIO
from argparse import ArgumentParser
from matplotlib import pyplot as plt
import numpy as np
import pandas
from pandas.api.types import is_categorical_dtype
from pandas.api.types import is_bool_dtype
from pandas.api.types import is_datetime64_dtype
from pandas.api.types import is_numeric_dtype

import seaborn as sns
import datetime

from cohortextractor.cohortextractor import list_study_definitions
from cohortextractor.cohortextractor import load_study_definition


def make_chart(name, series, dtype):
    FLOOR_DATE = datetime.datetime(1960, 1, 1)
    CEILING_DATE = datetime.datetime.today()
    img = BytesIO()
    # Setting figure sizes in seaborn is a bit weird:
    # https://stackoverflow.com/a/23973562/559140
    if is_categorical_dtype(dtype):
        sns.set_style("ticks")
        sns.catplot(
            x=name, data=series.to_frame(), kind="count", height=3, aspect=3 / 2
        )
        plt.xticks(rotation=45)
    elif is_bool_dtype(dtype):
        sns.set_style("ticks")
        sns.catplot(x=name, data=series.to_frame(), kind="count", height=2, aspect=1)
        plt.xticks(rotation=45)
    elif is_datetime64_dtype(dtype):
        # Early dates are dummy values; I don't know what late dates
        # are but presumably just dud data
        series = series[(series > FLOOR_DATE) & (series <= CEILING_DATE)]
        # Set bin numbers appropriate to the time window
        delta = series.max() - series.min()
        if delta.days <= 31:
            bins = delta.days
        elif delta.days <= 365 * 10:
            bins = delta.days / 31
        else:
            bins = delta.days / 365
        if bins < 1:
            bins = 1
        fig = plt.figure(figsize=(5, 2))
        ax = fig.add_subplot(111)
        series.hist(bins=int(bins), ax=ax)
        plt.xticks(rotation=45, ha="right")
    elif is_numeric_dtype(dtype):
        # Trim percentiles and negatives which are usually bad data
        series = series.fillna(0)
        series = series[
            (series < np.percentile(series, 95))
            & (series > np.percentile(series, 5))
            & (series > 0)
        ]
        fig = plt.figure(figsize=(5, 2))
        ax = fig.add_subplot(111)
        sns.distplot(series, kde=False, ax=ax)
        plt.xticks(rotation=45)
    else:
        raise ValueError()

    plt.savefig(img, transparent=True, bbox_inches="tight")
    img.seek(0)
    plt.close()
    return base64.b64encode(img.read()).decode("UTF-8")



def _make_cohort_report(input_dir, output_dir, study_name, suffix):
    study = load_study_definition(study_name)

    df = study.csv_to_df(f"{input_dir}/input{suffix}.csv")
    descriptives = df.describe(include="all")

    for name, dtype in zip(df.columns, df.dtypes):
        if name == "patient_id":
            continue
        main_chart = '<div><img src="data:image/png;base64,{}"/></div>'.format(
            make_chart(name, df[name], dtype)
        )
        empty_values_chart = ""
        if is_datetime64_dtype(dtype):
            # also do a null / not null plot
            empty_values_chart = (
                '<div><img src="data:image/png;base64,{}"/></div>'.format(
                    make_chart(name, df[name].isnull(), bool)
                )
            )
        elif is_numeric_dtype(dtype):
            # also do a null / not null plot
            empty_values_chart = (
                '<div><img src="data:image/png;base64,{}"/></div>'.format(
                    make_chart(name, df[name] > 0, bool)
                )
            )
        descriptives.loc["values", name] = main_chart
        descriptives.loc["nulls", name] = empty_values_chart

    with open(f"{output_dir}/descriptives{suffix}.html", "w") as f:

        f.write(
            """<html>
<head>
  <style>
    table {
      text-align: left;
      position: relative;
      border-collapse: collapse;
    }
    td, th {
      padding: 8px;
      margin: 2px;
    }
    td {
      border-left: solid 1px black;
    }
    tr:nth-child(even) {background: #EEE}
    tr:nth-child(odd) {background: #FFF}
    tbody th:first-child {
      position: sticky;
      left: 0px;
      background: #fff;
    }
  </style>
</head>
<body>"""
        )

        f.write(descriptives.to_html(escape=False, na_rep="", justify="left", border=0))
        f.write("</body></html>")
    print(f"Created cohort report at {output_dir}/descriptives{suffix}.html")


def make_cohort_report(input_dir, output_dir):
    for study_name, suffix in list_study_definitions():
        _make_cohort_report(input_dir, output_dir, study_name, suffix)
        
if __name__ == "__main__": 
    make_cohort_report(sys.argv[1],sys.argv[2])        