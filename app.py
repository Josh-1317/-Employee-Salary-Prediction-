import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import base64
import os

# --------- Page Setup --------- #
st.set_page_config(page_title="💼 Income Classifier", layout="wide")

# Load model pipeline
pipeline = joblib.load("salary_pipeline_model.pkl")

# --------- Mapping for education --------- #
education_mapping = {
    0: "Preschool", 1: "1st-4th", 2: "5th-6th", 3: "7th-8th", 4: "9th",
    5: "10th", 6: "11th", 7: "12th", 8: "HS-grad", 9: "Some-college",
    10: "Assoc-acdm", 11: "Assoc-voc", 12: "Bachelors", 13: "Masters", 14: "Doctorate",
}
# Dark mode toggle
dark_mode = st.toggle("🌞 / 🌙", value=False, help="Toggle dark mode")
background_color = "#0E1117" if dark_mode else "#FFFFFF"
font_color = "#FAFAFA" if dark_mode else "#000000"

# Background image setup
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64_image("images/background.png")

st.markdown(
    f"""
    <style>
        /* Background styling */
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image}");
            background-size: cover;
            background-position: center;
        }}

        .title-container {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}

        .logo-small {{
            width: 60px;
            height: auto;
        }}

        .dark .stMarkdown {{
            color: white;
        }}

        /* ✅ Change only font size of input values */
        input[type="number"], input[type="text"] {{
            font-size: 18px !important;
        }}

        .stSelectbox div[data-baseweb="select"] * {{
            font-size: 18px !important;
        }}

        .stRadio > div > label {{
            font-size: 18px !important;
        }}

        .css-1uccc91-singleValue, .css-qc6sy-singleValue {{
            font-size: 18px !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# --------- Logo and Title --------- #
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image("images/logo.png", width=120)
with col2:
    st.markdown(f"<h1 style='margin-bottom:0; color:{font_color};'>💼 Income Classifier</h1>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='margin-top:0; color:{font_color};'>Enter Employee Details</h4>", unsafe_allow_html=True)

st.markdown("---")

# --------- Input Form --------- #
with st.form("income_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
      age = st.number_input("Age", 18, 90, 30)
      fnlwgt = st.number_input("FNLWGT", 10000, 1000000, 200000)

    # Education dropdown with mapping
      education_options = {
        "Preschool": 0,
        "1st-4th": 1,
        "5th-6th": 2,
        "7th-8th": 3,
        "9th": 4,
        "10th": 5,
        "11th": 6,
        "12th": 7,
        "HS-grad": 8,
        "Some-college": 9,
        "Assoc-acdm": 10,
        "Assoc-voc": 11,
        "Bachelors": 12,
        "Masters": 13,
        "Doctorate": 14,
    }
    education_str = st.selectbox("Education Level", list(education_options.keys()))
    education_num = education_options[education_str]


    with col2:
        capital_gain = st.number_input("Capital Gain", 0, 100000, 0)
        capital_loss = st.number_input("Capital Loss", 0, 100000, 0)
        hours_per_week = st.number_input("Hours/Week", 1, 100, 40)

    with col3:
        workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay'])
        marital_status = st.selectbox("Marital Status", ['Never-married', 'Married-civ-spouse', 'Divorced', 'Separated', 'Widowed', 'Married-spouse-absent'])
        occupation = st.selectbox("Occupation", ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners'])

    col4, col5, col6 = st.columns(3)

    with col4:
        relationship = st.selectbox("Relationship", ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])

    with col5:
        race = st.selectbox("Race", ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'])

    with col6:
        gender = st.radio("Gender", ['Male', 'Female'])
        native_country = st.selectbox("Country", ['United-States', 'India', 'Mexico', 'Philippines', 'Germany', 'Canada'])

    submitted = st.form_submit_button("💰 Predict Income")


# Simple avatar logic
import streamlit as st
import pandas as pd

# --------- Avatar Display --------- #
def get_avatar(gender):
    if gender.lower() == 'male':
        return "images/avatars/male_1st.png"
    return "images/avatars/female_1st.png"

avatar_path = get_avatar(gender)
st.image(avatar_path, width=160, caption=f"{gender} Avatar")



# --------- Prediction --------- #
if submitted:
    input_data = pd.DataFrame([{
        'age': age,
        'fnlwgt': fnlwgt,
        'educational-num': education_num,
        'capital-gain': capital_gain,
        'capital-loss': capital_loss,
        'hours-per-week': hours_per_week,
        'workclass': workclass,
        'marital-status': marital_status,
        'occupation': occupation,
        'relationship': relationship,
        'race': race,
        'gender': gender,
        'native-country': native_country
    }])

    prediction = pipeline.predict(input_data)[0]

    label = "Income > ₹50K" if prediction == 1 else "Income ≤ ₹50K"
    emoji = "🤑" if prediction == 1 else "😐"
    result_color = "#ccc900" if prediction == 1 else "#ff3636"
    st.markdown(
    f"""
    <div style='
        color: {result_color}; 
        font-size: 28px; 
        font-weight: bold; 
        padding: 10px; 
        text-align: center;
        border: 2px solid {result_color};
        border-radius: 10px;
        background-color: {'#fef6d3' if prediction == 1 else '#ffe5e5'};
    '>
        {emoji} Predicted Income Class: {label}
    </div>
    """,
    unsafe_allow_html=True
)


    # Visualization using Gauge chart
    gauge_value = 90 if prediction == 1 else 30
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=gauge_value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Probability Score", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#00CC96" if prediction == 1 else "#FF4136"},
            'steps': [
                {'range': [0, 50], 'color': "#FFDDDD"},
                {'range': [50, 100], 'color': "#DDFFDD"}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)


