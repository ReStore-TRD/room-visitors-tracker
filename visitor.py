
import streamlit as st


def my_function(input_value):
    result = input_value
    return result
    

def main():

    def my_function(input_value):
        result = input_value
        return result

    # Create a Streamlit sidebar for the navbar
    st.sidebar.title("Navigation")

    # Add links to different sections of the app
    page = st.sidebar.radio("Go to", ["Home", "Kitchen", "Table"])

    # Display different content based on the selected page
    if page == "Home":
        st.title("Home Page")
        st.write("Hi Volunteer!")

    elif page == "Kitchen":
        st.title("About Page")
        st.write("This is the About Page.")

    elif page == "Table":
        st.title("Table room")
        input_value = st.text_input('Enter token number:')
        input_value2 = st.text_input('Which Room:')
        if st.button('Run'):
            number = my_function(input_value)
            room = my_function(input_value2)
            st.write('Attended once', number)
            st.write("You can contact us at contact@example.com")

        

   

if __name__ == "__main__":
    main()


