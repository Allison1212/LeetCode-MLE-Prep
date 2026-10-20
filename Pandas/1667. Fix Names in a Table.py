import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    # users['name'] = users['name'].apply(lambda x: x.lower()[0].upper() + x.lower()[1:])
    users['name'] = users['name'].str.capitalize()

    return users.sort_values('user_id')

    # .str.capitalize() can directory upper the first char and lower the remaining