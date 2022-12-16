from logger import logger
from sqlalchemy import create_engine
from typing import Dict
from pandas import DataFrame

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

@logger
def load(df: Dict[str, DataFrame]):
	"""
	Loads data into db
	"""
	df.to_sql('output',db)