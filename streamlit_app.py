# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Create a sample dataframe
data = {
    'X': np.random.rand(100),
    'Y': np.random.rand(100),
}

df = pd.DataFrame(data)

# Set the title of the dashboard
st.title('Simple Streamlit App')

# Display the raw data
st.write('### Raw Data')
st.write(df)

# Create a scatter plot using Plotly Express
scatter_plot = px.scatter(df, x='X', y='Y', title='Scatter Plot')

# Display the scatter plot
st.plotly_chart(scatter_plot)
