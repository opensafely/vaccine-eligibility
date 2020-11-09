from cohortextractor import codelist_from_csv

chronic_kidney_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-kidney-disease.csv", system="ctv3", column="CTV3ID"
)
chronic_liver_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-liver-disease.csv", system="ctv3", column="CTV3ID"
)
current_copd_codes = codelist_from_csv(
    "codelists/opensafely-current-copd.csv", system="ctv3", column="CTV3ID"
)
dementia_codes = codelist_from_csv(
    "codelists/opensafely-dementia.csv", system="ctv3", column="CTV3ID"
)
diabetes_codes = codelist_from_csv(
    "codelists/opensafely-diabetes.csv", system="ctv3", column="CTV3ID"
)
haematological_cancer_codes = codelist_from_csv(
    "codelists/opensafely-haematological-cancer.csv", system="ctv3", column="CTV3ID"
)
permanent_immunosuppression_codes = codelist_from_csv(
    "codelists/opensafely-permanent-immunosuppression.csv", system="ctv3", column="CTV3ID"
)
temporary_immunosuppression_codes = codelist_from_csv(
    "codelists/opensafely-temporary-immunosuppression.csv", system="ctv3", column="CTV3ID"
)
solid_organ_transplantation_codes = codelist_from_csv(
    "codelists/opensafely-solid-organ-transplantation.csv", system="ctv3", column="CTV3ID"
)
stroke_codes = codelist_from_csv(
    "codelists/opensafely-stroke-updated.csv", system="ctv3", column="CTV3ID"
)
