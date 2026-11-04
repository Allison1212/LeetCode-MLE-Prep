import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:

    merge_df = candidates.merge(rounds, on = 'interview_id', how = 'left')

    res = merge_df.groupby('candidate_id', as_index = False).agg(years_of_exp = ('years_of_exp','max'), sum_score = ('score','sum'))

    return res[(res['years_of_exp'] >= 2) & (res['sum_score'] > 15)][['candidate_id']]