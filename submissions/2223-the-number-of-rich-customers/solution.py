import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where the bill amount is strictly greater than 500
    rich_bills = store[store['amount'] > 500]
    
    # Count the number of unique customers with at least one such bill
    rich_count = rich_bills['customer_id'].nunique()

    # Return the result as a one-row DataFrame
    return pd.DataFrame({'rich_count': [rich_count]})
