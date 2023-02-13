import pandas as pd
import numpy as np
import os
from ast import literal_eval

OLD_DATABASE_DIRECTORY = './CSVs'
NEW_DATABASE_DIRECTORY = './databases'


def generate_airdata(kml_lookup):
    airdata_matches = pd.read_csv(os.path.join(OLD_DATABASE_DIRECTORY, 'airdata_matches.csv'))
    # Extract the relevant columns
    airdata = pd.DataFrame({
        'flight_start': airdata_matches['flight_start'],
        'flight_end': airdata_matches['flight_end'],
        'filename': airdata_matches['filename'],
        'air_seconds': airdata_matches['Air Seconds'],
        'kml_area': airdata_matches['kml_area'],
        'kml_matches': airdata_matches['kml_matches'],
        'video_length': airdata_matches['viedo_length'],
        'surveyID': airdata_matches['surveyID']
    })
    # Drop any entries which start and end at the same time on the same date to ensure unique entries
    airdata = airdata.drop_duplicates(subset=['flight_start', 'flight_end'])
    airdata = airdata.drop(columns=['flight_start', 'flight_end'])
    # Create a primary key
    airdata['airdataID'] = np.arange(len(airdata))
    # Reorder the columns to have the primary key in the first position and export
    airdata = airdata[['airdataID', 'filename', 'air_seconds', 'video_length', 'kml_area',
                                     'kml_matches', 'surveyID']]
    airdata = remove_bad_formatting(airdata)
    airdata = add_kml_key(airdata, kml_lookup)
    airdata.to_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'airdata.csv'), index=False)


def remove_bad_formatting(airdata):
    """Removes entries where the kml filename has a strange format with index"""
    for idx, kml_matches_list in airdata['kml_matches'].items():
        if isinstance(kml_matches_list, str) and '[' in kml_matches_list:
            airdata.at[idx, 'kml_matches'] = literal_eval(kml_matches_list)
        elif isinstance(kml_matches_list, str):
            airdata.at[idx, 'kml_matches'] = [kml_matches_list]
    return airdata


def add_kml_key(airdata, kml_lookup):
    """Replaces the kml filename lists with the kml keys from the kml_lookup table"""
    kmlIDs = []
    na_index = kml_lookup.index[kml_lookup['filename'].isna()][0]
    kml_filename_list = kml_lookup['filename'].to_list()
    for idx, kml_matches_list in airdata['kml_matches'].items():
        # Check if the first kml file listed has a key
        if isinstance(kml_matches_list, list):
            # Look through list of filenames to try associate a kml key with the list
            filename_key_not_found = True
            for kml_filename in kml_matches_list:
                if kml_filename in kml_filename_list:
                    kml_idx = kml_filename_list.index(kml_filename)
                    kmlIDs.append(kml_lookup.at[kml_idx, 'kmlID'])
                    filename_key_not_found = False
                    break
            if filename_key_not_found:
                # If the kml filename doesn't have a key in the kml_lookup table, assign it the na key
                kmlIDs.append(na_index)
        else:
            # If this entry is not a list, assign it the na key
            kmlIDs.append(na_index)
    airdata['kmlID'] = kmlIDs
    airdata = airdata.drop(columns='kml_matches')
    return airdata
