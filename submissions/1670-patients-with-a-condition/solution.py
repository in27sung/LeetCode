import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r'(^| )DIAB1'
    return patients[patients['conditions'].str.contains(pattern)]
