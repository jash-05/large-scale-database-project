# from db_config import get_mysql_connection
from service import InsertService
import time

# db_engine = get_mysql_connection()
# orm_engine, orm_session = get_sqlalchemy_connection()

insertService = InsertService()

start = time.time()
insertService.bulkInsertWithOrm()
end = time.time()

print("Time taken to add 5 million records to db using SQL alchemy => ", end - start)

# start = time.time()
# insertService.bulkInsert()
# end = time.time()

# print("Time taken to add 43200 records to db using SQL => ", end - start)
