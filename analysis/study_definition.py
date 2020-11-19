from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists
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
        "2019-02-01", "2020-02-01"
    ),
    # The rest of the lines define the covariates with associated GitHub issues
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/33
    age=patients.age_as_of(
        "2020-02-01",
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
        "2020-02-01",
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
            "category": {"ratios": {"PC": 0.05, "PN": 0.05, "PS": 0.05, "U": 0.85,},},
        },
    ),

    # ETHNICITY IN 6 CATEGORIES
    ethnicity=patients.with_these_clinical_events(
        ethnicity_codes,
        returning="category",
        find_last_match_in_period=True,
        include_date_of_match=False,
        return_expectations={
            "category": {"ratios": {"1": 0.2, "2":0.2, "3":0.2, "4":0.2, "5": 0.2}},
            "incidence": 0.75,
        },
    ),
    
    chronic_kidney_disease=patients.with_these_clinical_events(
        chronic_kidney_disease_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/12
    chronic_liver_disease=patients.with_these_clinical_events(
        chronic_liver_disease_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
        
    current_copd=patients.with_these_clinical_events(
        current_copd_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
        
    dementia=patients.with_these_clinical_events(
        dementia_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
        
    diabetes=patients.with_these_clinical_events(
        diabetes_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
        
    haematological_cancer=patients.with_these_clinical_events(
        haematological_cancer_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
    
    other_neuro=patients.with_these_clinical_events(
        other_neuro_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
        
    permanant_immunosuppression=patients.with_these_clinical_events(
        permanent_immunosuppression_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
        
    temporary_immunosuppression=patients.with_these_clinical_events(
        temporary_immunosuppression_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
        
    solid_organ_transplantation=patients.with_these_clinical_events(
        solid_organ_transplantation_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
        
    stroke=patients.with_these_clinical_events(
        stroke_codes,
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/10
    bmi=patients.most_recent_bmi(
        on_or_after="2010-02-01",
        minimum_age_at_measurement=16,
        include_measurement_date=False,
        include_month=True,
        return_expectations={
            "incidence": 0.6,
            "float": {"distribution": "normal", "mean": 28, "stddev": 10},
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/54
    stp=patients.registered_practice_as_of(
        "2020-02-01",
        returning="stp_code",
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"STP1": 0.5, "STP2": 0.5}},
        },
    ),
    msoa=patients.registered_practice_as_of(
        "2020-02-01",
        returning="msoa_code",
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"MSOA1": 0.5, "MSOA2": 0.5}},
        },
    ),
    # https://github.com/ebmdatalab/tpp-sql-notebook/issues/52
    imd=patients.address_as_of(
        "2020-02-01",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"100": 0.1, "200": 0.2, "300": 0.7}},
        },
    ),
    rural_urban=patients.address_as_of(
        "2020-02-01",
        returning="rural_urban_classification",
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"rural": 0.1, "urban": 0.9}},
        },
    ),
)
