import snowflake.connector
import time

con = snowflake.connector.connect(
    user='anuragvuppala',
    password='Snow@Flake44',
    account='VX24548.europe-west2.gcp'
    )

c = con.connect()

try:
    c.execute("USE DATABASE UK_CRIME_DB")
    data = c.execute("SELECT * FROM TABLE CRIME_DATA")
    q_id= c.sfqid
    while con.is_still_running(con.get_query_status(q_id)):
        time.sleep(1)
    print(data)
finally:
    c.close()
    con.close()


