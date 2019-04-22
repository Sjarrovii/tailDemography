import pandas as pd
import numpy as np


def label_pattern(x, pat_num, pattern, pat_col='toe_pattern', col='toes'):
    """searches a pandas series for a regex expression, pattern, and replaces with replacement"""
    # To-Do needs to capture when an entry fits multiple patterns and which patterns those are
    try:
        x.loc[(x[col].str.match(pattern)) & (x[pat_col].isnull()), pat_col] = str(pat_num)
    except Exception as e:
        logging.error("No values in f'{col} match f'{pattern} where f'{pat_col} is null")
    return x


def make_str(x):
    assert isinstance(x, pd.Series)
    # convert series to string
    x = x.astype(str)
    # create an index of single-digit numbers
    idx = x.str.len() < 2
    # add a zero to the beginning of those single-digit numbers
    x.loc[idx] = '0' + x.loc[idx]
    return x


def replace_pattern(x, pattern_b, replacement):
    """searches a pandas series for a regex expression, pattern, and replaces with replacement"""

    try:
        res = x.strip().replace(pattern_b, replacement)
    except "This doesn't work":
        res = x
        # insert logging
    return res


def report_pattern(x, pattern, col, return_type):
    """searches a pandas series for a regex expression, pattern, and replaces with replacement"""

    res = '{}:\ntoe pattern {}:{}'.format(return_type, str(pattern), (x[col].str.match(pattern) is True).sum())

    return res
