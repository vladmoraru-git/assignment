import pandas as pd
import re

input_csv = 'facebook_dataset.csv'
output_txt = 'facebook_clean3.txt'


def normalize_phone(phone):
    if pd.isna(phone):
        return None
    phone = re.sub(r'[^\d+]', '', str(phone))
    return phone

def normalize_company_name(name):
    if pd.isna(name):
        return None
    name = str(name).lower().strip()
    name = re.sub(r'[^\w\s]', '', name)
    return name

def normalize_category(category):
    if pd.isna(category):
        return None
    category = str(category).lower().strip()
    return category


def normalize_address(address):
    if pd.isna(address):
        return None
    address = str(address).lower().strip()
    address = re.sub(r'[^\w\s,]', '', address)
    return address


def clean_value(column, value):
    if 'phone' in column.lower():
        return normalize_phone(value)
    elif 'name' in column.lower():
        return normalize_company_name(value)
    elif 'categ' in column.lower():
        return normalize_category(value)
    elif 'address' in column.lower():
        return normalize_address(value)
    else:
        if pd.isna(value):
            return None
        return str(value).lower().strip()

try:
    df = pd.read_csv(input_csv, on_bad_lines='skip')
except pd.errors.ParserError as e:
    print(f"Error parsing CSV: {e}")
    exit()

with open(output_txt, 'w') as file:
    for index, row in df.iterrows():
        formatted_values = []
        for column, value in row.items():
            cleaned_value = clean_value(column, value)

            if pd.notna(cleaned_value):
                formatted_value = cleaned_value.replace("'", "''")
                formatted_values.append(f"'{formatted_value}'")
            else:
                formatted_values.append('NULL')

        formatted_row = ', '.join(formatted_values)
        formatted_row = f'({formatted_row}),'

        file.write(formatted_row + '\n')
