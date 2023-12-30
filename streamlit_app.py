import pandas as pd

import pandas_profiling

import streamlit as st

from streamlit_pandas_profiling import st_profile_report

from pandas_profiling import ProfileReport

df = pd.read_csv("TrainingData.csv")

profile = ProfileReport(df,

                        title="Bank Training Dataset",

        dataset={

        "description": "This profiling report was generated for Bank Loan Approval",

        "copyright_holder": "@Majety Harsha",

        "copyright_year": "2023",

        "url": "https://www.linkedin.com/in/majety-n-v-sai-rama-harsha-726145229",

    },

    variables={

        "descriptions": {

            "Id": "Identity",

            "Income": "Income of the Customer",

            "Age": "Age of the Person",

            "Experience": "Experience of person in years",

            "Married/Single": "Maritial Status",

            "House_Ownership": "Does the customer having own house?",

            "Car_Ownership": "Does the customer having own car?",
            "Profession":"Occupation of the customer",
            "City":"City",
            "State":"State",
            "CURRENT_JOB_YRS":"CURRENT_JOB_YRS",
            "CURRENT_HOUSE_YRS":"CURRENT_HOUSE_YRS",
            "Risk_Flag":"Risk for the bank"
        }
    }
)

st.title("Bank loan Dataset")

st.write(df)

st_profile_report(profile)