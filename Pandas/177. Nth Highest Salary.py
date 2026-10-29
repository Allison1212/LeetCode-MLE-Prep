import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N > len(employee['salary'].unique()) or N < 1:
        return pd.DataFrame({'salary': [None]}).rename(columns = {'salary': f"getNthHighestSalary({N})"})
    else:
        value = np.sort(employee['salary'].unique())[-N]
        return pd.DataFrame({'salary': [value]}).rename(columns = {'salary': f"getNthHighestSalary({N})"})
 