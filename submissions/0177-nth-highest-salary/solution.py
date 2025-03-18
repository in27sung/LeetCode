import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    result = employee[employee['salary'].rank(method='dense', ascending=False) == N]['salary']

    # Return result as required format
    if not result.empty:
        return pd.DataFrame({f'getNthHighestSalary({N})': [result.iloc[0]]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
