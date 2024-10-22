import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(
    page_title="chicken Cross Breeding Model",
    page_icon="🐔",
    layout= "wide"
)
st.title("Chicken Cross breeding growth model")

sh= st.selectbox(
    label="Which Diet",
    options=["1","2","3","4"],
    key="Selectbox"

)
sh1=st.select_slider(
    label= "Curent Weight Of Chicken In Grams",
    options=range(8800)
)
sh2=st.date_input(
    label="When Was the chicken Born"
)

st_lottie("https://lottie.host/6a54bd46-8d00-4cbd-ae35-b3413a016225/LzWU4BLb7j.json")

