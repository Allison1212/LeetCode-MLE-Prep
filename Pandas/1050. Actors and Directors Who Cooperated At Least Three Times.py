import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:

    res = actor_director.groupby(['actor_id','director_id'],as_index = False)['timestamp'].count()

    return res[res['timestamp']>=3][['actor_id','director_id']]
    # .count()	非 NULL 值数量
    # .size()	所有行数，包括 NULL