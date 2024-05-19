import streamlit as st

# Define the function to perform the desired task
def my_function(input_value):
    result = input_value
    return result

# Create the Streamlit UI components
st.title('Kitchen Room')
input_value = st.text_input('Please enter token number:')

if st.button('Run'):
    number = my_function(input_value)
    st.write('Attended once', number)
