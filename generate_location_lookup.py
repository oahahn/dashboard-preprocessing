import pandas as pd
import os


def generate_location_lookup(old_csvs, new_csvs, survey_lookup):
    location_dataframe = pd.read_csv(os.path.join(old_csvs, 'location_dataframe.csv'))
    location_lookup = pd.DataFrame({
        'location_id': location_dataframe['location_id'],
        'lat_min': location_dataframe['lat_min'],
        'lat_max': location_dataframe['lat_max'],
        'lon_min': location_dataframe['lon_min'],
        'lon_max': location_dataframe['lon_max'],
        'area': location_dataframe['area']
    })

    location_lookup['lat_avg'] = (location_lookup['lat_min'] + location_lookup['lat_max']) / 2
    location_lookup['lon_avg'] = (location_lookup['lon_min'] + location_lookup['lon_max']) / 2
    # Add in the survey ID key to the location database
    # location_lookup = pd.merge(location_lookup, survey_lookup[['surveyID', 'location_id']], on='location_id',
    #                       validate='one_to_many')
    # location_lookup.to_csv(os.path.join(new_csvs, 'location_lookup.csv'), index=False)
    survey_lookup = pd.merge(left=survey_lookup, right=location_lookup, on='location_id', validate='many_to_one')
    survey_lookup, null_location_ids = remove_null_rows(survey_lookup)
    survey_lookup.to_csv(os.path.join(new_csvs, 'survey_lookup.csv'), index=False)
    return null_location_ids


def remove_null_rows(survey_lookup):
    # Drops rows where coordinates are null i.e. the location has not been flown
    rows_to_drop = []
    null_location_ids = []
    for idx, row in survey_lookup.iterrows():
        lat_lon_null = pd.isnull(row['lat_min']) and pd.isnull(row['lon_min'])
        if lat_lon_null:
            rows_to_drop.append(idx)
            null_location_ids.append(row['location_id'])
    return survey_lookup.drop(index=rows_to_drop), null_location_ids
