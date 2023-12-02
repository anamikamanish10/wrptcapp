# Import necessary library
import streamlit as st

# Set the title of the dashboard
st.title('Moderate Streamlit App')

# Add a sidebar for user input
st.sidebar.header('User Input')

# Allow the user to enter a number
user_input = st.sidebar.number_input('Enter a number:', value=5.0)

# Perform a simple calculation
result = user_input * 2

# Display the result
st.write(f'Twice of {user_input} is: {result}')
