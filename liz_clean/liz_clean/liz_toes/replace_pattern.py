def replace_pattern(x, pattern, pattern_b, source_col, replacement):
    """searches a pandas series for a regex expression, pattern, and replaces with replacement"""

    return x.loc[x[source_col].str.match(pattern)==True, source_col].str.replace(pattern_b, replacement)
