import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = np.where(((employees['employee_id']%2 == 1) & (~employees['name'].str.startswith('M'))),employees['salary'],0)
    return employees[['employee_id','bonus']].sort_values('employee_id')



    # .str.startswith('X') is used to check if the name starts with 'X'