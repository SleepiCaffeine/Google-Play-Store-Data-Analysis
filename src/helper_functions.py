import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
def drop_col_pd(dataset, column_arr):

    dataset.drop(column_arr, axis=1, inplace=True)
    dataset.dropna(axis=0, how='any')
    return dataset

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
def is_eng(app_series):
    
    df = []
    for app_name in app_series:
        ASCII = 0
        for character in str(app_name):
            if (ord(character) > 127):
                ASCII +=1
                
        if (ASCII >= 4):
            df.append(False)
    
        else:
            df.append(True)
            
    return df

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
def frequency(genre_series):

    table = {}
    size = 0
    for genre in genre_series:
        size += 1
        
        if genre in table:
            table[genre] += 1
        else:
            table[genre] = 1
            
    p_table = {}
    
    for x in table:
        p_table[x] = (table[x]/size)*100
        
    return p_table
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

def f_table(genre_series):

    table = frequency(genre_series)
    display = {}
    for key in table:
        display[key] = table[key]
        
    keys=list(display.keys())
    values=list(display.values())
    sort_val = np.argsort(values)
    
    return {keys[i]: values[i] for i in sort_val} # Ty GeeksForGeeks
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 