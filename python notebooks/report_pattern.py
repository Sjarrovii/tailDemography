def report_pattern(x, pattern, col, return_type):
    """searches a pandas series for a regex expression, pattern, and replaces with replacement"""

    res = '{}:\ntoe pattern {}:{}'.format(return_type, str(pattern), (x[col].str.match(pattern)==True).sum())

    return res
