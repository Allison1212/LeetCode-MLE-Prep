import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    
    # better solution
    bull = files['content'].str.contains(' bull ',).sum()
    bear = files['content'].str.contains(' bear ').sum()

    res_df = pd.DataFrame({'word': ['bull','bear'],'count':[bull, bear]})

    return res_df

    # Gap: pandas dataframe 的创建方式

    
    # # mine: 仔细读题disregarding any instances where it appears without space on either side
    # files['bull'] = np.where(files['content'].str.contains(' bull ', regex = True),1,0)
    # files['bear'] = np.where(files['content'].str.contains(' bear ', regex = True),1,0)
    # bull_df = pd.DataFrame(files.agg({'bull':'sum'}),columns=['count'])
    # bull_df['word'] = 'bull'
    # bear_df = pd.DataFrame(files.agg({'bear':'sum'}),columns=['count'])
    # bear_df['word'] = 'bear'

    # conact_df = pd.concat([bull_df,bear_df])

    # return conact_df[['word','count']]