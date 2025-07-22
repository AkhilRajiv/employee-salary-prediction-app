import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('employee_salary_model.joblib')

st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼")

st.title("💼 Employee Salary Prediction Software")
st.write("Enter employee details to estimate their expected salary.")

# Input form
experience = st.slider("Years of Experience", 0, 30, 1)
education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
job_title = st.selectbox("Job Title", ["Software Engineer", "Manager"])

# Prepare input data
def prepare_input(exp, edu, job):
    return pd.DataFrame([{
        'YearsExperience': exp,
        "EducationLevel_Master's": 1 if edu == "Master's" else 0,
        'EducationLevel_PhD': 1 if edu == 'PhD' else 0,
        'JobTitle_Manager': 1 if job == 'Manager' else 0,
        'JobTitle_Software Engineer': 1 if job == 'Software Engineer' else 0
    }])

# Predict salary
if st.button("Predict Salary"):
    input_df = prepare_input(experience, education, job_title)
    predicted_salary = model.predict(input_df)[0]
    st.success(f"💰 Predicted Salary: ₹{predicted_salary:,.2f}")
