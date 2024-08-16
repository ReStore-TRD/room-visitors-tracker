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
st.write('During the unlimited slot, you do not need to record the token anymore — instead, just click on the button "Add unlimited slot visitor" to record a visit to your room.')
st.write("Have a fun opening!")

