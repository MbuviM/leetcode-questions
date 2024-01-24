"""
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+
Write a solution to correct the errors:

The grade column is stored as floats, convert it to integers.

The result format is in the following example.

Example 1:
Input:
DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
Output:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
+------------+------+-----+-------+
"""
"""
N.B:  If you have a dataframe with all object columns for instance 
and you want pandas to infer the best dtype, then convert_dtypes is handy. 
If you want to cast a given column to another dtype, go with astype
"""
import pandas as pd

# convert_dtypes() method is used to convert data types
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:

    students['grade'] = students['grade'].convert_dtypes(convert_integer=True)

    #astype() can also be used
    students['grade'] = students['grade'].astype(int)

    return students
    
