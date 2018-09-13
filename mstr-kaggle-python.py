# Important prerequisites : when using this script, you need to
# 1. Install the python package mstrio-py
# 2. Enable internet (Kaggle beta feature)

# mstr initialization
username = 'my_username' #changeme
password = 'my_password' #changeme
base_url = 'https://yourserver.com/MicroStrategyLibrary/api' #changeme
project_name = 'MicroStrategy Tutorial'

import os
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from mstrio import microstrategy # MicroStrategy library for sending data to in-memory cubes

conn = microstrategy.Connection(base_url=base_url, username=username, password=password, project_name=project_name)
conn.connect()

# Loop through all datasets added to the Kaggle Kernel
for dirname, dirnames, filenames in os.walk('../input'):
    # loop through all files included in the dataset
    for filename in filenames:
        print(os.path.join(dirname, filename))
        dataset_name = filename.replace('.csv', '')
        table_name = dataset_name
        newDatasetId, newTableId = conn.create_dataset(data_frame=pd.read_csv(os.path.join(dirname, filename)), dataset_name=dataset_name, table_name=table_name)
