from prgm6 import employee_details

def test_employee_details():
    result = employee_details("Yogesh Patil", "EMP101", "IT", 50000)
    expected = (
        "Name: Yogesh Patil\n"
        "Employee Id: EMP101\n"
        "Department: IT\n"
        "Salary: 50000"
    )
    assert result == expected