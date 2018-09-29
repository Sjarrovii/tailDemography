import pandas as pd


def make_str(x):
    assert isinstance(x, pd.Series)
    # convert series to string
    x = x.astype(str)
    # create an index of single-digit numbers
    idx = x.str.len()<2
    # add a zero to the beginning of those single-digit numbers
    x.loc[idx] = '0' + x.loc[idx]
    return x