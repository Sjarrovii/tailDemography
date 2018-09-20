import pandas as pd


def mindate(x, sort_criteria=['species', 'toes', 'sex']):
    """
    takes a pandas data frame and returns a dataframe with sorting criteria adds a column containing the earliest date
    at which each unique combination of the sort criteria was sighted. [Requires that the source dataframe,x, has a
    column labeled 'date'.]
    """
    if any(x.columns == 'initialCaptureDate'):
        x = x['n_val_data'].drop('initialCaptureDate',1)
    sortable_min_date =pd.DataFrame(x.groupby(sort_criteria).date.min()).\
        rename(index=str, columns={'date': 'initialCaptureDate'}).reset_index()
    x = x.merge(sortable_min_date, how='left', on=sort_criteria)
    x['year_diff'] = x.date.dt.year - x.initialCaptureDate.dt.year
    return x
