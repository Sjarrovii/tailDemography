import os


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
