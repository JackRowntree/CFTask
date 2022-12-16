import pytest
import sys

sys.path.append("../src/")
from app import create_app
from unittest.mock import patch
import json


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    with patch("app.get_first_chunk", return_value=json.loads('{"data": "data"}')):
        yield app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
