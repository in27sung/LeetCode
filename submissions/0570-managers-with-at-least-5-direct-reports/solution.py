import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee.groupby('managerId').size()
    manager_ids = counts[counts >= 5].index

    return employee[employee['id'].isin(manager_ids)][['name']]
    
