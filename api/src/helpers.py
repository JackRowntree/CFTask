import pandas as pd
import sqlalchemy
import logging
from datetime import datetime, timezone
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)
logger = logging.getLogger("My Logger")


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        called_at = datetime.now(timezone.utc)
        logger.info(f">>> Running {func.__name__!r} function. Logged at {called_at}")
        to_execute = func(*args, **kwargs)
        logger.info(f">>> Function: {func.__name__!r} executed. Logged at {called_at}")
        return to_execute

    return wrapper


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


def get_first_chunk():
    return pd.read_sql("select * from output limit 10", create_engine()).to_json(
        orient="records"
    )
