import pandas as pd
import re

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # return patients[patients['conditions'].str.contains('(?:^DIAB1| DIAB1)')]
    return patients[patients['conditions'].str.contains('(?:^| )DIAB1')]