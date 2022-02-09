#!/usr/bin/env python
import snowflake.connector
import pandas as pd
import numpy as np
from snowflake.connector.pandas_tools import write_pandas
from snowflake.connector.pandas_tools import pd_writer
###
# https://docs.snowflake.com/en/user-guide/python-connector-example.html
from glob import glob

from ETL import ET_load



# Create main connection context
con = snowflake.connector.connect(
    user='anuragvuppala',
    password='Snow@Flake44',
    account='vx24548.europe-west2.gcp'
)
c = con.cursor()
f= c.execute("SELECT current_version()").fetchone()
print(f)


c.execute("USE ROLE ACCOUNTADMIN")

c.execute("CREATE WAREHOUSE IF NOT EXISTS STREET_CRIME_WH")
c.execute("CREATE DATABASE IF NOT EXISTS STREET_CRIME_DB")
c.execute("USE WAREHOUSE STREET_CRIME_WH")
c.execute('USE DATABASE STREET_CRIME_DB')
c.execute('USE SCHEMA PUBLIC')


output = c.execute('''                                  ''').fetchall()
print(output)

con.close()


