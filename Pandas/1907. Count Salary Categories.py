import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['category'] = np.where(accounts['income'] < 20000, 'Low Salary', np.where(accounts['income'] > 50000, 'High Salary','Average Salary'))
    result = accounts.groupby('category').agg(accounts_count = ('account_id','count'))
    return result.reindex(
        ['Low Salary', 'Average Salary', 'High Salary'],
        fill_value=0
    ).reset_index()


    # .reindex(new_index, fill_value=0)
    # Conform DataFrame to new index with optional filling logic.
    
    