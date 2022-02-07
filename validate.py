#!/usr/bin/env python
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='anuragvuppala',
    password='Snow@Flake44',
    account='VX24548.europe-west2.gcp'
    )
c = ctx.cursor()
try:
    c.execute("USE DATABASE UK_CRIME_DB")
    c.execute("USE SCHEMA UK_CRIME_DB.PUBLIC")
    data = c.execute("SELECT * FROM crime_data")
    print(data)
   
    # cs.execute("SELECT current_version()")
    # one_row = cs.fetchone()
    # print(one_row[0])
finally:
    c.close()
ctx.close()