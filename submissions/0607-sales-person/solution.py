import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Rename company.name to avoid name collision
    company = company.rename(columns={'name': 'company_name'})

    # Merge all tables
    merged = orders.merge(company, on='com_id').merge(sales_person, on='sales_id')

    # Find salespeople who sold to RED
    red_sales = merged.loc[merged['company_name'] == 'RED', 'sales_id'].unique()

    # Filter out salespeople who sold to RED
    result = sales_person[~sales_person['sales_id'].isin(red_sales)][['name']]

    return result
