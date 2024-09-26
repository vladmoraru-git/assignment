import pandas as pd
import re

input_csv = 'website_dataset.csv'
output_txt = 'website_clean.txt'

def clean_value(value):
    if pd.isna(value):
        return None

    cleaned_value = re.sub(r'[^\w\s,]', '', str(value)).strip()

    return cleaned_value

try:
    df = pd.read_csv(input_csv, on_bad_lines='skip')
except pd.errors.ParserError as e:
    exit()

with open(output_txt, 'w') as file:
    for index, row in df.iterrows():
        formatted_values = []
        for column, value in row.items():
            cleaned_value = clean_value(value)  # Clean the value
            if pd.notna(cleaned_value):
                formatted_value = cleaned_value.replace("'", "''")
                formatted_values.append(f"'{formatted_value}'")
            else:
                formatted_values.append('NULL')

        formatted_row = ', '.join(formatted_values)
        formatted_row = f'({formatted_row}),'

        file.write(formatted_row + '\n')
