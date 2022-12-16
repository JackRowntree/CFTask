from unittest import mock
import sys
sys.path.append("../src/")
import extract as ex
import pandas as pd

@mock.patch('extract.coerce_datetimes')
def test_enforce_schemas(mock_coerce_datetimes,extract_data):
	ex.enforce_schemas(extract_data)
	mock_coerce_datetimes.assert_called_with(extract_data)

def test_enforce_schemas(extract_data):
	ex.coerce_datetimes(extract_data)
	target = pd.DataFrame({
		'blah':[1,1,1],
		'blah_date':pd.to_datetime(['01/13/2011','01/13/2021','01/13/2015'],infer_datetime_format = True)
		})
	
	pd.testing.assert_frame_equal(extract_data['df1'], target)

def test_extract():
	pass

def test_transform():
	pass

def test__transform():
	pass

def test_load():
	pass
