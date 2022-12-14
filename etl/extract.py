from common.logging import logger
from typing import Dict
from pandas import DataFrame

class NameInfo(TypedDict):
    name: str
    first_letter: str
CSV_PATH = ""

@logger
def extract() -> Dict[str, DataFrame]:
	"""
	Reads data from db
	"""
	extracted_dfs = pd.read_csv(CSV_PATH)
	return extracted_df