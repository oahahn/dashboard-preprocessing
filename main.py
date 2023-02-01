import pandas as pd


def remove_columns(dataframe):
    """
    Removes all unnessary columns for Power BI dashboard
    :param dataframe: pandas dataframe
    :return: dataframe with dropped columns
    """
    drop_columns = dataframe.keys().tolist()
    drop_columns.remove('detection_time')
    drop_columns.remove('probability')
    drop_columns.remove('detection_count')
    drop_columns.remove('drone_lat')
    drop_columns.remove('drone_lon')
    drop_columns.remove('surveyID')
    drop_columns.remove('KML')
    drop_columns.remove('species_category')
    drop_columns.remove('species_name')
    return dataframe.drop(columns=drop_columns)


if __name__ == '__main__':
    det_match = pd.read_csv('det_match.csv')
    print(f'det match size before: {det_match.shape}')
    det_match = remove_columns(det_match)
    print(f'det match size after: {det_match.shape}')
