import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    res= employee.groupby('managerId', as_index = False).agg(nbr_reporters = ('id','nunique'))
    merge = employee.merge(res, left_on = 'id', right_on = 'managerId', how = 'inner')
    return merge[merge['nbr_reporters'] >= 5][['name']]

    # id 是primary key 所以可以不去重， 用.size 也可以


