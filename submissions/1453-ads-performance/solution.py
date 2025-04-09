import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    def process(g):
        return (g['action'] == 'Clicked').sum() / (g['action'] != 'Ignored').sum() * 100
    
    res = ads.groupby('ad_id').apply(process).reset_index(name='ctr')
    return res.fillna(0).round(2).sort_values(['ctr', 'ad_id'], ascending=[False, True])
