from sqlalchemy import create_engine ,Column , Integer , String
from sqlalchemy.orm import Mapped , mapped_column , DeclarativeBase
from database_model import engine
class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = "Employee_table"
    
    e_id : Mapped[str] = mapped_column(String(20) , primary_key = True)
    name : Mapped[str] = mapped_column(String(20) , nullable = False)
    age : Mapped[int] = mapped_column(Integer , nullable = False)

# if not tagretted database not exist , then it generates the all defined databases
Base.metadata.create_all(engine)
