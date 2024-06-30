import gspread  # Python API for Google Sheets, used for private connection
import streamlit as st
import datetime

# Credentials from secrets.toml
gc_credentials = st.secrets["gs_credentials"]['streamlit_visitor_tracking_creds']
creds_dict = {key:value for key, value in gc_credentials.items()}

# Obtaining credentials with spread
gc = gspread.service_account_from_dict(creds_dict) # from secrets file
#gc = gspread.service_account(filename="test-tracking-streamlit-dae6d2892d19.json") # from local json file
# Opening a GS by name, including worksheet name 
sheet = gc.open('Test_tracking_streamlit').worksheet('Kitchen')

st.subheader("Visitor tracking functions")

# Streamlit app functions
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

visitor_data = {}
    # Adding app data row-by-row to GS
for k, v in st.session_state.items():
    if "FormSubmitter" not in k:
        if k not in visitor_data.keys():
            visitor_data[k] = v
                

for k, v in visitor_data.items():
    sheet.append_row([k,v])