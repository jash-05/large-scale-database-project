from .credentials import user, password, host, port, database
from sqlalchemy import create_engine
import pymysql


def get_sqlalchemy_connection():
    try:
        engine = create_engine(
            url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        )
        print(
            f"Connection to the {host} for user {user} created successfully using ORM."
        )
        return engine
    except Exception as ex:
        print(f"Connection could not be made due to the following error: {ex}")
