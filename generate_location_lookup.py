import pandas as pd
import os


def generate_location_lookup(old_csvs, new_csvs):
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
    location_lookup.to_csv(os.path.join(new_csvs, 'location_lookup.csv'), index=False)
