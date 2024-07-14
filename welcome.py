import streamlit as st
from PIL import Image

img = Image.open("images/ReStore_logo_pink.png")
resized_img = img.resize((50, 650))
#st.sidebar.image(img)
st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://raw.githubusercontent.com/ReStore-TRD/room-visitors-tracker/main/images/ReStore_logo_resized.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
)

st.header("Welcome to ReStore Opening!")

st.write("Dear volunteer, thank you for your help at the opening!")
st.write("Choose a room where you want to track visitors from the bar on the left.")