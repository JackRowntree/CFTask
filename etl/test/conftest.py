import pandas as pd 
import pytest

@pytest.fixture
def extract_data():
	return {'df1': pd.DataFrame({
		'blah':[1,1,1],
		'blah_date':['01/13/2011','01/13/2021','01/13/2015']
		})
	}