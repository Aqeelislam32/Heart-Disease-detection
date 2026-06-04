import streamlit as st
import numpy as np
import joblib

# Load model only
try:
    model = joblib.load("random_forest_model.joblib")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Custom CSS for professional look
st.markdown("""
    <style>
    .stApp {
        background-color: #d1e9ff;
    }
    .main-title {
        color: #0e4d92;
        text-align: center;
        font-weight: 800;
        padding-bottom: 10px;
        text-shadow: 2px 2px 5px red;
    }
    .description-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1e88e5;
        color: #444;
        margin-bottom: 25px;
    }
    [data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] label {
        font-size: 23px !important;
        color: #0e4d92 !important;
        font-weight: 600 !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ef6c00;
        color: white;
        font-weight: bold;
        font-size: 20px !important;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #e65100;
        color: white;
        border: none;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    div[data-baseweb="input"], div[data-baseweb="select"], div[data-baseweb="input"] > div {
        background-color: #fcf8f3 !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🫀 Heart Disease Prediction App</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class='description-box'>
        Welcome to the <b>Heart Disease Diagnostic Tool</b>. Please enter the patient's clinical data below 
        to predict the risk of heart disease using our trained machine learning model.
    </div>
""", unsafe_allow_html=True)

st.divider()

# Inputs - Arranged line by line for a professional look
age = st.number_input("Age - Enter the patient's age", 1, 100, help="Patient's age in years")
sex = st.selectbox("Sex - Select the patient's gender", [1, 0], format_func=lambda x: "Male" if x == 1 else "Female", help="Biological sex of the patient")
cp = st.selectbox("Chest Pain Type - Select the type of pain (0-3)", [0, 1, 2, 3], format_func=lambda x: {0: "Typical Angina", 1: "Atypical Angina", 2: "Non-anginal Pain", 3: "Asymptomatic"}[x], help="0: Typical Angina, 1: Atypical Angina, 2: Non-anginal, 3: Asymptomatic")
trestbps = st.number_input("Resting BP (mm Hg) - Enter the resting blood pressure", help="Resting blood pressure on admission to the hospital")
chol = st.number_input("Cholesterol (mg/dl) - Enter the cholesterol level", help="Serum cholesterol level")
fbs = st.selectbox("Fasting Blood Sugar - Select if sugar > 120 mg/dl", [0, 1], format_func=lambda x: "True (> 120 mg/dl)" if x == 1 else "False (<= 120 mg/dl)", help="Is fasting blood sugar higher than 120 mg/dl?")
restecg = st.selectbox("Resting ECG - Select the results (0-2)", [0, 1, 2], format_func=lambda x: {0: "Normal", 1: "ST-T Wave Abnormality", 2: "Left Ventricular Hypertrophy"}[x], help="Resting electrocardiographic results")
thalach = st.number_input("Max Heart Rate - Enter the maximum heart rate achieved", help="Maximum heart rate achieved during stress test")
exang = st.selectbox("Exercise Induced Angina - Select if exercise causes chest pain", [0, 1], format_func=lambda x: "Yes (Chest pain induced by exercise)" if x == 1 else "No (No chest pain during exercise)", help="Did exercise cause chest pain?")
oldpeak = st.number_input("ST Depression (Oldpeak) - Enter the ST depression value", 0.0, 10.0, help="ST depression induced by exercise relative to rest")
slope = st.selectbox("Slope - Select the slope of the peak exercise ST segment (0-2)", [0, 1, 2], format_func=lambda x: {0: "Upsloping", 1: "Flat", 2: "Downsloping"}[x], help="The slope of the peak exercise ST segment")
ca = st.selectbox("Major Vessels - Number of major vessels colored by fluoroscopy (0-4)", [0, 1, 2, 3, 4], format_func=lambda x: {0: "0 Vessels (None)", 1: "1 Vessel", 2: "2 Vessels", 3: "3 Vessels", 4: "4 (Unknown/Not Available)"}[x], help="Number of major vessels (0-3) colored by fluoroscopy. Option 4 represents missing or unavailable data.")
thal = st.selectbox("Thalassemia - Select the thalassemia blood disorder type (0-3)", [0, 1, 2, 3], format_func=lambda x: {0: "0 (Unknown)", 1: "1 (Normal)", 2: "2 (Fixed Defect)", 3: "3 (Reversible Defect)"}[x], help="Blood disorder types: 1 = normal; 2 = fixed defect; 3 = reversable defect. 0 is used for unknown values.")

if st.button("Run Diagnostic Assessment"):
    try:
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("### ⚠️ Result: High Risk of Heart Disease")
        else:
            st.success("### ✅ Result  No Heart Disease")
    except Exception as e:
        st.warning(f"An error occurred during prediction: {e}")