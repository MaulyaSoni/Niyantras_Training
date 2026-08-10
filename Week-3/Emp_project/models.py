from sqlalchemy import create_engine ,Column , Integer , String
from sqlalchemy.orm import Mapped , mapped_column , DeclarativeBase , relationship
from database import engine

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = "Employee_table"
    
    e_id : Mapped[str] = mapped_column(String(20) , primary_key = True)
    name : Mapped[str] = mapped_column(String(20) , nullable = False)
    age : Mapped[int] = mapped_column(Integer , nullable = False)
    # child : Mapped["Child"] = relationship(back_populates = "parent")

class EmployeeSalary(Base):
    __tablename__ = "Salary_table"

    e_id : Mapped[str] = mapped_column(String(20) , primary_key= True)
    salary : Mapped[int] = mapped_column(Integer , nullable=False)
    present_days : Mapped[int] = mapped_column(Integer , nullable=False)
    # parent : Mapped["Parent"] = relationship(back_populates="child")



