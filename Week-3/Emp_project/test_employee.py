from operations.employee import get_all_emp , get_all_emp_details , create_emp , update_emp , delete_emp
from models.model import Employee , Department
from schemas.employee import EmployeeSchema

def test_create_emp():
    department = Department(dept_id = "dept01" , dept_name = "HR")
    db.add(department)
    db.commit()

    employee = EmployeeSchema(e_id="emp01" , name = "KK" , age=25 , dept_id="dept01")
    db.add(employee)
    db.commit()

    result = create_emp(db , employee)

    assert result.e_id == "emp01"
    assert result.name == "KK"
    assert result.age == 25
    assert result.dept_id == "dept01"

# @pytest.fixture

def test_get_all_emp():
 