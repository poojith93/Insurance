import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Insurance Cost Prediction",
    page_icon="🏥",
    layout="wide"
)

# Title
st.title("🏥 Insurance Cost Prediction")
st.write("Machine Learning Based Insurance Cost Predictor")

st.markdown("---")

# Input Fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 25)
    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)

with col2:
    children = st.number_input("Children", 0, 10, 0)
    smoker = st.selectbox("Smoker", ["No", "Yes"])

# Predict Button
if st.button("Predict"):
    st.success("Streamlit is working successfully!")
    
    # Dummy prediction
    estimated_cost = age * bmi * 10
    
    st.metric(
        label="Estimated Insurance Cost",
        value=f"₹ {estimated_cost:,.2f}"
    )

st.markdown("---")
st.caption("Insurance Cost Prediction Project")