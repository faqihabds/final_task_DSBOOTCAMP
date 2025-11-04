import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Weather Prediction',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :earth_americas: Weather Prediction

'''

# Add some spacing
''
''

# Input pengguna
MinTemp = st.number_input("Min Temperature (°C)")
MaxTemp = st.number_input("Max Temperature (°C)")
Rainfall = st.number_input("Rainfall (mm)")
Humidity3pm = st.number_input("Humidity at 3pm (%)")
Pressure3pm = st.number_input("Pressure at 3pm (hPa)")
Temp3pm = st.number_input("Temperature at 3pm (°C)")
WindGustSpeed = st.number_input("Wind Gust Speed (km/h)")
WindSpeed3pm = st.number_input("Wind Speed at 3pm (km/h)")

# Fitur baru dalam bentuk DataFrame
data = pd.DataFrame({
    'MinTemp': [MinTemp],
    'MaxTemp': [MaxTemp],
    'Rainfall': [Rainfall],
    'Humidity3pm': [Humidity3pm],
    'Pressure3pm': [Pressure3pm],
    'Temp3pm': [Temp3pm],
    'WindGustSpeed': [WindGustSpeed],
    'WindSpeed3pm': [WindSpeed3pm]
})


# Prediksi
if st.button("Prediksi"):
    prediction = model.predict(data_scaled)[0]
    if prediction == 1:
        st.success("Besok kemungkinan *HUJAN ☔*")
    else:
        st.info("Besok kemungkinan *TIDAK HUJAN 🌤*")
