import pandas as pd
import os
import numpy as np
from ast import literal_eval


def generate_video_lookup(old_csvs, new_csvs, kml_lookup):
    video_matches = pd.read_csv(os.path.join(old_csvs, 'video_matches.csv'))

    video_lookup = pd.DataFrame({
        'date': pd.to_datetime(video_matches['creation_time']).dt.date,
        'file_size': video_matches['file_size'],
        'duration': video_matches['duration'],
        'flight_distance': video_matches['flight_distance'],
        'KMLs': video_matches['kml_matches'],
        'client': video_matches['client'],
        'mission': video_matches['mission'],
        'surveyID': video_matches['surveyID']
    })
    video_lookup = clean_kml_column(video_lookup)
    video_lookup = add_kml_key(video_lookup, kml_lookup)
    video_lookup.to_csv(os.path.join(new_csvs, 'video_lookup.csv'), index=False)


def clean_kml_column(video_lookup):
    for idx, kml_matches_list in video_lookup['KMLs'].items():
        if isinstance(kml_matches_list, str) and '[' in kml_matches_list:
            video_lookup.at[idx, 'KMLs'] = literal_eval(kml_matches_list)[0]
        elif (kml_matches_list == "['']") or (kml_matches_list == "no_det"):
            video_lookup.at[idx, 'KMLs'] = np.nan
    return video_lookup


def add_kml_key(video_lookup, kml_lookup):
    # Add in the KML ID key to the video lookup database
    kml_lookup_to_merge = kml_lookup[['kmlID', 'filename']]
    video_lookup = pd.merge(video_lookup, kml_lookup_to_merge, left_on='KMLs', right_on='filename',
                            validate='many_to_one')
    # Remove species category and species name from detections database
    video_lookup = video_lookup.drop(columns=['KMLs', 'filename'])
    return video_lookup
