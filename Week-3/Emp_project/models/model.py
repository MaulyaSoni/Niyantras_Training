from sqlalchemy import create_engine ,Column , Integer , String , ForeignKey
from sqlalchemy.orm import Mapped , mapped_column , DeclarativeBase , relationship
from database import engine

class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = "Department_table"

    dept_id : Mapped[str] = mapped_column(String(20) , primary_key = True)
    dept_name : Mapped[str] = mapped_column(String(20) , nullable = False)

    employee_object = relationship("Employee" , back_populates = "department_object")


class Employee(Base):
    __tablename__ = "Employee_table"
    
    e_id : Mapped[str] = mapped_column(String(20) , primary_key = True)
    name : Mapped[str] = mapped_column(String(20) , nullable = False)
    age : Mapped[int] = mapped_column(Integer , nullable = False)

    #foreign key 
    dept_id : Mapped[str] = mapped_column(ForeignKey("Department_table.dept_id"), nullable= False)
   
    department_object =relationship ("Department" , back_populates = "employee_object")

class Users(Base):
    __tablename__ = "User_table"
    
    #autoincrement for new user coming 
    userid : Mapped[int] = mapped_column(Integer , primary_key = True , autoincrement = True)
    username : Mapped[str] = mapped_column(String(20) , nullable = False)
    hashed_password : Mapped[str] = mapped_column(String(100) , nullable = False)
    user_role : Mapped[str] = mapped_column(String(20), nullable = False)
    # admin_key : Mapped[str] = mapped_column(String(100))
    
# class Admin(Base):
#     __tablename__ = "Admin_table"

#     admin_id : Mapped[int] = mapped_column(Integer , primary_key = True , autoincrement = True)
#     admin_name : Mapped[str] = mapped_column(String , nullable = False)
