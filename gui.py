import streamlit as st
from joblib import load  # or joblib, depending on your saved model
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    # Cache only the loading of the model
    return load('housepricepredictor.joblib') 

model = load_model()
# App title
st.title("House Price Predictor")

# Input fields for user
st.header("Enter the Details of the House:")

# Collecting user inputs
bedrooms = st.number_input("Number of Bedrooms:", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms:", min_value=1, max_value=10, value=2)
living_area = st.number_input("Living Area (in sq ft):", min_value=100, value=1500)
lot_area = st.number_input("Lot Area (in sq ft):", min_value=100, value=5000)
floors = st.number_input("Number of Floors:", min_value=1, max_value=5, value=1)
grade = st.selectbox("Grade of the House (1-13):", options=list(range(1, 14)), index=6)
house_area = st.number_input("Area of the House (excluding basement, in sq ft):", min_value=100, value=1200)
basement_area = st.number_input("Area of the Basement (in sq ft):", min_value=0, value=500)
built_year = st.number_input("Built Year:", min_value=1800, max_value=2024, value=2000)
living_area_renov = st.number_input("Living Area after Renovation (in sq ft):", min_value=0, value=1500)
lot_area_renov = st.number_input("Lot Area after Renovation (in sq ft):", min_value=0, value=5000)
schools_nearby = st.number_input("Number of Schools Nearby:", min_value=0, max_value=20, value=5)
distance_airport = st.number_input("Distance from Airport (in km):", min_value=0.0, value=20.0)

if st.button("Predict House Price"):
    input_data = np.array([[bedrooms, bathrooms, living_area, lot_area, floors, grade,
                            house_area, basement_area, built_year, living_area_renov,
                            lot_area_renov, schools_nearby, distance_airport]])
    predicted_price = model.predict(input_data)
    st.success(f"The predicted house price is: ₹{predicted_price[0]:,.2f}")


# Predict button
# if st.button("Predict House Price"):
#     # Prepare the input data array
#     input_data = np.array([[bedrooms, bathrooms, living_area, lot_area, floors, grade,
#                             house_area, basement_area, built_year, living_area_renov,
#                             lot_area_renov, schools_nearby, distance_airport]])

#     # Make prediction
#     predicted_price = model.predict(input_data)

#     # Display the predicted price
#     st.success(f"The predicted house price is: ₹{predicted_price[0]:,.2f}")