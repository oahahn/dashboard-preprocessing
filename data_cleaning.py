import pandas as pd
import maps


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


def string_format(dataframe, column):
    dataframe[column] = dataframe[column].str.strip()
    dataframe[column] = dataframe[column].str.title()
    dataframe[column] = dataframe[column].str.replace('_', ' ')
    return dataframe


def standardise_species_name(dataframe):
    # Strip text and format
    det_match['species_name'] = det_match['species_name'].str.strip()
    det_match['species_name'] = det_match['species_name'].str.title()
    det_match['species_name'] = det_match['species_name'].str.replace('_', ' ')

    remove_indices = []
    for idx, name in dataframe['species_name'].items():
        if (name in maps.to_remove):
            remove_indices.append(idx)
            continue
        for correct_name, alias_list in maps.species_name_map.items():
            if (name in alias_list):
                dataframe.at[idx, 'species_name'] = correct_name
                break
    return dataframe.drop(index=remove_indices)


if __name__ == '__main__':
    det_match = pd.read_csv('det_match.csv')
    det_match = remove_columns(det_match)
    det_match = standardise_species_name(det_match)

    print(len(det_match['species_name'].unique()))
