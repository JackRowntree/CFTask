from logger import logger
from typing import Dict
from pandas import DataFrame

@logger
def transform(dfs: Dict[str, DataFrame]) -> DataFrame:
	"""
	Transforms data
	"""
	transformed_df = _transform(dfs)
	return transformed_df

@logger
def _transform(dfs: Dict[str, DataFrame]) -> DataFrame:
	df_people = dfs['people']
	df_trades = dfs['trades']
	most_recent_trade_index = df_trades.groupby('person_id').date.idxmin()
	df_trades_latest = df_trades.loc[most_recent_trade_index].reset_index(drop=True)
	df_people_with_latest_trade = df_people.merge(df_trades_latest, on='person_id', how='left')
	return df_people_with_latest_trade

