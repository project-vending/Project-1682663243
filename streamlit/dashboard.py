python
import streamlit as st
import boto3
import pandas as pd
import plotly.express as px

# Initialize AWS resources
s3 = boto3.resource('s3')
bucket_name = 'your_bucket_name'
bucket = s3.Bucket(bucket_name)

# Define file paths and column names
file_path = 'sensor_data.csv'
date_colname = 'date'
sensor_colname = 'sensor'
value_colname = 'value'

# Load data from S3 bucket
def load_data():
    obj = bucket.Object(file_path)
    body = obj.get()['Body'].read().decode('utf-8')
    data = pd.read_csv(StringIO(body), parse_dates=[date_colname])
    return data

# Define Streamlit app layout
st.title('Real-time Sensor Data Monitoring Dashboard')

st.sidebar.header('Filters')
selected_sensor = st.sidebar.selectbox('Select Sensor', ['sensor 1', 'sensor 2', 'sensor 3'])

# Load and filter data
data = load_data()
filtered_data = data.loc[data[sensor_colname] == selected_sensor]

# Create Plotly chart
fig = px.line(filtered_data, x=date_colname, y=value_colname)

# Display chart
st.plotly_chart(fig)
