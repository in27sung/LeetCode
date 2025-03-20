import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge Employee and Departement tables
    merged = employee.merge(department, left_on='departmentId', right_on='id')

    # Find max salary per department
    max_salary = merged.groupby('departmentId')['salary'].transform('max')

    # Filter rows where salary equals max salary
    result = merged[merged['salary'] == max_salary][['name_y', 'name_x', 'salary']]

    # Rename colums as per requirement
    result.columns = ['Department', 'Employee', 'Salary']

    return result
    
