import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads['Clicked'] = np.where(ads['action'] == 'Clicked',1,0)
    ads['Viewed'] = np.where(ads['action'] == 'Viewed',1,0)

    ads_groups = ads.groupby('ad_id').agg(total_click = ('Clicked','sum'),
                                        total_view = ('Viewed','sum'),
    ).reset_index()
    ads_groups['ctr'] = round((ads_groups['total_click']/ (ads_groups['total_click'] + ads_groups['total_view'])) * 100,2)
    return ads_groups[['ad_id','ctr']].fillna(0).sort_values(by=['ctr', 'ad_id'], ascending=[False, True])


# optimal 的写法， 不需要manual创建两个column
# 用.value_counts()
# 然后unstack
# reindex 保证category不存在也会有一列
def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    counts = (
        ads.groupby('ad_id')['action']
        .value_counts()
        .unstack(fill_value=0)
    )

    # 确保 Clicked 和 Viewed 两列都存在
    counts = counts.reindex(
        columns=['Clicked', 'Viewed'],
        fill_value=0
    )

    counts['ctr'] = (
        counts['Clicked'] /
        (counts['Clicked'] + counts['Viewed']) * 100
    ).fillna(0).round(2)

    return (
        counts[['ctr']]
        .reset_index()
        .sort_values(['ctr', 'ad_id'], ascending=[False, True])
    )