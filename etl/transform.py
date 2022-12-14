from common.logging import logger
from etl.db import connect_db

@logger
def transform(df):
	"""
	Transforms data
	"""
	transformed_df = _transform(df)
	return transformed_df

@logger
def _transform(df):
	pass