from db_config import mysql_db, cursor, session
from model import Customer
from db_config import host, user, password, database, port
import threading
import time
import mysql.connector as mysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def concurrent_burst_reads(
    query,
):
    mysql_db = mysql.connect(host=host, user=user, password=password, database=database)
    cursor = mysql_db.cursor()
    cursor.execute(query)
    print(f"SQL res: {cursor.fetchone()}")


def concurrent_burst_reads_orm(model=Customer):
    engine = create_engine(
        url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(model).filter(Customer.id == 1)
    print(f"ORM res: {res[0].name}")


def sql_worker():
    query = "SELECT name FROM customer WHERE id=1"
    concurrent_burst_reads(
        query,
    )


def sql_orm_worker():
    concurrent_burst_reads_orm()


"""
    Simulating concurrent burst reads (many small reads)  
    execution flow begins below
"""

sql_threads = []
sql_orm_threads = []

start = time.time()
for i in range(100):
    t = threading.Thread(target=sql_worker)
    sql_threads.append(t)
    t.start()
    t.join()
end = time.time()
print("Time taken to execute short reads on 100 threads using SQL => ", end - start)

start = time.time()
for i in range(100):
    t = threading.Thread(target=sql_orm_worker)
    sql_orm_threads.append(t)
    t.start()
    t.join()
end = time.time()
print("Time taken to execute short reads on 100 threads using ORM => ", end - start)
