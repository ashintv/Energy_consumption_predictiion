from datetime import datetime
import pandas as pd
import random
import smtplib

# Define email credentials (ideally use environment variables for security)
mail = ''
pas = ''

# Read the CSV file
data = pd.read_csv('birthdays.csv')

# Create a dictionary with (month, day) as keys and each row of data as values
bdays = {(row['month'], row['day']): row for (index, row) in data.iterrows()}

# Get today's date
today = (datetime.now().month, datetime.now().day)

# Check if today is anyone's birthday
if today in bdays:
    print('Match found!')
    info = bdays[today]
    print(info)

    # Select a random letter template
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace('[NAME]', info['name'])

    # Send the email
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(mail, pas)
        print('Login successful', info['email'])
        connection.sendmail(
            from_addr=mail,
            to_addrs=info['email'],
            msg=f'Subject:Happy Birthday!!\n\n{contents}'
        )
        print('Email sent')
else:
    print("No birthdays today.")