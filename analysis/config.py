#study start date.  should match date in project.yaml
start_date = "2020-12-01"

#study end date.  should match date in project.yaml
end_date = "2021-04-01"

#demographic variables by which code use is broken down
#select from ["sex", "age_band", "region", "imd", "ethnicity", "learning_disability"]
demographics = ["age_band", "region"]

#name of measure
marker="COVID vaccine declined"

#codelist path
codelist_path = "codelists/primis-covid19-vacc-uptake-cov1decl.csv"

#column name referencing code in chosen codelist
codelist_code_column="code"

#codelist system for chosen codelist
codelist_system = "snomed"

#column name referencing code descriptions in chosen codelist
codelist_term_column='term'