import oracledb
import os
from dotenv import load_dotenv

load_dotenv()
dbuser = os.getenv('DATABASE_USER')
dbpswd = os.getenv('DATABASE_PSWD')
dbdir = os.getenv('DIR_LOCATION')
cs = os.getenv('CONN_ST')

print(dbdir)

connection = oracledb.connect(config_dir=dbdir, user=dbuser,
                              password=dbpswd, dsn=cs,
                              wallet_location=dbdir, wallet_password=dbpswd)

cursor = connection.cursor()

#Change name of table you need to drop
query = """select * from Prescription_Details
"""

cursor.execute(query)

connection.commit()