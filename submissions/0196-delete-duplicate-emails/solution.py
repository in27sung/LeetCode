import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort by id to keep the smallest id
    person.sort_values(by='id', inplace=True)
    
    # Drop duplicates based on email, keeping the first occurrence
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)
