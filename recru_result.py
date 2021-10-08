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


def result(status ,file_name : str) -> None:
    l = list(filter(outer_fn(status),dataframe['Result'].values))
    new_sheet = pd.DataFrame(columns=[x for x in dataframe.columns.values])

    for index,row in dataframe.iterrows():
        if row['Result'] in l:
            r = {}
            r = dict(zip(new_sheet.columns.values,row))
            new_sheet = new_sheet.append(r,ignore_index=True)

    new_sheet.to_excel(f"{file_name}.xlsx")  

if __name__ =="__main__":

    accepted = ["YES","yes"]
    rejected = ["NO", "no"]

    dataframe = pd.read_excel("recru.xlsx",sheet_name="Interviews",engine="openpyxl", dtype=str)
    dataframe.dropna(subset = ["Result"], inplace=True)
    
    result(accepted,"accepted")
    result(rejected,"rejected")


