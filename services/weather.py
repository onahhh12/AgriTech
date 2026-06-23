import requests
import streamlit as st

@st.cache_data(ttl=600)
def get_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-25.8655"
        "&longitude=25.6436"
        "&current=temperature_2m,relative_humidity_2m,rain,wind_speed_10m"
    )

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        return {
            "location": "North West, South Africa",
            "temperature": data["current"]["temperature_2m"],
            "humidity": data["current"]["relative_humidity_2m"],
            "rain": data["current"]["rain"],
            "wind_speed": data["current"]["wind_speed_10m"],
            "last_updated": data["current"]["time"]
        }

    except requests.exceptions.RequestException:
        return None