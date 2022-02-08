#!/usr/bin/env python
import snowflake.connector
import pandas as pd
#### https://docs.snowflake.com/en/user-guide/python-connector-example.html
from glob import glob
from clean_data import clean_dataset







filenames = glob('raw_datasets/*/20*.csv',recursive=True) 
print(len(filenames))





for file in filenames:
    # Read the data files individually 
    data = pd.read_csv(file)
    
    print('Reading file ==>' ,file)
    
    #Cleaning the data base for null values and replacing the with corrresponing valuse and droping unwanted columns
    
    data=clean_dataset(data)
    
    print('Cleaned file ==>',file)
    
    
    #Saving the cleaned file to to new directory
     
    p = 'processed_datasets/'+file[21:] 
    
    data.to_csv(p,header=None,index=False)
    
    print('Saving File ==>',file)
    print('#########################################################################################################################')
    
    



cleaned_filenames = glob('processed_datasets/20*.csv') 
print(len(cleaned_filenames))


print('_______________________________________________________________________________________Connecting to Snowflake____________________________________________________________________________________')

# Create main connection context
con = snowflake.connector.connect(
    user='anuragvuppala',
    password='Snow@Flake44',
    account='vx24548.europe-west2.gcp'
)




c = con.cursor()
c.execute("SELECT current_version()").fetchone()

print('Connected to Snowflake..............!')



c.execute("USE ROLE ACCOUNTADMIN")

c.execute("CREATE WAREHOUSE IF NOT EXISTS STREET_CRIME_WH")
c.execute("CREATE DATABASE IF NOT EXISTS STREET_CRIME_DB")
c.execute("USE WAREHOUSE STREET_CRIME_WH")
c.execute('USE DATABASE STREET_CRIME_DB')
c.execute('USE SCHEMA PUBLIC')


print('Warehouse and Database Created and in USE...........')


print('Table Creates/IN-USE............')
c.execute('CREATE TABLE IF NOT EXISTS "CRIME_DATA_TABLE" (crime_id STRING, month STRING, reported_by STRING, fall_within STRING, longitude FLOAT, latitude FLOAT, location STRING, lsoa_code STRING, lsoa_name STRING, crime_type STRING, last_outcome STRING, id integer not null constraint unique_id primary key not enforced)')

print('Stagging files...............')
c.execute("PUT file://processed_datasets/20*.csv @%crime_data_table")


print('Copying files...............')

c.execute("COPY INTO CRIME_DATA_TABLE")


print('...................................................................................................................DATA UPLOADED.................................................................................................................')

print('Romoving files form Stageing area...............')
c.execute("Remove @%crime_data_table")

print('Romoved files form Stageing area!')


crime_count_bytype = c.execute("SELECT crime_type,COUNT(crime_type) FROM CRIME_DATA_TABLE GROUP BY crime_type ORDER BY COUNT(crime_type) DESC; ").fetchall()
print(crime_count_bytype)

crime_count_bystreet = c.execute("SELECT location,COUNT(crime_type) FROM CRIME_DATA_TABLE GROUP BY location ORDER BY COUNT(crime_type) DESC; ").fetchall()
print(crime_count_bystreet)


con.close() 

print('________________________________________________________________________DATABASE CONNECTION CLOSED_____________________________________________________________________________________')   
    
    
    
    