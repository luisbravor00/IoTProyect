from dotenv import load_dotenv
import oracledb
import os

load_dotenv()
dbuser = os.getenv('DATABASE_USER')
dbpswd = os.getenv('DATABASE_PSWD')
dbdir = os.getenv('DIR_LOCATION')
cs = os.getenv('CONN_ST')

connection = oracledb.connect(config_dir = dbdir,  user= dbuser, 
                              password=dbpswd, dsn=cs, 
                              wallet_location = dbdir, wallet_password=dbpswd)

cursor = connection.cursor()
