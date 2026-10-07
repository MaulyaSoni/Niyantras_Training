import uuid
from sqlalchemy import UUID
from sqlalchemy import create_engine ,Column , Integer , String , ForeignKey
from sqlalchemy.orm import Mapped , mapped_column , DeclarativeBase , relationship
from database.db import engine

class Base(DeclarativeBase):
    pass

class Department(Base):
    __tablename__ = "Department_table"
    
    # dept_id : Mapped[int] = mapped_column(Integer , primary_key = True , autoincrement = True)
    dept_id : Mapped[uuid.UUID] = mapped_column(String(36) , default=uuid.uuid4)
    dept_name : Mapped[str] = mapped_column(String(20) , primary_key = True)

    employee_object = relationship("Employee" , back_populates = "department_object")

class Employee(Base):
    __tablename__ = "Employee_table"

    # e_id : Mapped[str] = mapped_column(String(20) , primary_key = True)
    e_id : Mapped[uuid.UUID] = mapped_column(String(36), primary_key=True, default=uuid.uuid4)
    name : Mapped[str] = mapped_column(String(20) , nullable = False)
    age : Mapped[int] = mapped_column(Integer , nullable = False)

    dept_name : Mapped[str] = mapped_column(ForeignKey("Department_table.dept_name"), nullable= False)
    department_object =relationship ("Department" , back_populates = "employee_object")

class Users(Base):
    __tablename__ = "User_table"
    
    # userid : Mapped[int] = mapped_column(Integer , primary_key = True , autoincrement = True)
    userid : Mapped[uuid.UUID] = mapped_column(String(36), primary_key=True, default=uuid.uuid4)
    username : Mapped[str] = mapped_column(String(20) , nullable = False)
    hashed_password : Mapped[str] = mapped_column(String(100) , nullable = False)
    user_role : Mapped[str] = mapped_column(String(20), nullable = False)
