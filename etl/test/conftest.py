import pandas as pd
import pytest


@pytest.fixture
def extract_data():
    return {
        "df1": pd.DataFrame(
            {"blah": [1, 1, 1], "blah_date": ["01/13/2011", "01/13/2021", "01/13/2015"]}
        )
    }


@pytest.fixture
def representative_extract_data():
    return {
        "people": pd.DataFrame({"person_id": [1, 2, 3], "blah": [4, 5, 6]}),
        "trades": pd.DataFrame(
            {
                "person_id": [1, 2, 3, 3, 2, 1],
                "date": pd.to_datetime(
                    [
                        "01/13/2011",
                        "01/13/2021",
                        "01/13/2015",
                        "01/14/2011",
                        "01/14/2021",
                        "01/14/2015",
                    ],
                    infer_datetime_format=True,
                ),
                "stock": ["A", "B", "C", "D", "E", "F"],
            }
        ),
    }
