import pandas as pd


def validate(x, sort_criteria=['species', 'toes', 'sex'], validation=['date', 'svl']):
    x['tmp'] = 1
    numbers = x.loc[(x.year_diff <= 7) & (x.svl_diff >= -2), :].\
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
