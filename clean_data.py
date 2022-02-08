import pandas as pd

def clean_dataset(data):
    
    data['Crime ID'].fillna('c_id_NA', inplace = True)
    
    data['Last outcome category'].fillna("outcome_not_available", inplace = True)
    
    print('~~Empty values replaced!!')
    
    data.drop(['Context'],axis = 1, inplace = True)
    
    print('~~Dataset Cleaned!!')
    
    data= data.replace(',','',regex=True)
    
    data.drop_duplicates(inplace=True)
    
    print('~~Duplicated Entries Removed')
    
    data['u_id']= data['Crime ID']+data['Month']+data['Reported by']+data['Location']+data['LSOA code']+data['Last outcome category']+ str(data['Longitude']*data['Latitude'])
    data['UN_ID']=data['u_id'].apply(hash)
    data.drop(['u_id'],axis = 1, inplace = True)
    print('~~UniqueID Created!!')
    
    return data