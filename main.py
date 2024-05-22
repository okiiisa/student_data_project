from functions import load_data, extract_names, generate_unique_email
from constaints import DEFAULT_DOMAIN

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
        unique_email = generate_unique_email(first_name, last_name, used_emails, DEFAULT_DOMAIN)
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


#TSV and CSV files
from functions import load_data, extract_names, generate_unique_email
from constaints import DEFAULT_DOMAIN

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
        unique_email = generate_unique_email(first_name, last_name, used_emails, DEFAULT_DOMAIN)
        email_addresses.append(unique_email)
    
    # Add the generated emails to the DataFrame
    df['Email'] = email_addresses
    
    # Display the generated email addresses
    for name, email in zip(df['Student Name'], email_addresses):
        print(f"Student Name: {name} - Email address: {email}")
    
    # Save the updated DataFrame to a new Excel file
    output_excel_file = "Updated_Test_Files.xlsx"
    df.to_excel(output_excel_file, index=False)
    print(f"Updated DataFrame saved to {output_excel_file}")
    
    # Save the updated DataFrame to a CSV file
    output_csv_file = "Updated_Test_Files.csv"
    df.to_csv(output_csv_file, index=False)
    print(f"Updated DataFrame saved to {output_csv_file}")
    
    # Save the updated DataFrame to a TSV file
    output_tsv_file = "Updated_Test_Files.tsv"
    df.to_csv(output_tsv_file, sep='\t', index=False)
    print(f"Updated DataFrame saved to {output_tsv_file}")

if __name__ == "__main__":
    file_path = 'Test Files.xlsx'
    main(file_path)
