
import streamlit as st
import pandas as pd
from services.weather import get_weather


def field_overview_page():
    st.markdown(
        "<h4 style='text-align: center'>Field Data and Water Predictor</h4>",
        unsafe_allow_html=True
    )

    weather = get_weather()

    if weather is None:
        st.warning("Live weather is currently unavailable. Showing field data only.")
    else:
        st.info(f"📍 {weather['location']}")
        st.caption(f"Last Updated: {weather['last_updated']}")
        st.success("🟢 Live Weather Feed Active")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("🌡 Temperature", f"{weather['temperature']}°C")
        with col2:
            st.metric("💧 Humidity", f"{weather['humidity']}%")
        with col3:
            st.metric("🌧 Rainfall", f"{weather['rain']} mm")
        with col4:
            st.metric("🌬 Wind Speed", f"{weather['wind_speed']} km/h")

    field_data = {
        "Field": ["Field A", "Field B", "Field C", "Field D"],
        "Crop": ["Corn", "Sunflower", "Corn", "Sunflower"],
        "Growth Stage": ["Vegetative", "Flowering", "Vegetative", "Emergence"],
        "Soil Moisture (%)": [45, 38, 52, 41],
        "Size (ha)": [25, 18, 30, 22],
        "Status": ["Healthy", "Needs Attention", "Healthy", "Needs Attention"]
    }

    df = pd.DataFrame(field_data)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Fields", len(df))

    with col2: 
        st.metric("Total Area", f"{df['Size (ha)'].sum()} ha")

    with col3:
        st.metric("Average Soil Moisture", f"{df['Soil Moisture (%)'].mean():.1f}%")

    st.markdown(" ")
    st.subheader("Field Condition Summary")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Moisture Trend")

    moisture_trend = pd.DataFrame({
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Field A": [45, 47, 50, 48, 46],
        "Field B": [38, 40, 42, 39, 37],
        "Field C": [52, 54, 55, 53, 51],
        "Field D": [41, 43, 44, 42, 40]
    })

    st.line_chart(moisture_trend.set_index("Day"))
    