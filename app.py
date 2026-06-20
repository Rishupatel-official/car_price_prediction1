import streamlit as st
import joblib

model = joblib.load("model.pkl")

fuel_encoder = joblib.load("fuel.pkl")
door_encoder = joblib.load("door.pkl")
body_encoder = joblib.load("body.pkl")

st.title("Car Price Prediction")

st.write("Enter the car details below")

fuel = st.selectbox("Fuel Type", ["gas", "diesel"])

door = st.selectbox("Door Number", ["two", "four"])

body = st.selectbox(
    "Car Body",
    ["sedan", "hatchback", "wagon", "convertible", "hardtop"]
)

wheelbase = st.number_input("Wheelbase", min_value=0.0)

horsepower = st.number_input("Horsepower", min_value=0)

if st.button("Predict Price"):

    fuel_value = fuel_encoder.transform([fuel])[0]
    door_value = door_encoder.transform([door])[0]
    body_value = body_encoder.transform([body])[0]

    data = [[
        fuel_value,
        door_value,
        body_value,
        wheelbase,
        horsepower
    ]]

    price = model.predict(data)[0]

    st.success(f"Predicted Price: ₹ {price:,.0f}")
