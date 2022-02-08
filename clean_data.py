import pandas as pd

def clean_dataset(data):
    
    data['Crime ID'].fillna('c_id_NA', inplace = True)
    
    data['Last outcome category'].fillna("outcome_not_available", inplace = True)
    
    print('~~Empty values replaced!!')
    
    data.drop(['Context'],axis = 1, inplace = True)
    
    print('~~Dataset Cleaned')
    
    data= data.replace(',','',regex=True)
    
    data.drop_duplicates(inplace=True)
    
    print('~~Duplicated Entries Removed')
    
    return data