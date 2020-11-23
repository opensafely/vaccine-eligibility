from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists,
)
from codelists import *

study = StudyDefinition(
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "exponential_increase",
    },
    # This line defines the study population
    population=patients.registered_with_one_practice_between(
        "2019-02-01", "2020-10-01"
    ),
    # The rest of the lines define the covariates with associated GitHub issues
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/33
    age=patients.age_as_of(
        "2020-10-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/46
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),
    care_home_type=patients.care_home_status_as_of(
        "2020-10-01",
        categorised_as={
            "PC": """
              IsPotentialCareHome
              AND LocationDoesNotRequireNursing='Y'
              AND LocationRequiresNursing='N'
            """,
            "PN": """
              IsPotentialCareHome
              AND LocationDoesNotRequireNursing='N'
              AND LocationRequiresNursing='Y'
            """,
            "PS": "IsPotentialCareHome",
            "U": "DEFAULT",
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "PC": 0.05,
                    "PN": 0.05,
                    "PS": 0.05,
                    "U": 0.85,
                },
            },
        },
    ),
    # Ethnicity in 6 categories
    ethnicity=patients.with_these_clinical_events(
        ethnicity_codes,
        returning="category",
        find_last_match_in_period=True,
        include_date_of_match=False,
        return_expectations={
            "category": {
                "ratios": {"1": 0.2, "2": 0.2, "3": 0.2, "4": 0.2, "5": 0.2}
            },
            "incidence": 0.75,
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/54
    stp=patients.registered_practice_as_of(
        "2020-10-01",
        returning="stp_code",
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"STP1": 0.5, "STP2": 0.5}},
        },
    ),
    msoa=patients.registered_practice_as_of(
        "2020-10-01",
        returning="msoa_code",
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"MSOA1": 0.5, "MSOA2": 0.5}},
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/52
    imd=patients.address_as_of(
        "2020-10-01",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"100": 0.1, "200": 0.2, "300": 0.7}},
        },
    ),
    rural_urban=patients.address_as_of(
        "2020-10-01",
        returning="rural_urban_classification",
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"rural": 0.1, "urban": 0.9}},
        },
    ),
    ####### HIGH RISK CODELISTS #######
    # https://github.com/opensafely/codelist-development/issues/9
    solid_organ_transplantation=patients.with_these_clinical_events(
        solid_organ_transplantation_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/10
    chemo_or_radio=patients.with_these_clinical_events(
        chemotherapy_or_radiotherapy_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/10
    lung_cancer=patients.with_these_clinical_events(
        lung_cancer_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/10
    cancer_excl_lung_and_haem=patients.with_these_clinical_events(
        cancer_excluding_lung_and_haematological_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/10
    haematological_cancer=patients.with_these_clinical_events(
        haematological_cancer_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # In last 6 months
    # https://github.com/opensafely/codelist-development/issues/10
    bone_marrow_transplant=patients.with_these_clinical_events(
        bone_marrow_transplant_codes,
        between=["2020-04-01", "2020-10-01"],
        returning="number_of_matches_in_period",
        return_expectations={
            "int": {"distribution": "normal", "mean": 1, "stddev": 0.1},
            "incidence": 0.05,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/30
    cystic_fibrosis=patients.with_these_clinical_events(
        cystic_fibrosis_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/15
    # Severe Asthma - NOT DEFINED YET
    severe_asthma=patients.with_these_clinical_events(
        asthma_diagnosis_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/ics-research/issues/12
    current_copd=patients.with_these_clinical_events(
        current_copd_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/4
    sickle_cell_disease=patients.with_these_clinical_events(
        sickle_cell_disease_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/11
    permanant_immunosuppression=patients.with_these_clinical_events(
        permanent_immunosuppression_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/11
    temporary_immunosuppression=patients.with_these_clinical_events(
        temporary_immunosuppression_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/2
    chronic_cardiac_disease=patients.with_these_clinical_events(
        chronic_cardiac_disease_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/29
    intel_dis_incl_downs_syndrome=patients.with_these_clinical_events(
        intellectual_disability_including_downs_syndrome_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/28
    dialysis=patients.with_these_clinical_events(
        dialysis_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    ####### MODERATE RISK CODELISTS #######
    # non-severe asthma - NOT DEFINED YET
    # https://github.com/opensafely/codelist-development/issues/15
    non_severe_asthma=patients.with_these_clinical_events(
        asthma_diagnosis_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/ics-research/issues/10
    other_respiratory_conditions=patients.with_these_clinical_events(
        other_respiratory_conditions_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/80
    heart_failure=patients.with_these_clinical_events(
        heart_failure_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/83
    other_heart_disease=patients.with_these_clinical_events(
        other_heart_disease_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/8
    diabetes=patients.with_these_clinical_events(
        diabetes_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/risk-factors-research/issues/50
    chronic_kidney_disease=patients.with_these_clinical_events(
        chronic_kidney_disease_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/12
    chronic_liver_disease=patients.with_these_clinical_events(
        chronic_liver_disease_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/5
    other_neuro=patients.with_these_clinical_events(
        other_neuro_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/5
    dementia=patients.with_these_clinical_events(
        dementia_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/opensafely/codelist-development/issues/20
    stroke=patients.with_these_clinical_events(
        stroke_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/10
    bmi=patients.most_recent_bmi(
        on_or_after="2010-02-01",
        minimum_age_at_measurement=16,
        include_measurement_date=False,
        include_month=True,
        return_expectations={
            "incidence": 0.3,
            "float": {"distribution": "normal", "mean": 28, "stddev": 10},
        },
    ),
)
