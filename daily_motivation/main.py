import smtplib
import datetime as dt
import random
mail = ''
pas = ''
to = ['ashintv2003@gmail.com','aksreelakshmi22@gmail.com']
if dt.datetime.now().weekday() in [0,1,2,3]:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(mail,pas)
        for i in to:
            connection.sendmail(
                from_addr=mail,
                to_addrs=i,
                msg=f'subject:Motivation\n\n{quote}'
            )
        print('mail send')