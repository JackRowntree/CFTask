from logger import logger
from typing import Dict
import pandas as pd

CSV_PATH = "../static/"
CSV_KEYS_AND_PATHS = {
	'people': CSV_PATH + 'people.csv',
	'trades': CSV_PATH + 'trades.csv'
}

@logger
def extract() -> Dict[str, pd.DataFrame]:
	"""
	Reads data from db
	"""
	extracted_dfs = {key: pd.read_csv(path) for key,path in CSV_KEYS_AND_PATHS.items()}
	enforce_schemas(extracted_dfs)
	return extracted_dfs

@logger
def enforce_schemas(dfs: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
	"""
	Here is where schemas/dtypes could theoretically be enforced.
	"""
	coerce_datetimes(dfs)

@logger
def coerce_datetimes(dfs: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
	"""
	Any cols with 'date' get converted to dt (clearly not optimal, but for the sake of expediency)
	"""
	for key, df in dfs.items():
		for col in df.columns:
			if 'date' in col:
				df[col] = pd.to_datetime(df[col], infer_datetime_format = True)