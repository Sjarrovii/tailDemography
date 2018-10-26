# To-Do needs to capture when an entry fits multiple patterns and which patterns those are


def label_pattern(x, pat_num, pattern, pat_col='toe_pattern', col='toes'):
    """searches a pandas series for a regex expression, pattern, and replaces with replacement"""

    x.loc[(x[col].str.match(pattern) == True) & (x[pat_col].isnull()), pat_col] = str(pat_num)
    return x
