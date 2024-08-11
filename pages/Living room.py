from utils import api_call, store_tokens, write_visitor_info
import streamlit as st

room = "Living"
st.sidebar.markdown("## Living room 📺")
st.subheader("You are in the room: Living room 📺")

sheet = api_call()

form = st.form(key='my_form')
token = form.number_input(label='Enter visitor token', min_value=int(1), max_value=int(500))
submitted = form.form_submit_button(label='Submit')
if submitted:
    store_tokens(token, room, sheet)

if st.button('Show all submitted tokens'):
    write_visitor_info(room, sheet)