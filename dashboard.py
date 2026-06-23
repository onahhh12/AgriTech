import streamlit as st
import requests
import pandas as pd


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
    
    except requests.exceptions.RequestException as e:
        st.error(f"Weather API Error: {e}")
        return None


st.set_page_config(
    page_title="Farm Command Centre",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align: center;'>Farm Command Centre</h1>",
    unsafe_allow_html=True
)

#Sidebar
page = st.sidebar.radio("Navigation Hub", [
    "Field Overview",
    "Crop Health",
    "Irrigation Management",
    "Pest and Disease Control",
    "Livestock Monitoring",
    "Harvest Planning",
    "Market Analysis",
    "Virtual Advisor",
])

if page == "Field Overview":
    st.markdown("<h4 style = 'text-align: center'>Field Data and Water Predictor</h4>", unsafe_allow_html=True)

    weather = get_weather()

    if weather is None:
        st.warning("Live weather is currently unavailable. Showing field data only.")
    else:
        st.info(f"📍{weather['location']}")
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
        "Field": [ "Field A", "Field B", "Field C", "Field D"],
        "Crop": ["Corn", "Sunflower", "Corn", "Sunflower"],
        "Growth Stage": ["Vegetative", "Flowering", "Vegetative", "Emergence"],
        "Soil Moisture (%)": [45, 38, 52, 41],
        "Size (ha)": [25, 18, 30, 22],
        "Status" : ["Healthy", "Needs Attention", "Healthy", "Needs Attention"]
    }

    df = pd.DataFrame(field_data)

    st.markdown("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total fields", "4")
    with col2:
        st.metric("Total Area", "95 ha")
    with col3:
        st.metric("Average Soil Moisture", "44%") 

    st.markdown("")
    st.subheader("Field Condition Summary")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Soil Moisture Trend")

    moisture_trend = pd.DataFrame({
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Field A": [45, 47, 50, 48, 46],
        "Field B": [38, 40, 42, 39, 37],
        "Field C": [52, 54, 55, 53, 51],
        "Field D": [41, 43, 44, 42, 40]
    })

    st.line_chart(moisture_trend.set_index("Day"))


elif page == "Crop Health":
    st.markdown("<h4 style = 'text-align: center'>Crop Health Monitoring and Disease Detection</h4>", unsafe_allow_html=True)

elif page == "Irrigation Management":
    st.markdown("<h4 style = 'text-align: center'>Irrigation Scheduling and Water Usage Optimization</h4>", unsafe_allow_html=True)

elif page == "Pest and Disease Control":
    st.markdown("<h4 style = 'text-align: center'>Pest and Disease Identification and Management</h4>", unsafe_allow_html=True)

elif page == "Livestock Monitoring":
    st.markdown("<h4 style = 'text-align: center'>Livestock Health and Behavior Monitoring</h4>", unsafe_allow_html=True)

elif page == "Harvest Planning":
    st.markdown("<h4 style = 'text-align: center'>Harvest Planning and Yield Prediction</h4>", unsafe_allow_html=True)

elif page == "Market Analysis":
    st.markdown("<h4 style = 'text-align: center'>Market Trends and Price Forecasting</h4>", unsafe_allow_html=True)

elif page == "Virtual Advisor":
    st.markdown("<h4 style = 'text-align: center'>Virtual Agricultural Advisor and Decision Support System</h4>", unsafe_allow_html=True)

