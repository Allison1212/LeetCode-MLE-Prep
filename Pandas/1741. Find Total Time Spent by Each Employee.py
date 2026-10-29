import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.groupby(['event_day','emp_id']).apply(lambda x: (x['out_time'] - x['in_time']).sum()).reset_index(name='total_time').rename(columns = {'event_day':'day'}).sort_values('day')

    # Another simple way
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees.groupby(['event_day','emp_id'], as_index = False)['total_time'].sum().rename(columns = {'event_day':'day'}).sort_values('day')

    