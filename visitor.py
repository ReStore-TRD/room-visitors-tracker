import streamlit as st


def my_function(input_value):
    result = input_value
    return result
    

def main():
    # Create a Streamlit sidebar for the navbar
    st.sidebar.title("Navigation")

    # Add links to different sections of the app
    page = st.sidebar.radio("Go to", ["Home", "Kitchen", "Table"])

    # Display different content based on the selected page
    if page == "Home":
        st.title("Home Page")
        st.write("Hi Volunteer!")
        st.write("You can contact us at info@restore-trd.no")

    elif page == "Kitchen":
        st.title("Kitchen room")
        input_value = st.text_input('Enter token number:')
        if st.button('Run'):
            number = my_function(input_value)
            st.write('Attended once', number)

    elif page == "Table":
        st.title("Table room")
        input_value = st.text_input('Enter token number:')
        if st.button('Run'):
            number = my_function(input_value)
            st.write('Attended once', number)

   

if __name__ == "__main__":
    main()




## zero for unlimited