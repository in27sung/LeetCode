import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(unique_salaries) >= 2:
        return pd.DataFrame({"SecondHighestSalary": [unique_salaries.iloc[1]]})
    else:
        return pd.DataFrame({"SecondHighestSalary": [None]})
