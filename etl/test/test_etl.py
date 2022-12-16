from unittest import mock
import sys

sys.path.append("../src/")
import extract as ex
import pandas as pd
import transform as tr
import load as lo
import run_etl as run


@mock.patch("extract.coerce_datetimes")
def test_enforce_schemas(mock_coerce_datetimes, extract_data):
    ex.enforce_schemas(extract_data)
    mock_coerce_datetimes.assert_called_with(extract_data)


def test_enforce_schemas(extract_data):
    ex.coerce_datetimes(extract_data)
    target = pd.DataFrame(
        {
            "blah": [1, 1, 1],
            "blah_date": pd.to_datetime(
                ["01/13/2011", "01/13/2021", "01/13/2015"], infer_datetime_format=True
            ),
        }
    )

    pd.testing.assert_frame_equal(extract_data["df1"], target)


@mock.patch("extract.pandas.read_csv", pd.DataFrame())
def read_csvs(mock_read_csv):
    out = ex.read_csvs()
    mock_read_csv.assert_called_with(
        ["/code/static/people.csv", "/code/static/trades.csv"]
    )
    assert list(out.keys()) == ["people", "trades"]
    for df in list(out.values()):
        pd.testing.assert_frame_equal(df, pd.DataFrame())


@mock.patch("extract.enforce_schemas")
@mock.patch("extract.read_csvs")
def test_extract(mock_read_csvs, mock_enforce_schemas, extract_data):
    mock_read_csvs.return_value = extract_data
    out = ex.extract()
    mock_read_csvs.assert_called_once()
    mock_enforce_schemas.assert_called_with(extract_data)
    for name, frame in out.items():
        pd.testing.assert_frame_equal(frame, extract_data[name])


@mock.patch("transform._transform")
def test_transform(mock__transform, extract_data):
    mock_transformed = pd.DataFrame({"transformed": [1]})
    mock__transform.return_value = mock_transformed
    out = tr.transform(extract_data)
    mock__transform.assert_called_with(extract_data)
    pd.testing.assert_frame_equal(out, mock_transformed)


def test__transform(representative_extract_data):
    target = pd.DataFrame(
        {
            "person_id": [1, 2, 3],
            "blah": [4, 5, 6],
            "date": pd.to_datetime(
                ["01/13/2011", "01/13/2021", "01/14/2011"], infer_datetime_format=True
            ),
            "stock": ["A", "B", "D"],
        }
    )
    out = tr._transform(representative_extract_data)
    print(out)
    pd.testing.assert_frame_equal(out, target)


@mock.patch("load.create_engine")
@mock.patch("load.DataFrame.to_sql")
def test_load(mock_to_sql, mock_create_engine):
    lo.load(pd.DataFrame)
    mock_to_sql.assert_called_with("output", mock_create_engine(), if_exists="replace")


@mock.patch("run_etl.load")
@mock.patch("run_etl.transform")
@mock.patch("run_etl.extract")
def test_run_tel(test_e, test_t, test_l, extract_data):
    test_e.return_value = extract_data
    test_t.return_value = extract_data
    run.run_etl()
    test_e.assert_called_once()
    test_t.assert_called_with(extract_data)
    test_l.assert_called_with(extract_data)
