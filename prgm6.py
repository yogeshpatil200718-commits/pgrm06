import sys

def employee_details(name, employee_id, department, salary):
    return (
        f"Name: {name}\n"
        f"Employee Id: {employee_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Yogesh Patil"
    employee_id = sys.argv[2] if len(sys.argv) > 2 else "EMP101"
    department = sys.argv[3] if len(sys.argv) > 3 else "IT"
    salary = sys.argv[4] if len(sys.argv) > 4 else "50000"

    print("\nEmployee Details")
    print(employee_details(name, employee_id, department, salary))