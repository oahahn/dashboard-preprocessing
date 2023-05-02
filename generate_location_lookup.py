import pandas as pd
import os


def generate_location_lookup(old_csvs, new_csvs, survey_lookup):
    location_dataframe = pd.read_csv(os.path.join(old_csvs, 'location_dataframe.csv'))
    location_lookup = pd.DataFrame({
        'location_id': location_dataframe['location_id'],
        'lat': location_dataframe['lat'],
        'lon': location_dataframe['lon'],
        'area': location_dataframe['area'],
        'lga': location_dataframe['lga']
    })

    survey_lookup = pd.merge(left=survey_lookup, right=location_lookup, on='location_id', validate='many_to_one')
    survey_lookup = remove_null_rows(survey_lookup)
    survey_lookup = remove_geographic_outliers(survey_lookup)
    survey_lookup.to_csv(os.path.join(new_csvs, 'survey_lookup.csv'), index=False)


def remove_null_rows(survey_lookup):
    # Drops rows where coordinates are null i.e. the location has not been flown
    rows_to_drop = []
    for idx, row in survey_lookup.iterrows():
        lat_lon_null = pd.isnull(row['lat']) and pd.isnull(row['lon'])
        lat_lon_zero = (row['lat'] == 0) and (row['lon'] == 0)
        if lat_lon_null or lat_lon_zero:
            rows_to_drop.append(idx)
    return survey_lookup.drop(index=rows_to_drop)


def remove_geographic_outliers(survey_lookup):
    # Cycle through the latitude and longitude columns and search for coordinates outside NSW
    remove_indices = []
    for idx, row in survey_lookup.iterrows():
        latitude_outside_nsw = (row['lat'] < -37.505768) or (row['lat'] > -28.156804)
        longitude_outside_nsw = (row['lon'] < 140.993300) or (row['lon'] > 153.638805)
        if latitude_outside_nsw or longitude_outside_nsw:
            remove_indices.append(idx)

    # Remove vague detections
    return survey_lookup.drop(index=remove_indices)