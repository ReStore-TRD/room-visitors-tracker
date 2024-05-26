import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1uV84YaB9HQr2fKR_J8Onaq49wUEWaaYTjuFFnoy30eo/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0,1])
st.dataframe(data)