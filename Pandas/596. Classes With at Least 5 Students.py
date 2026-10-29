import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    res = courses.groupby('class', as_index = False)['student'].count()
    return res[res['student'] >=5][['class']]
    
    #需要考虑学生会不会重复，如果会重复要考虑nunique
    