import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Compute time spent per login session
    employees['spent_time'] = employees['out_time'] - employees['in_time']
    
    # Group by employee and day, then sum total spent time
    result = employees.groupby(['emp_id', 'event_day'])['spent_time'].sum().reset_index()

    # Reorder columns and rename them as required
    result = result[['event_day', 'emp_id', 'spent_time']]
    result.rename(columns={'event_day': 'day', 'spent_time': 'total_time'}, inplace=True)

    return result
