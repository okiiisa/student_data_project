import pandas as pd

def load_data(file_path):
    #Load the Excel file into a DataFrame.
    
    return pd.read_excel(file_path)

def extract_names(full_name):
    #Extract the first and last names from the full name.
    
    parts = full_name.split(", ")
    if len(parts) > 1:
        last_name, first_name = parts[0].lower(), parts[1].lower()
    else:
        name_parts = full_name.split()
        first_name = name_parts[0].lower()
        last_name = name_parts[1].lower() if len(name_parts) > 1 else ""
    return first_name, last_name

def generate_unique_email(first_name, last_name, used_emails, domain="gmail.com"):
    #Generate a unique email address using the first initial of the first name and the full last name.
    
    base_email = f"{first_name[0]}{last_name}@{domain}"
    unique_email = base_email
    i = 1
    while unique_email in used_emails:
        unique_email = f"{first_name[0]}{last_name}{i}@{domain}"
        i += 1
    used_emails.add(unique_email)
    return unique_email
