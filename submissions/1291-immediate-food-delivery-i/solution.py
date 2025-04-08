import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Count row where delivery was immediate
    immediate_count = (delivery['order_date'] == delivery['customer_pref_delivery_date']).sum()

    # Total number of orders
    total_orders = len(delivery)

    # Calculate percentage (rounded to 2 decimal places)
    percentage = round(immediate_count / total_orders * 100, 2)

    # Return result as DataFrame
    return pd.DataFrame({'immediate_percentage': [percentage]})
