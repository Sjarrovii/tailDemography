import pandas as pd


def smallest(x, svlGroup = ['species', 'toes', 'sex', 'initialCaptureDate']):
    """finds svl of animal at date of the initial capture."""
    # To-Do:  Make 'sortable_smallest_svl' into local variable
    if any(x.columns == 'smallest_svl'):
        x = x.drop('smallest_svl', 1)
    sortable_smallest_svl = x.groupby(svlGroup).svl.min().reset_index()\
        .rename(index=str, columns={'svl': 'smallest_svl'})
    # sortable_smallest_svl
    x = x.merge(sortable_smallest_svl, how='left', on=svlGroup)
    x['svl_diff'] = x.svl - x.smallest_svl
    return x
