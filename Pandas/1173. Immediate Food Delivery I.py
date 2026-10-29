import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    delivery['immediate'] = np.where(delivery['order_date'] == delivery['customer_pref_delivery_date'], 1, 0)

    return pd.DataFrame({'immediate_percentage':[np.round(delivery['immediate'].mean()*100,2)]})

    # 可以不需要numpy
        immediate = (
        delivery['order_date'] == delivery['customer_pref_delivery_date']
    ) # boolean series 

    return pd.DataFrame({
        'immediate_percentage': [round(immediate.mean() * 100, 2)]
    })