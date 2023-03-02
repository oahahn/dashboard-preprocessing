import pandas as pd
import numpy as np
import os
from ast import literal_eval


def generate_kml_lookup(detections, survey_lookup, old_csvs, new_csvs):
    kml_matches = pd.read_csv(os.path.join(old_csvs, 'kml_matches.csv'))
    kml_lookup = pd.DataFrame({
        'filename': kml_matches['filename'],
        'flight_distance': kml_matches['flight_distance'],
        'flight_time (h)': kml_matches['flight_time (h)'],
        'kml_area (m^2)': kml_matches['kml_area(m^2)'],
        'date': kml_matches['detection_time'],
    })
    # Remove KML files that weren't flown
    kml_lookup = kml_lookup[kml_lookup['flight_time (h)'] != 0]
    # Create a primary key
    kml_lookup['kmlID'] = np.arange(1, len(kml_lookup) + 1)
    null_id = pd.DataFrame({'kmlID': 0, 'filename': np.nan, 'flight_distance': np.nan, 'flight_time (h)': np.nan,
                            'kml_area (m^2)': np.nan, 'date': np.nan}, index=[0])
    kml_lookup = pd.concat([null_id, kml_lookup], ignore_index=True)
    # Reorder the columns to have the primary key in the first position and export
    kml_lookup = kml_lookup[['kmlID', 'filename', 'flight_distance', 'flight_time (h)', 'kml_area (m^2)', 'date']]
    kml_lookup = associate_kmls_with_surveys(detections, survey_lookup, kml_lookup)
    kml_lookup['date'] = pd.to_datetime(kml_lookup['date']).dt.date
    kml_lookup.to_csv(os.path.join(new_csvs, 'kml_lookup.csv'), index=False)
    return detections, kml_lookup


def associate_kmls_with_surveys(detections, survey_lookup, kml_lookup):
    # Go through each KML file and associate a surveyID with it
    surveyID_list = []
    for kml_filename in kml_lookup['filename'].values:
        filename_key_not_found = True
        for idx, row in survey_lookup.iterrows():
            kml_list = row['KMLs']
            surveyID = row['surveyID']
            if isinstance(kml_list, list) and kml_filename in kml_list:
                surveyID_list.append(surveyID)
                filename_key_not_found = False
                break
        # If no surveyID was found, assign null
        if filename_key_not_found:
            surveyID_list.append(np.nan)
    kml_lookup['surveyID'] = surveyID_list

    # Fill in null values: look for kml_lookup surveyID keys which are null and try and find a key to fit the entry
    for idx, row in kml_lookup.iterrows():
        surveyID = row['surveyID']
        kml_filename = row['filename']
        if pd.isnull(surveyID) and pd.notnull(kml_filename):
            kml_lookup.at[idx, 'surveyID'] = get_surveyID_from_detections(detections, kml_filename)
    return kml_lookup


def get_surveyID_from_detections(detections, kml_filename):
    # Look through the detections database to associate a kml filename with a surveyID key
    for i, kml_matches in detections['kml_matches'].items():
        list_type = isinstance(kml_matches, str) and '[' in kml_matches
        # If the kml exists in the kml_matches list from detections, use this surveyID key
        if list_type and (kml_filename in literal_eval(kml_matches)):
            return detections.at[i, 'surveyID']
    # If none can be found, keep the entry null
    return np.nan
