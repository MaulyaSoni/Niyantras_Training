import sqlalchemy
from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column , relationship
from sqlalchemy import create_engine
import psycopg2

print(psycopg2.__version__)
print(sqlalchemy.__version__)

# engine = create_engine('postgresql+psycopg2://username:password\@127.0.0.1:5432/testdb')

connection = engine.connect()
print("Connection successfully done")
connection.close()