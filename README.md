# Status of Work

This work was conducted between October 2020 and January 2021. In January 2021 this analysis was superseeded by the "SARS-CoV2 (COVID-19) Vaccine Uptake Reporting Specification" - https://github.com/opensafely/primis-covid-vacc-uptake-spec.  It is published here as record but not to be used for onward development, decision making or analysis.

# Vaccine Eligibility

Calculate counts of eligble patients for the Covid vaccine based on the priorities set out in the [Green Book](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/941450/Greenbook_chapter_14a_v2.pdf) and [GOV advice](https://www.gov.uk/government/publications/guidance-on-shielding-and-protecting-extremely-vulnerable-persons-from-covid-19/guidance-on-shielding-and-protecting-extremely-vulnerable-persons-from-covid-19#cev) for clinically extremely vulnerable.

Monitors 1st and 2nd dose vaccinations through TPP vaccination record for target_disease_matches="SARS-2 CORONAVIRUS"

* Raw model outputs, including charts, crosstabs, etc, are in `released_analysis_results/`
* If you are interested in how we defined our variables, take a look at the [study definition](analysis/study_definition.py); this is written in `python`, but non-programmers should be able to understand what is going on there
* If you are interested in how we defined our code lists, look in the [codelists folder](./codelists/).

# Project Information

## Priority Definitions (Source: Green Book):

1. Residents in a care home for older adults & Staff working in care homes for older adults
2. All those 80 years of age and over & Health and social care workers
3. All those 75 years of age and over
4. All those 70 years of age and over & Clinically extremely vulnerable individuals (not including pregnant women and those under 18 years of age)
5. All those 65 years of age and over
6. Adults aged 18 to 65 years in an at-risk group
7. All those 60 years of age and over
8. All those 55 years of age and over
9. All those 50 years of age and over 
10. Rest of the population (priority to be determined)

## Worker Demographics (source: NHS D):

The approach considered in this analysis is to calculate the vaccine priority cohorts from primary care data, mostly based on age and a set list of high/moderate risk health conditions without health care workers considered.  The age, gender and ethnicity profiles will then be analysed.  At this point the priority cohorts are adapted to include the impact of the health and care workforce with aggregate figures presented.  However, no individual analysis can be conducted at this point as we don’t have the data at a granular level to match individuals to probability of being a health and care worker.  

**Care home workers:**
Social Care Residential - 675K

**Health and Social Care Workers:**
Social Care non-residential - 868k 
Health and social care workers - 1.32m
General Practice - 187k 
Dentistry - 96k
Community Pharmacy - 96k

## Risk Classification: 

[OpenSafely codelist](https://codelists.opensafely.org/) identified against each definition from above source *italicize*.

**Clinically extremely vulnerable individuals** - (https://www.gov.uk/government/publications/guidance-on-shielding-and-protecting-extremely-vulnerable-persons-from-covid-19/guidance-on-shielding-and-protecting-extremely-vulnerable-persons-from-covid-19#cev)
- on the shielding list - **not considered** but large overlap of shielding list definition with the rest of the clinically extremeley vulnerable criteria
- solid organ transplant recipients - *Solid Organ Transplantation*
- people with specific cancers:
  - are having chemotherapy or antibody treatment for cancer, including immunotherapy - *Chemotherapy or Radiotherapy* with *Cancer excluding lung and haematological*
  - are having an intense course of radiotherapy (radical radiotherapy) for lung cancer - *Chemotherapy or Radiotherapy* with *Lung Cancer*
  - are having targeted cancer treatments that can affect the immune system (such as protein kinase inhibitors or PARP inhibitors) - **Not considered**
  - have blood or bone marrow cancer (such as leukaemia, lymphoma or myeloma) - *Haematological cancer*
  - have had a bone marrow or stem cell transplant in the past 6 months, or are still taking immunosuppressant medicine - *Bone Marrow Transplant* in last 6 months (immunosuppressant medicine covered by dmards below)
- have been told by a doctor you have a severe lung condition (such as cystic fibrosis, severe asthma or severe COPD) - *Cystic Fibrosis* or (*Asthma Diagnosis* not included here as awaiting severe definition) or *Current COPD*
- have a condition that means they have a very high risk of getting infections (such as SCID or sickle cell) - *Sickle Cell Disease* or (**SCID not considered**)
- are taking medicine that makes them much more likely to get infections (such as high doses of steroids or immunosuppressant medicine) - *permanaent immunosuppression* or *temporary immunosuppression* or *dmards*
- problems with your spleen, e.g. splenectomy (having your spleen removed) - *asplenia*
- have a serious heart condition and are pregnant - (Could use *Chronic Cardiac Disease* with *pregnant* but currently **not considered**)
are an adult with Down's syndrome - *Intellectual disability including Down's Syndrome*
are an adult who is having dialysis or has severe (stage 5) long-term kidney disease - *Dialysis*
have been classed as clinically extremely vulnerable, based on clinical judgement and an assessment of your needs - **not considered ** Can’t code this and similar to being on the shielding list.

**At-risk group** - (COVID-19 Green Book Chapter 14a (Provisional guidance subject to MHRA approval of vaccine supply))
- Chronic respiratory disease - Individuals with a severe lung condition, including those with asthma that requires continuous or repeated use of systemic steroids or with previous exacerbations requiring hospital admission, and chronic obstructive pulmonary disease (COPD) including chronic bronchitis and emphysema; bronchiectasis, cystic fibrosis, interstitial lung fibrosis, pneumoconiosis and bronchopulmonary dysplasia (BPD).have a lung condition that's not severe (such as asthma, COPD, emphysema or bronchitis) - *Asthma Diagnosis* with *Salbutamol prescribed( or *Other Respiratory Conditions*
- Chronic heart disease and vascular disease - Congenital heart disease, hypertension with cardiac complications, chronic heart failure, individuals requiring regular medication and/or follow-up for ischaemic heart disease. This includes individuals with atrial fibrillation, peripheral vascular disease or a history of venous thromboembolism - *Heart Failure* or *Other Heart Disease*
- Diabetes - Type 1 diabetes, type 2 diabetes requiring insulin or oral hypoglycaemic drugs, diet-controlled diabetes - *Diabetes* (Needs further refining)
- Chronic kidney disease - Chronic kidney disease at stage 3, 4 or 5, chronic kidney failure, nephrotic syndrome, kidney transplantation - *Chronic Kidney Disease*
- Chronic liver disease - Cirrhosis, biliary atresia, chronic hepatitis - *Chronic Liver Disease*
- Chronic neurological disease - Stroke, transient ischaemic attack (TIA). Conditions in which respiratory function may be compromised due to neurological disease (e.g. polio syndrome sufferers). This includes individuals with cerebral palsy, severe or profound learning disabilities, Down’s Syndrome, multiple sclerosis, epilepsy, dementia, Parkinson’s disease, motor neurone disease and related or similar conditions; or hereditary and degenerative disease of the nervous system or muscles; or severe neurological disability - *Other Neurological Conditions*
- Immunosuppression - Immunosuppression due to disease or treatment, including patients undergoing chemotherapy leading to immunosuppression, patients undergoing radical radiotherapy, solid organ transplant recipients, bone marrow or stem cell transplant recipients, HIV infection at all stages, multiple myeloma or genetic disorders affecting the immune system (e.g. IRAK-4, NEMO, complement disorder, SCID). Individuals who are receiving immunosuppressive or immunomodulating biological therapy including, but not limited to, anti-TNF, alemtuzumab, ofatumumab, rituximab, patients receiving protein kinase inhibitors or PARP inhibitors, and individuals treated with steroid sparing agents such as cyclophosphamide and mycophenolate mofetil. Individuals treated with or likely to be treated with systemic steroids for more than a month at a dose equivalent to prednisolone at 20mg or more per day (any age). Anyone with a history of haematological malignancy, including leukaemia, lymphoma, and myeloma and those with systemic lupus erythematosus and rheumatoid arthritis, and psoriasis who may require long term immunosuppressive treatments. Some immunocompromised patients may have a suboptimal immunological response to the vaccine - Covered in the clinically extremley vulnerable. 
- Asplenia or dysfunction of the spleen - This also includes conditions that may lead to splenic dysfunction, such as homozygous sickle cell disease, thalassemia major and coeliac syndrome - *asplenia*
- Morbid Obesity - Adults with a Body Mass Index >= 40 kg/m2 - *bmi value*
- Severe mental illness - Individuals with schizophrenia or bipolar disorder, or any mental illness that causes severe functional impairment - *Psychosis, schizophrenia + bipolar affective disease*
- Adult Carers - **Not considered**
- Adult household members, close contacts and carers of immunocompromised adults - **Not considered**
- Younger adults in long-stay nursing and residential care setting - *Care home flag* with *age*

## Independent Variables
- Age
- Sex
- Care home status
- Ethnicity
- STP
- MSOA
- IMD
- Rural

## Ethics Approval
Work falls under service evaluation/audit


# About the OpenSAFELY framework

The OpenSAFELY framework is a new secure analytics platform for
electronic health records research in the NHS.

Instead of requesting access for slices of patient data and
transporting them elsewhere for analysis, the framework supports
developing analytics against dummy data, and then running against the
real data *within the same infrastructure that the data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org).

The framework is under fast, active development to support rapid
analytics relating to COVID19; we're currently seeking funding to make
it easier for outside collaborators to work with our system.  You can
read our current roadmap [here](ROADMAP.md).
