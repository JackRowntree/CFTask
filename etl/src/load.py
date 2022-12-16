from logger import log
import sqlalchemy
from typing import Dict
from pandas import DataFrame


def create_engine():
    db_name = "database"
    db_user = "username"
    db_pass = "secret"
    db_host = "db"
    db_port = "5432"
    # Connecto to the database
    db_string = "postgresql://{}:{}@{}:{}/{}".format(
        db_user, db_pass, db_host, db_port, db_name
    )
    db = sqlalchemy.create_engine(db_string)
    return db


@log
def load(df: DataFrame):
    """
    Loads data into db
    """
    df.to_sql("output", create_engine(), if_exists="replace")
