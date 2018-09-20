import pandas as pd

def mindate(x, sortCriteria = ['species','toes', 'sex']): # finds date of the initial capture of an animal
    """
    takes a pandas data frame and returns a dataframe with sorting criteria adds a column containing the earliest date
    at which each unique combination of the sort criteria was sighted. [Requires that the source dataframe,x, has a
    column labeled 'date'.]
    """
    if any(x.columns=='initialCaptureDate'):
        x = tmp_sort['n_val_data'].drop('initialCaptureDate',1)
    sortable_min_date =pd.DataFrame(x.groupby(sortCriteria).date.min()).\
    rename(index = str, columns= {'date':'initialCaptureDate'}).reset_index()
    x = x.merge(sortable_min_date,how = 'left', on = sortCriteria)
    x['year_diff'] = x.date.dt.year - x.initialCaptureDate.dt.year
    return x
