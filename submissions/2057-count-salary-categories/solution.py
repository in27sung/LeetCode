import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Define conditions for each category
    low = (accounts['income'] < 20000)
    average = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000))
    high = (accounts['income'] > 50000)
    
    # Count number of accounts in each category
    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [
            low.sum(),
            average.sum(),
            high.sum()
        ]
    })
    
    return result
