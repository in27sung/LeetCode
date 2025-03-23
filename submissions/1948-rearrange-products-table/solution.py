import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return products.melt(id_vars='product_id', value_name='price', var_name='store').dropna().sort_values(by=['product_id'])
