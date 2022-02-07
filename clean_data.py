import pandas as pd

def clean_dataset(data):
    
    data['Crime ID'].fillna('c_id_NA', inplace = True)
    
    data['Last outcome category'].fillna("outcome_not_available", inplace = True)
    
    print('Empty cells filled with respective values')
    
    data.drop(['Context'],axis = 1, inplace = True)
    
    data.drop_duplicates(inplace=True)
    
    print('unnecessary Columns removed')
    
    return data