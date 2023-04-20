import pandas as pd
import os


def generate_mission_lookup(survey_lookup, new_csvs):
    mission_lookup = pd.DataFrame({
        'location_id': survey_lookup['location_id'],
        'mission': survey_lookup['mission']
    })
    mission_lookup = mission_lookup.drop_duplicates(subset='location_id')
    mission_lookup = remove_null_rows(mission_lookup)
    mission_lookup.to_csv(os.path.join(new_csvs, 'mission_lookup.csv'), index=False, inplace=True)


def remove_null_rows(mission_lookup):
    # Drops rows where the location id is null
    rows_to_drop = []
    for idx, row in mission_lookup.iterrows():
        if pd.isnull(row['location_id']):
            rows_to_drop.append(idx)
    return mission_lookup.drop(index=rows_to_drop)
