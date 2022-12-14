from common.logging import logger
from etl.db import get_engine

@logger
def load(df):
	"""
	Loads data into db
	"""
	df.to_sql(get_engine())