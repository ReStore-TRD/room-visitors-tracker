import gspread  # Python API for Google Sheets, used for private connection
import streamlit as st
import datetime

@st.cache_resource(show_spinner="Connecting to Google Spreadsheets...")
def api_call():
    gc_credentials = st.secrets["gs_credentials"]['streamlit_visitor_tracking_creds']
    # Credentials from secrets.toml
    creds_dict = {key:value for key, value in gc_credentials.items()}
    # Obtaining credentials with spread
    gc = gspread.service_account_from_dict(creds_dict) # from secrets file
    # Opening a GS by name, including worksheet name 
    return gc.open('Test_tracking_streamlit').worksheet('Books')

sheet = api_call()

st.subheader("You are in the room: Books 📖, Bedframes 	🛏️, Toys 🧸")

def store_tokens(token):
    if token not in st.session_state:
        time_stamp = str(datetime.datetime.now())[:-7]
        st.session_state[token] = time_stamp
        sheet.append_row([token, time_stamp])
        message = ":green[Token #" + str(token) + " has been submitted successfully! 🎉]"
        st.write(message)
    else: 
        st.write(":red[This visitor token has already been submitted. ❌]")

form = st.form(key='my_form')
token = form.number_input(label='Enter visitor token', min_value=int(1), max_value=int(300))
submitted = form.form_submit_button(label='Submit')
if submitted:
    store_tokens(token)

if st.button('Show all submitted tokens'):
    st.write("#\u3000Time")
    for k, v in st.session_state.items():
        if "FormSubmitter" not in k:
            st.write(k, "\u3000",  v)
