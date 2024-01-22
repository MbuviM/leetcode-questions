"""
DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
There are some duplicate rows in the DataFrame based on the email column.

Write a solution to remove these duplicate rows and keep only the first occurrence.
"""

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    drop_duplicates() method is used to drop the duplicates with keep showing the occurence that should 
    remain and inplace ensures no copy of the dataset is created after the changes. 
    subset is the column of reference.
    """
    drop_duplicates = customers.drop_duplicates(subset='email', keep='first', inplace=True)

    return customers