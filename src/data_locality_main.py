from matplotlib.pyplot import close
from db_config import mysql_db, cursor, session
from model import WeatherStation
from db_config import host, user, password, database, port
import threading
import time
import mysql.connector as mysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from codetiming import Timer

distantServer = {
    'host': "database-1.chvixucrsk1d.eu-west-3.rds.amazonaws.com",
    'port': 3306,
    'user': 'root',
    'pass': 'pass1234',
    'database': 'database1'
}

closeServer = {
    'host': "large-scale-db.csaczpzfcpsq.us-west-1.rds.amazonaws.com",
    'port': 3306,
    'user': 'root',
    'pass': 'cmpe_226',
    'database': 'meso_west_db'
}


def fetchJDBC(server, query="SELECT * FROM weather_station_data"):
    mysql_db = mysql.connect(
        host=server['host'],
        user=server['user'],
        password=server['pass'],
        database=server['database']
    )
    cursor = mysql_db.cursor()
    cursor.execute(query)
    # print(f"SQL res: {cursor.fetchone()}")


def fetchORM(server, model=WeatherStation):
    engine = create_engine(
        url=f"mysql+pymysql://{server['user']}:{server['pass']}@{server['host']}:{server['port']}/{server['database']}")
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(model)
    # print(f"ORM res: {res[0].stationId}")


@Timer(name="decorator")
def jdbcCloseServer():
    print(f"NA server: JDBC")
    fetchJDBC(closeServer)


@Timer(name="decorator")
def ormCloseServer():
    print(f"NA server: ORM")
    fetchJDBC(closeServer)


@Timer(name="decorator")
def jdbcDistantServer():
    print(f"EU server: JDBC")
    fetchJDBC(distantServer)


@Timer(name="decorator")
def ormDistantServer():
    print(f"EU server: ORM")
    fetchORM(distantServer)


jdbcCloseServer()
ormCloseServer()
jdbcDistantServer()
ormDistantServer()
