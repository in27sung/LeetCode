import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    # Group rounds by interview_id and compute total score
    interview_scores = rounds.groupby('interview_id')['score'].sum().reset_index()

    # Filter those with toal score > 15
    passed_interviews = interview_scores[interview_scores['score'] > 15]

    # Merge with candidates on interview_id
    merged = pd.merge(candidates, passed_interviews, on='interview_id', how='inner')

    # Filter by years of experience
    result = merged[merged['years_of_exp'] >= 2]

    # Return only required columns
    return result[['candidate_id']]
