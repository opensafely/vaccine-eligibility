from cohortextractor import codelist_from_csv

solid_organ_transplantation_codes = codelist_from_csv(
    "codelists/opensafely-solid-organ-transplantation.csv", system="ctv3", column="CTV3ID"
)
chemotherapy_or_radiotherapy_codes = codelist_from_csv(
    "codelists/opensafely-chemotherapy-or-radiotherapy-2020-04-15.csv", system="ctv3", column="CTV3ID"
)
cancer_excluding_lung_and_haematological_codes = codelist_from_csv(
    "codelists/opensafely-cancer-excluding-lung-and-haematological-2020-04-15.csv", system="ctv3", column="CTV3ID"
)
lung_cancer_codes = codelist_from_csv(
    "codelists/opensafely-lung-cancer-2020-04-15.csv", system="ctv3", column="CTV3ID"
)
haematological_cancer_codes = codelist_from_csv(
    "codelists/opensafely-haematological-cancer.csv", system="ctv3", column="CTV3ID"
)
bone_marrow_transplant_codes = codelist_from_csv(
    "codelists/opensafely-bone-marrow-transplant-2020-04-15.csv", system="ctv3", column="CTV3ID"
)
cystic_fibrosis_codes = codelist_from_csv(
    "codelists/opensafely-cystic-fibrosis-2020-07-20.csv", system="ctv3", column="CTV3ID"
)
asthma_diagnosis_codes = codelist_from_csv(
    "codelists/opensafely-asthma-diagnosis-2020-04-15.csv", system="ctv3", column="CTV3ID"
)
current_copd_codes = codelist_from_csv(
    "codelists/opensafely-current-copd.csv", system="ctv3", column="CTV3ID"
)
sickle_cell_disease_codes = codelist_from_csv(
    "codelists/opensafely-sickle-cell-disease-2020-04-14.csv", system="ctv3", column="CTV3ID"
)
permanent_immunosuppression_codes = codelist_from_csv(
    "codelists/opensafely-permanent-immunosuppression.csv", system="ctv3", column="CTV3ID"
)
temporary_immunosuppression_codes = codelist_from_csv(
    "codelists/opensafely-temporary-immunosuppression.csv", system="ctv3", column="CTV3ID"
)
chronic_cardiac_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease-2020-04-08.csv", system="ctv3", column="CTV3ID"
)
intellectual_disability_including_downs_syndrome_codes = codelist_from_csv(
    "codelists/opensafely-intellectual-disability-including-downs-syndrome-2020-08-27.csv", system="ctv3", column="CTV3ID"
)
dialysis_codes = codelist_from_csv(
    "codelists/opensafely-dialysis-2020-07-16.csv", system="ctv3", column="CTV3ID"
)
other_respiratory_conditions_codes = codelist_from_csv(
    "codelists/opensafely-other-respiratory-conditions-2020-07-21.csv", system="ctv3", column="CTV3ID"
)
heart_failure_codes = codelist_from_csv(
    "codelists/opensafely-heart-failure-2020-05-05.csv", system="ctv3", column="CTV3ID"
)
other_heart_disease_codes = codelist_from_csv(
    "codelists/opensafely-other-heart-disease-2020-05-11.csv", system="ctv3", column="CTV3ID"
)
diabetes_codes = codelist_from_csv(
    "codelists/opensafely-diabetes.csv", system="ctv3", column="CTV3ID"
)
chronic_kidney_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-kidney-disease.csv", system="ctv3", column="CTV3ID"
)
chronic_liver_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-liver-disease.csv", system="ctv3", column="CTV3ID"
)
other_neuro_codes = codelist_from_csv(
    "codelists/opensafely-other-neurological-conditions-2020-06-02.csv", system="ctv3", column="CTV3ID"
)
dementia_codes = codelist_from_csv(
    "codelists/opensafely-dementia.csv", system="ctv3", column="CTV3ID"
)
stroke_codes = codelist_from_csv(
    "codelists/opensafely-stroke-updated.csv", system="ctv3", column="CTV3ID"
)
ethnicity_codes = codelist_from_csv(
    "codelists/opensafely-ethnicity-2020-04-27.csv", system="ctv3", column="Code", category_column="Grouping_6",
)