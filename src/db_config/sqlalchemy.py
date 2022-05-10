from .credentials import user, password, host, port, database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# def get_sqlalchemy_connection():
#     try:
#         engine = create_engine(
#             url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
#         )
#         print(
#             f"Connection to the {host} for user {user} created successfully using ORM."
#         )
#         Session = sessionmaker(bind=engine)
#         session = Session()

#         return engine, session

#     except Exception as ex:
#         print(f"Connection could not be made due to the following error: {ex}")

engine = create_engine(
    url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
)

print(f"Connection to the {host} for user {user} created successfully using ORM.")

Session = sessionmaker(bind=engine)
session = Session()
