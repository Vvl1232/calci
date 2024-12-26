import streamlit as st

st.title("🧮 Calculator & Unit Converter 🌡️")
st.write("This is a simple app that combines a calculator and a unit converter")

# Initialize session state for memory
if "result" not in st.session_state:
    st.session_state.result = None

# Calculator
def cal():
    st.header("🧮 Calculator")
    n1 = st.number_input("Enter first number:", step=1, key="num1")
    n2 = st.number_input("Enter second number:", step=1, key="num2")
    choice = st.selectbox("Enter operation:", ("Addition (+) ➕", "Subtraction (-) ➖", "Multiplication (x) ✖️", "Division (/) ➗"), key="operation")

    if st.button("Calculate"):
        if choice == "Addition (+) ➕":
            result = add(n1, n2)
            st.info(f"Addition: {n1} + {n2} = {result}")
        elif choice == "Subtraction (-) ➖":
            result = sub(n1, n2)
            st.info(f"Subtraction: {n1} - {n2} = {result}")
        elif choice == "Multiplication (x) ✖️":
            result = mul(n1, n2)
            st.info(f"Multiplication: {n1} x {n2} = {result}")
        elif choice == "Division (/) ➗":
            if n2 != 0:
                result = div(n1, n2)
                st.info(f"Division: {n1} / {n2} = {result}")
            else:
                st.write("Error: Division by zero is not allowed.")
        else:
            st.write("Invalid operation")
        
        st.session_state.result = result
        st.write("Thank you for using the calculator! 🎉")

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 // n2

# Unit Converter
def unit_converter():
    st.header("🌡️ Unit Converter")
    unit_type = st.selectbox("Select unit type:", ("Length 📏", "Weight ⚖️", "Temperature 🌡️"), key="unit_type")
    
    if unit_type == "Length 📏":
        length_units = ["Meters", "Kilometers", "Feet", "Miles"]
        from_unit = st.selectbox("From:", length_units, key="from_length")
        to_unit = st.selectbox("To:", length_units, key="to_length")
        value = st.number_input("Enter value:", step=1, key="length_value")
        
        if st.button("Convert"):
            result = convert_length(value, from_unit, to_unit)
            st.info(f"{value} {from_unit} = {result} {to_unit}")

    elif unit_type == "Weight ⚖️":
        weight_units = ["Grams", "Kilograms", "Pounds", "Ounces"]
        from_unit = st.selectbox("From:", weight_units, key="from_weight")
        to_unit = st.selectbox("To:", weight_units, key="to_weight")
        value = st.number_input("Enter value:", step=1, key="weight_value")
        
        if st.button("Convert"):
            result = convert_weight(value, from_unit, to_unit)
            st.info(f"{value} {from_unit} = {result} {to_unit}")

    elif unit_type == "Temperature 🌡️":
        temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
        from_unit = st.selectbox("From:", temp_units, key="from_temp")
        to_unit = st.selectbox("To:", temp_units, key="to_temp")
        value = st.number_input("Enter value:", step=1, key="temp_value")
        
        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.info(f"{value} {from_unit} = {result} {to_unit}")

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1.0, "Kilometers": 1000.0, "Feet": 0.3048, "Miles": 1609.34
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Grams": 1.0, "Kilograms": 1000.0, "Pounds": 453.592, "Ounces": 28.3495
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

mode = st.selectbox("Select mode:", ("Choose...", "Calculator 🧮", "Unit Converter 🌡️"))
if mode == "Choose...":
    st.warning("Please select a mode")
elif mode == "Calculator 🧮":
    cal()
else:
    unit_converter()
