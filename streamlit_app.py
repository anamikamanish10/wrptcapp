# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title of the dashboard
st.title('Advanced Streamlit App')

# Add a file uploader to allow the user to upload a CSV file
uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

# If a file is uploaded, load the data into a DataFrame
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Display the raw data
    st.write('### Raw Data')
    st.write(df)

    # Allow the user to select columns for plotting
    selected_columns = st.multiselect('Select Columns for Plotting', df.columns)

    # Plot the selected columns using Plotly Express
    if selected_columns:
        fig = px.line(df, x='Date', y=selected_columns, title='Customizable Plot')
        st.plotly_chart(fig)
else:
    st.write('Upload a CSV file to get started.')
