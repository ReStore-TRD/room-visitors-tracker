import streamlit as st


st.sidebar.markdown("## Home 🏠")

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

st.write("Dear volunteer, thank you for your help with visitor tracking!")
st.write("Choose a room where you want to track visitors from the bar on the left.")
st.write("You will need to submit the token number every time a visitor enters your room.")
st.write("Before the opening, please navigate to the upper right corner, click on the three dots, and select 'Clear cache'. This only needs to be done once, before you record any visitors.")