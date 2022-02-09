import pandas as pd

def ET_load(data):

    for name in data.columns:
        if name == 'Longitude' or  name =='Latitude':
            data[name].fillna(0, inplace = True)
        else:
            data[name].fillna('NA', inplace = True)
    print('~~Empty values replaced!!')


    #Creating a UNIQUE VALUE FOR EACH ROW
    data['UN_ID'] = ""
    for name in data.columns:
        data['UN_ID'] = data['UN_ID'] + str(data[name])
         

    data['UN_ID']=data['UN_ID'].apply(hash)
    print('~~UniqueID Created!!')


    data.drop(['Context'],axis = 1, inplace = True)
    print('~~UniqueID Created!!')


    data= data.replace(',','',regex=True)
    print('~~Dataset Cleaned!!')


    data.drop_duplicates(inplace=True)
    print('~~Duplicated Entries Removed')
    
    return data