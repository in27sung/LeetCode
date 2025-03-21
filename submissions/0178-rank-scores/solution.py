import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Calculate rank in descending order, using 'dense' method to handle duplicate scores
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)

    # Return only 'score' and 'rank' columns, sorted by score in descending order
    return scores[['score', 'rank']].sort_values(by='score', ascending=False)


