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

class EmployeeSalary(Base):
    __tablename__ = "Salary_table"

    e_id : Mapped[str] = mapped_column(String(20) , primary_key= True)
    salary : Mapped[int] = mapped_column(Integer , nullable=False)
    present_days : Mapped[int] = mapped_column(Integer , nullable=False)