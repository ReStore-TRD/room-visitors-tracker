import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Public Google Sheet but the link is kept in secret
url = st.secrets["spreadsheet"]
conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, worksheet="0")
# With the 'worksheet' param, you can specify the id of a GS (everything after gid= in the url)
# Tables: worksheet="196616450"
st.dataframe(data)

# Let's try to add a row to the data