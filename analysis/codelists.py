from cohortextractor import codelist_from_csv

solid_organ_transplantation_codes = codelist_from_csv(
    "codelists/opensafely-solid-organ-transplantation.csv",
    system="ctv3",
    column="CTV3ID",
)
chemotherapy_or_radiotherapy_codes = codelist_from_csv(
    "codelists/opensafely-chemotherapy-or-radiotherapy.csv",
    system="ctv3",
    column="CTV3ID",
)
cancer_excluding_lung_and_haematological_codes = codelist_from_csv(
    "codelists/opensafely-cancer-excluding-lung-and-haematological.csv",
    system="ctv3",
    column="CTV3ID",
)
lung_cancer_codes = codelist_from_csv(
    "codelists/opensafely-lung-cancer.csv",
    system="ctv3",
    column="CTV3ID",
)
haematological_cancer_codes = codelist_from_csv(
    "codelists/opensafely-haematological-cancer.csv",
    system="ctv3",
    column="CTV3ID",
)
bone_marrow_transplant_codes = codelist_from_csv(
    "codelists/opensafely-bone-marrow-transplant.csv",
    system="ctv3",
    column="CTV3ID",
)
cystic_fibrosis_codes = codelist_from_csv(
    "codelists/opensafely-cystic-fibrosis.csv",
    system="ctv3",
    column="CTV3ID",
)
asthma_diagnosis_codes = codelist_from_csv(
    "codelists/opensafely-asthma-diagnosis.csv",
    system="ctv3",
    column="CTV3ID",
)
current_copd_codes = codelist_from_csv(
    "codelists/opensafely-current-copd.csv", system="ctv3", column="CTV3ID"
)
sickle_cell_disease_codes = codelist_from_csv(
    "codelists/opensafely-sickle-cell-disease.csv",
    system="ctv3",
    column="CTV3ID",
)
permanent_immunosuppression_codes = codelist_from_csv(
    "codelists/opensafely-permanent-immunosuppression.csv",
    system="ctv3",
    column="CTV3ID",
)
temporary_immunosuppression_codes = codelist_from_csv(
    "codelists/opensafely-temporary-immunosuppression.csv",
    system="ctv3",
    column="CTV3ID",
)
chronic_cardiac_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease.csv",
    system="ctv3",
    column="CTV3ID",
)
intellectual_disability_including_downs_syndrome_codes = codelist_from_csv(
    "codelists/opensafely-intellectual-disability-including-downs-syndrome.csv",
    system="ctv3",
    column="CTV3ID",
)
dialysis_codes = codelist_from_csv(
    "codelists/opensafely-dialysis.csv",
    system="ctv3",
    column="CTV3ID",
)
other_respiratory_conditions_codes = codelist_from_csv(
    "codelists/opensafely-other-respiratory-conditions.csv",
    system="ctv3",
    column="CTV3ID",
)
heart_failure_codes = codelist_from_csv(
    "codelists/opensafely-heart-failure.csv",
    system="ctv3",
    column="CTV3ID",
)
other_heart_disease_codes = codelist_from_csv(
    "codelists/opensafely-other-heart-disease.csv",
    system="ctv3",
    column="CTV3ID",
)
diabetes_codes = codelist_from_csv(
    "codelists/opensafely-diabetes.csv", system="ctv3", column="CTV3ID"
)
chronic_kidney_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-kidney-disease.csv",
    system="ctv3",
    column="CTV3ID",
)
chronic_liver_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-liver-disease.csv",
    system="ctv3",
    column="CTV3ID",
)
other_neuro_codes = codelist_from_csv(
    "codelists/opensafely-other-neurological-conditions.csv",
    system="ctv3",
    column="CTV3ID",
)
#dementia_codes = codelist_from_csv(
#    "codelists/opensafely-dementia.csv", system="ctv3", column="CTV3ID"
#)
#stroke_codes = codelist_from_csv(
#    "codelists/opensafely-stroke-updated.csv", system="ctv3", column="CTV3ID"
#)
ethnicity_codes = codelist_from_csv(
    "codelists/opensafely-ethnicity.csv",
    system="ctv3",
    column="Code",
    category_column="Grouping_6",
)
salbutamol_codes = codelist_from_csv(
    "codelists/opensafely-asthma-inhaler-salbutamol-medication.csv",
    system="snomed",
    column="id",
)
psychosis_schizophrenia_bipolar_affective_disease_codes = codelist_from_csv(
    "codelists/opensafely-psychosis-schizophrenia-bipolar-affective-disease.csv", system="ctv3", column="CTV3Code"
)
