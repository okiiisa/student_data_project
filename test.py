import pandas as pd   

df = pd.read_excel('Test Files.xlsx')
print(df.head())


import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel("Test Files.xlsx")

# Generate unique email addresses
email_addresses = []
used_emails = set()

for index, row in df.iterrows():
    name = row['Student Name']
    parts = name.split(", ")
    
    first_name = parts[1].lower() if len(parts) > 1 else parts[0].lower()
    last_name = parts[0].lower() if len(parts) > 1 else ""
    
    email = f"{first_name[0]}{last_name}@gmail.com"
    unique_email = email
    i = 1
    while unique_email in used_emails:
        unique_email = f"{email}{i}"
        i += 1
    
    used_emails.add(unique_email)
    email_addresses.append(unique_email)

# Display the generated email addresses
for name, email in zip(df['Student Name'], email_addresses):
    print(f"Student Name: {name} - Email address: {email}")


