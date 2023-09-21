import streamlit as st
import requests

# Streamlit app title and header
st.title("Weather Dashboard")

# API keys for OpenWeatherMap and Weatherstack
openweathermap_api_key = 'eddfcb2e5368ad6034a63479dd015c5b'
weatherstack_api_key = '4e1edd2c575541dddfdfbf81419562eb'

# City for weather information
city = st.text_input("Enter a city name:", "New York")

if st.button("Get Weather"):
    # API endpoints
    openweathermap_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}'
    weatherstack_url = f'http://api.weatherstack.com/current?access_key={weatherstack_api_key}&query={city}'

    # Make API requests
    try:
        openweathermap_response = requests.get(openweathermap_url)
        weatherstack_response = requests.get(weatherstack_url)
        openweathermap_data = openweathermap_response.json()
        weatherstack_data = weatherstack_response.json()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        openweathermap_data = {}
        weatherstack_data = {}

    # Extract relevant weather information
    if 'main' in openweathermap_data:
        temperature = openweathermap_data['main']['temp']
    else:
        temperature = "N/A"

    if 'current' in weatherstack_data:
        weather_description = weatherstack_data['current']['weather_descriptions'][0]
    else:
        weather_description = "N/A"

    # Display weather information
    st.write(f"Weather in {city}:")
    st.write(f"Temperature: {temperature}°C")
    st.write(f"Description: {weather_description}")
