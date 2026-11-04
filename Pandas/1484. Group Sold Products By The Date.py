import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.drop_duplicates().sort_values('product').groupby('sell_date', as_index = False).agg(num_sold = ('product','nunique'),products = ('product',','.join) )