import pandas as pd

def load_data(file_path):
    """
    Load the Excel file into a DataFrame.
    
    Parameters:
    file_path (str): The path to the Excel file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    return pd.read_excel(file_path)

def extract_names(full_name):
    """
    Extract the first and last names from the full name.
    
    Parameters:
    full_name (str): The full name in "Last, First" or "First Last" format.
    
    Returns:
    tuple: A tuple containing (first_name, last_name).
    """
    parts = full_name.split(", ")
    if len(parts) > 1:
        last_name, first_name = parts[0].lower(), parts[1].lower()
    else:
        name_parts = full_name.split()
        first_name = name_parts[0].lower()
        last_name = name_parts[1].lower() if len(name_parts) > 1 else ""
    return first_name, last_name

def generate_unique_email(first_name, last_name, used_emails, domain="gmail.com"):
    """
    Generate a unique email address using the first initial of the first name and the full last name.
    
    Parameters:
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.
    used_emails (set): A set of already used email addresses to ensure uniqueness.
    domain (str): The email domain (default is "gmail.com").
    
    Returns:
    str: The unique email address.
    """
    base_email = f"{first_name[0]}{last_name}@{domain}"
    unique_email = base_email
    i = 1
    while unique_email in used_emails:
        unique_email = f"{first_name[0]}{last_name}{i}@{domain}"
        i += 1
    used_emails.add(unique_email)
    return unique_email

def main(file_path):
    # Load the data
    df = load_data(file_path)
    print("Data loaded successfully.")
    print(df.head())
    
    # Initialize list for emails and set for used emails
    email_addresses = []
    used_emails = set()
    
    # Generate unique email addresses for each student
    for index, row in df.iterrows():
        full_name = row['Student Name']
        first_name, last_name = extract_names(full_name)
        unique_email = generate_unique_email(first_name, last_name, used_emails)
        email_addresses.append(unique_email)
    
    # Add the generated emails to the DataFrame
    df['Email'] = email_addresses
    
    # Display the generated email addresses
    for name, email in zip(df['Student Name'], email_addresses):
        print(f"Student Name: {name} - Email address: {email}")
    
    # Optionally, save the updated DataFrame to a new Excel file
    output_file = "Updated_Test_Files.xlsx"
    df.to_excel(output_file, index=False)
    print(f"Updated DataFrame saved to {output_file}")

if __name__ == "__main__":
    file_path = 'Test Files.xlsx'
    main(file_path)
