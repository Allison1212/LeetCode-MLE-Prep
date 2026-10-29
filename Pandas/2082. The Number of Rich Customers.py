import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'rich_count':[store[store['amount']> 500]['customer_id'].nunique()]})


    # .unique(): list unique values
    # .nunique(): return the count of unique value