import pandas as pd 



dataframe = pd.read_excel("/root/Desktop/freeways/freeways_scripts/recru.xlsx",sheet_name="Interviews",engine="openpyxl", dtype=str)
not_yet_contacted = dataframe['Interview Date and Time (dd/mm/yyyy hh:mm )'].isnull()
emails_not_yet_contacted = dataframe[not_yet_contacted]["Email"]

f = open("/root/Desktop/freeways/freeways_scripts/not_contacted_emails.txt",'w+')
for email in emails_not_yet_contacted:
    f.write(f'{email}\n')
f.close()

   

