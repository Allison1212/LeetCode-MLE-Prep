import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # merge_df = pd.merge(customers,orders.rename(columns = {'id': 'orderId'}), left_on = 'id', right_on = 'customerId', how = 'left' )
    # return merge_df[merge_df['orderId'].isnull()][['name']].rename(columns = {'name': 'Customers'})
    
    #Better solution
    return customers[~customers['id'].isin(orders['customerId'])][['name']].rename(columns = {'name': 'Customers'})