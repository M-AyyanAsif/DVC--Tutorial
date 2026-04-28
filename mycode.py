import pandas as pd
import os

data =  {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [22,33,44],
    'City': ['Los Angleos', 'California', 'Newyork']
}
df = pd.DataFrame(data)

new_row_loc = {'Name':'AGF1', 'Age':30, 'City': 'Texas'}
df.loc[len(df.index)] = new_row_loc

new_row_loc2 = {'Name':'AGF2', 'Age':32, 'City': 'Texas'}
df.loc[len(df.index)] = new_row_loc2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data,csv')

df.to_csv(file_path, index=False)

print(f"CSV File saved to {file_path}")


