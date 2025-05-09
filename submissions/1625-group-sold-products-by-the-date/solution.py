import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouped = activities.groupby('sell_date')['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))
    ]).reset_index()

    return grouped.sort_values('sell_date')
