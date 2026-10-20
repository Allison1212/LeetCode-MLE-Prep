import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # tweets['length'] = tweets["content"].apply(lambda x: len(x))
    # return tweets[tweets['length']>15][['tweet_id']]

    return tweets[tweets['content'].str.len() > 15][['tweet_id']]

# .str.len() is used to get the length of each string