import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    sale_com = sales_person.merge(orders.merge(company, on = 'com_id', how = 'left').rename(columns = {'name':'com_name'}), on = 'sales_id', how = 'left')

    # 不需要np.where
    sale_com['is_red'] = sale_com['com_name'] == 'RED'

    res = sale_com.groupby(
        ['sales_id', 'name'], as_index=False
    )['is_red'].any()
    # sale_com['is_red'] = np.where(sale_com['com_name'] == 'RED',1,0)
    # res = sale_com.groupby('name',as_index = False)['is_red'].sum()
    return res[res['is_red'] == False][['name']]

    #.groupby() with .any() allows you to check if at least one value in a group evaluates to True.


