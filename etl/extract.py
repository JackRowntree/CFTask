from common.logging import logger

CSV_PATH = ""

@logger
def extract():
	"""
	Reads data from db
	"""
	extracted_df = pd.read_csv(CSV_PATH)
	return extracted_df