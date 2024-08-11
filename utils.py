import streamlit as st
import gspread  # Python API for Google Sheets, can be used for private connections
import datetime
import pytz

# Main functions
@st.cache_resource(show_spinner="Connecting to Google Spreadsheets...")
def api_call():
    gc_credentials = st.secrets["gs_credentials"]['streamlit_visitor_tracking_creds']
    # Credentials from secrets.toml
    creds_dict = {key:value for key, value in gc_credentials.items()}
    # Obtaining Google credentials with spread
    gc = gspread.service_account_from_dict(creds_dict) # from secrets file
    # Opening a GS by name, including worksheet name 
    return gc.open("Test_tracking_streamlit").worksheet("All_rooms")


def store_tokens(token, room, sheet):
    timezone = pytz.timezone('Europe/Oslo')
    list_of_lists = sheet.get_all_values() # row-by-row gs
    # Make token-keys from spreadsheet
    registered_token_keys = [str(lrow[2]) + "-" + str(lrow[0]) for lrow in list_of_lists] 
    token_key = room + "-" + str(token) # The current key combines visitor token and room so that 
    # the same token could be visiting multiple rooms in one session state
    if token_key not in registered_token_keys:
        ts = str(datetime.datetime.now(tz = timezone)) # format: 2024-08-09 20:32:33.294137+02:00
        time_stamp = ts.split(".")[0] # remove everything after period
        st.session_state[token_key] = time_stamp
        sheet.append_row([token, time_stamp, room])
        message = ":green[Token #" + str(token) + " has been submitted successfully! 🎉]"
        st.write(message)
    else: 
        st.write(":red[Token #" + str(token) + " has already been submitted. ❌]")


def write_visitor_info(room, sheet):
    list_of_lists = sheet.get_all_values() # row-by-row gs
    registered_token_keys = [str(lrow[2]) + "-" + str(lrow[0]) for lrow in list_of_lists]
    timestamps = [lrow[1] for lrow in list_of_lists]
    tk_dict = dict(zip(registered_token_keys, timestamps))
    # st.write(tk_dict)
    st.write("#\u3000Time")
    for k, v in tk_dict.items():
        if room in k: # Showing visitors admitted to this particular room
            tkn = k.split("-") # Splitting token_key, showing just the token
            st.write(tkn[1], "\u3000",  v)