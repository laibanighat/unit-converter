import streamlit as st

st.title("🌍Unit Converter App")
st.markdown("### Converts Length, Weight And Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted resultin real-time")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
                return value / 0.621371

        elif category == "Weight":
            if unit == "Kilometers to pounds":
                return value * 2.20462
        elif unit == "Pounds to Kilometers":
                return value / 2.20462
        elif category == "Time": 
            if unit == "Seconds to minutes":
                return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
             return value /24
        elif unit == "Days to hours":
             return value *24
        
if category == "Length":
     unit = st.selectbox("📏 Select Conversaton", ["Miles to kilometers", "Kilometers to miles"])
elif category == "Weight":
     unit = st.selectbox("⚖ Select Conversation", ["Kilograms to pounds", "Pounds to Kilogram"])
elif category == "Time":
     unit = st.selectbox("⌚ Select Conversation", ["Days to hours", "Hours to days", "Hours to minutes", "Minutes to hours", "Minutes to seconds", "Seconds to minutes"])   

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
     result = convert_units(category, value, unit)
     st.success(f"The result is {result:.2f}")



