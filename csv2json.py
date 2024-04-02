import os
import pandas as pd
import json
import html
from bs4 import BeautifulSoup

# Get name of current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Edit this to your excel file name
csv_filename = 'yourExcelFileName.csv'

# Excel file path
csv_file_path = os.path.join(current_dir, csv_filename)

# Load csv file into panda
df = pd.read_csv(csv_file_path)

# Choose the columns you wish to export, you may add more
selected_columns = ['columnName-1', 'columnName-2', 'columnName-3']

# Filter DataFrame to keep only selected columns
df_selected = df[selected_columns]

# The below code is situational, when you have columns that contain html tags, you may uncommented the code below to parse text data properly

# def clean_html(raw_html):
#     clean_text = BeautifulSoup(raw_html, 'html.parser').get_text()
#     return html.unescape(clean_text)
# df_selected.loc[:, 'columnName'] = df_selected['columnName'].apply(clean_html)

# Convert DataFrame to list of dictionaries (JSON objects)
json_data = df_selected.to_dict(orient='records')

# Write JSON data to a file, you may edit file name and change indentation
output_file = 'speakers.json'
output_file_path = os.path.join(current_dir, output_file)
with open(output_file_path, 'w') as f:
    json.dump(json_data, f, indent=2)

print(f'Data from Excel file has been printed to {output_file_path}')
