import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return (
        courses['class']
        .value_counts()
        .loc[lambda x: x >= 5]
        .index.to_frame(index=False)
        .rename(columns={0: 'class'})
    )
