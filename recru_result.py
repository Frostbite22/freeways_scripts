from numpy.core.numeric import outer
import pandas as pd 
import numpy as np 
import functools


def outer_fn(keywords):
    def filtre(data) -> bool:
        for key in keywords:
            if key in data.lower():
                return True 
        return False 
    return filtre


def result(keywords ,file_name : str,dataframe,field) :
    l = list(filter(outer_fn(keywords),dataframe[f'{field}'].values))
    new_sheet = pd.DataFrame(columns=[x for x in dataframe.columns.values])

    for index,row in dataframe.iterrows():
        if row[f'{field}'] in l:
            r = {}
            r = dict(zip(new_sheet.columns.values,row))
            new_sheet = new_sheet.append(r,ignore_index=True)

    with pd.ExcelWriter(f"/root/Desktop/freeways/freeways_scripts/{file_name}.xlsx") as writer:
        new_sheet.to_excel(writer,sheet_name=f'{file_name}')  
    return new_sheet

if __name__ =="__main__":

    accepted = ["YES","yes"]
    rejected = ["NO", "no"]

    dataframe = pd.read_excel("/root/Desktop/freeways/freeways_scripts/recru.xlsx",sheet_name="Interviews",engine="openpyxl", dtype=str)
    dataframe.dropna(subset = ["Result"], inplace=True)
    acc = result(accepted,"accepted",dataframe,"Result")
    rej = result(rejected,"rejected",dataframe,"Result")

    accepted_emails= acc['Email']
    rejected_emails = rej['Email']


    f = open("/root/Desktop/freeways/freeways_scripts/accepted_emails.txt",'w+')
    for email in accepted_emails:
        f.write(f'{email}\n')
    f.close()

    f = open("/root/Desktop/freeways/freeways_scripts/rejected_emails.txt",'w+')
    for email in rejected_emails:
        f.write(f'{email}\n')
    f.close()


