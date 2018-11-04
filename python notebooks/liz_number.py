import os
import pandas as pd


def validate(x, sort_criteria=['species', 'toes', 'sex'], validation=['date', 'svl']):
    x['tmp'] = 1
    numbers = x.loc[(x.year_diff <= 7) & (x.svl_diff >= -2), :]. \
        groupby(['species', 'sex', 'toes']).tmp.min().cumsum().reset_index()
    validated = x.loc[(x.year_diff <= 7) & (x.svl_diff >= -2), :].shape[0]
    not_val_data = x.loc[(x.year_diff <= 7) & (x.svl_diff >= -2), :]
    not_validated = x.loc[~((x.year_diff <= 7) & (x.svl_diff >= -2)), :].shape[0]
    numbers = numbers.rename(columns={'tmp': 'liznumber'})  # rename last column to liznumber
    # the next line merges the numbers to the original data frame to assign the lizard number to the full record
    # of an animal.  It then drop 'tmp'and 'smallest_svl, since we won't be using these again
    x = x.merge(numbers, 'left', on=['species', 'sex', 'toes']).drop(['tmp', 'smallest_svl'], 1)
    print("\nOf those entries we can handle, there are {} individuals as defined by {} which pass validation based\
    on {} and {} which do not pass validation.".format(validated, sort_criteria, validation, not_validated))
    return {'val_data': x, 'n_val_data': not_val_data, 'n_validated': not_validated}


def smallest(x, svlGroup =['species', 'toes', 'sex', 'initialCaptureDate']):
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

def mindate(x, sort_criteria = ['species', 'toes', 'sex']):
    """
    takes a pandas data frame and returns a dataframe with sorting criteria adds a column containing the earliest date
    at which each unique combination of the sort criteria was sighted. [Requires that the source dataframe,x, has a
    column labeled 'date'.]
    """
    if any(x.columns == 'initialCaptureDate'):
        x = x.drop('initialCaptureDate',1)
    sortable_min_date =pd.DataFrame(x.groupby(sort_criteria).date.min()).\
        rename(index=str, columns={'date': 'initialCaptureDate'}).reset_index()
    x = x.merge(sortable_min_date, how='left', on=sort_criteria)
    x['year_diff'] = x.date.dt.year - x.initialCaptureDate.dt.year
    return x

def lizsort(x, path: str, sort_criteria = ['species', 'toes', 'sex'], validation = ['date', 'svl'],\
            unsortablefile='unsortable.csv'):
    """
    takes a pandas data frame and returns a pandas dataframe with only those values which
    can be evaluated according to given criteria and prints a summaryof the files evaluated
    :param path:
    :param sortCriteria:
    :param validation:
    :param unsortablefile:
    """
    # identify lizards with sufficient data to evaluate
    # report on those without sufficient data and save them to a file for later evaluation
    critical = sort_criteria + validation
    unsortable = x.loc[x.loc[:, critical].isnull().any(axis=1)]
    sortable = x.loc[x.loc[:, critical].notnull().all(axis=1)]
    os.chdir(path)
    unsortable.to_csv(unsortablefile)
    print("\nThere were {} entries for which values for one of the critical criteria, ({}), were null.  \
    These entries could not be evaluated and were written out to the file {} for evaluation."\
          .format(unsortable.shape[0], critical, unsortablefile))
    return sortable