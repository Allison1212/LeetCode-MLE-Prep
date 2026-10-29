import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense',ascending = False).astype(int)
    
    return scores.sort_values('rank').drop('id', axis = 1)



# method to decide How to rank the group of records that have the same value (i.e. ties):
# method 'dense', like ‘min’, but rank always increases by 1 between groups.