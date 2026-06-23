import streamlit as st
from pages.field_overview import field_overview_page
from services.weather import get_weather

st.set_page_config(
    page_title="Farm Command Centre",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align: center;'>Farm Command Centre</h1>",
    unsafe_allow_html=True
)

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
    field_overview_page()

elif page == "Crop Health":
    st.markdown("<h4 style='text-align: center'>Crop Health Monitoring and Disease Detection</h4>", unsafe_allow_html=True)