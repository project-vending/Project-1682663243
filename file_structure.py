 
import os

root_dir = os.getcwd()  # get current working directory

# create necessary directories
data_dir = os.path.join(root_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

aws_dir = os.path.join(root_dir, 'aws')
os.makedirs(aws_dir, exist_ok=True)

streamlit_dir = os.path.join(root_dir, 'streamlit')
os.makedirs(streamlit_dir, exist_ok=True)

# create empty files in each directory
data_file = os.path.join(data_dir, 'sensor_data.csv')
with open(data_file, 'w') as f:
    f.write("")

aws_file = os.path.join(aws_dir, 'lambda_functions.py')
with open(aws_file, 'w') as f:
    f.write("")

streamlit_file = os.path.join(streamlit_dir, 'dashboard.py')
with open(streamlit_file, 'w') as f:
    f.write("")
