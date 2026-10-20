import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$"

    # users['valid'] = users['mail'].apply(lambda x: re.search(pattern,x))
    # return users[~users['valid'].isnull()].drop(columns=['valid'])

    return users[users['mail'].str.fullmatch(pattern)]

    #. 是一个特殊字符（metacharacter），不是普通的句号
    #. → Matches any single character（除了换行符，默认情况下）
    # \. → Matches a literal dot (.)
    # pandas regex match: .str.fullmatch(pattern)

    