import streamlit as st
st.title('DEMO APP FOR STREAMLIT')
st.write('Hello, Streamlit!')
user_input = st.text_input("Enter something:")

# Display the output if user input is provided
if user_input:
    st.write("You entered:", user_input)
