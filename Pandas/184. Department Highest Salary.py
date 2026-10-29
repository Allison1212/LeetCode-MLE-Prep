import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # emp_dept = department.rename(columns = {'id':'departmentId','name':'Department'}).merge(employee, on = 'departmentId').groupby('departmentId').agg(Department=('Department','first'), Salary=('salary','max')).reset_index()
    # merge_df = emp_dept.merge(employee, on = 'departmentId').rename(columns = {'name':'Employee'})
    # return merge_df[merge_df['salary'] == merge_df['Salary']][['Department','Employee','Salary']]

    employee['max_salary'] = employee.groupby('departmentId')['salary'].transform('max')

    result = employee[employee['salary'] == employee['max_salary']]

    result = result.merge(
        department,
        left_on='departmentId',
        right_on='id'
    )

    return result.rename(columns={
        'name_x': 'Employee',
        'name_y': 'Department',
        'salary': 'Salary'
    })[['Department', 'Employee', 'Salary']]

    # agg('max') → Returns one value per group, reducing the number of rows.
    # transform('max') → Returns a value for every original row, preserving the original number of rows.