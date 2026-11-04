import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    
    merge_df = students.merge(subjects, how='cross')
    groupby_df = examinations.groupby(['student_id','subject_name'], as_index = False).agg(attended_exams = ('subject_name','size'))
    res = merge_df.merge(groupby_df, on = ['student_id','subject_name'], how = 'left').astype({'attended_exams': int}).fillna({'attended_exams':0}).sort_values(['student_id','subject_name'])

    return res

    # 'cross' get all possible combination