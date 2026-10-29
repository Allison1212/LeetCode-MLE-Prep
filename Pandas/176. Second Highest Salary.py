import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_s = np.sort(employee['salary'].unique())
    if len(unique_s) < 2:
        salary = None
    else:
        salary = unique_s[-2]
    return pd.DataFrame({'SecondHighestSalary':[salary]})