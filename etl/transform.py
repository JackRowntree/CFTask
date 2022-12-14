from common.logging import logger
from etl.db import connect_db

@logger
def transform(df: Dict[str, DataFrame]) -> DataFrame:
	"""
	Transforms data
	"""
	transformed_df = _transform(df)
	return transformed_df

@logger
def _transform(df: Dict[str, DataFrame]) -> DataFrame:
	df_people = transformed_df['people']
	df_trades = transformed_df['trades']
	most_recent_trade_index = df_trades.groupby('date').B.idxmin()
	df_trades_latest = df.loc[most_recent_trade_index].reset_index(drop=True)
	df_people_with_latest_trade = df_people.merge(df_trades_latest, by='id', how='left')
	return df_people_with_latest_trade

