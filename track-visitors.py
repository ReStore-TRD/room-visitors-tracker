import streamlit as st
import datetime
from streamlit_gsheets import GSheetsConnection

# Public Google Sheet but the link is kept in secret
url = st.secrets["spreadsheet"]
conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, worksheet="0")
# With the 'worksheet' param, you can specify the id of a GS (everything after gid= in the url)
# Tables: worksheet="196616450"
st.subheader("Public connection can be used to display data from a GS, but not to update/write it")
st.dataframe(data)

st.subheader("Visitor tracking functions")

def store_tokens():
    if token not in st.session_state:
        st.session_state[token] = str(datetime.datetime.now())[:-7]
    else: 
        st.text("This visitor token has already been submitted.")

form = st.form(key='my_form')
token = form.number_input(label='Enter visitor token', min_value=int(1), max_value=int(300))
submitted = form.form_submit_button(label='Submit')
if submitted:
    store_tokens()

st.markdown(f"### Visitor tokens submitted so far: ")
for k, v in st.session_state.items():
    if "FormSubmitter" not in k:
        st.write(k, ": ",  v)

# Let's try to add a row to the data