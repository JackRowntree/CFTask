@mock.patch("extract.coerce_datetimes")
def test_enforce_schemas(mock_coerce_datetimes, extract_data):
	with self.assertLogs('foo', level='INFO') as cm:
   		ex.enforce_schemas(extract_data)
    	print(cm.output)