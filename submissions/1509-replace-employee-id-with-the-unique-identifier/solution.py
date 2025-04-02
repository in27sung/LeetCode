import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Perform left join on 'id' to bring in 'unique_id'
    merged = pd.merge(employees, employee_uni, how='left', on='id')

    # Select only the required columns
    return merged[['unique_id', 'name']]


