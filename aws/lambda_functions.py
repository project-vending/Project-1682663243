python
import boto3
import pandas as pd

def get_sensor_data():
    """Fetches sensor data from AWS S3 bucket"""
    
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket='your-bucket-name', Key='sensor_data.csv')
    
    data = response['Body'].read().decode('utf-8')  # read the data from S3 object
    df = pd.read_csv(pd.compat.StringIO(data))  # convert the data to pandas DataFrame
    
    return df
