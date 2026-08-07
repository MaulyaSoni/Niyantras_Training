from sqlalchemy import create_engine ,Column , Integer , String

engine = create_engine("sqlite://", echo=True)

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = "Employee_table"
    
    e_id = Column(Integer , primary_key = True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String , unique = True)