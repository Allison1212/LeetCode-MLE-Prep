import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    res = orders.groupby('customer_number',as_index = False).agg(nbr_orders = ('order_number','count'))
    
    # Return 所有customer that with largest order
    return res[res['nbr_orders'] == res['nbr_orders'].max()][['customer_number']]

    # Return 第一个customer that with largest order
    return res.loc[[res['nbr_orders'].idxmax()], ['customer_number']]
    