"""
Write a solution to calculate and display the number of rows and columns of players.

Return the result as an array:

[number of rows, number of columns]
"""

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:

    return ([len(players), len(players.columns)])

    