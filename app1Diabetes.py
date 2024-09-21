import streamlit as st
import pickle
import numpy as np

# Load the trained model
# model = pickle.load(open("lo.pkl","rb"))
model = pickle.load(open(r"C:\Users\Lenovo\OneDrive\Desktop\Jupyter notebook\lo.pkl", "rb"))


# Set up the title and introduction
st.title("Diabetes Prediction")
st.write("""
This is a diabetes prediction app. Enter the details below to find out if you are at risk of diabetes.
""")

# # User inputs for features
pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=0, step=1)
glucose = st.number_input('Glucose Level', min_value=0, max_value=200, value=100)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=150, value=70)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=20)
insulin = st.number_input('Insulin', min_value=0, max_value=900, value=80)
bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0)
diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input('Age', min_value=1, max_value=120, value=25)

# # Create a button for prediction
if st.button('Predict'):
    # Create a numpy array for model prediction
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Show the result
    if prediction[0] == 1:
        st.write("The model predicts that you are at risk of diabetes.")
    else:
        st.write("The model predicts that you are not at risk of diabetes.")

