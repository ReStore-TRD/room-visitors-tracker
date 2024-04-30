import streamlit as st

# Define the function to perform the desired task
def my_function(input_value):
    result = input_value
    return result

# Create the Streamlit UI components
st.title('ReStore Opening')
input_value = st.text_input('Enter token number:')
input_value2 = st.text_input('Which Room:')

if st.button('Run'):
    number = my_function(input_value)
    room = my_function(input_value2)
    st.write('Attended once', number)
