import pandas as pd
import numpy as np
import os

OLD_DATABASE_DIRECTORY = './CSVs'
NEW_DATABASE_DIRECTORY = './databases'


def generate_kml_lookup(detections):
    kml_matches = pd.read_csv(os.path.join(OLD_DATABASE_DIRECTORY, 'kml_matches.csv'))
    kml_lookup = kml_matches[['filename', 'flight_distance', 'flight_time (h)']]
    # Remove KML files that weren't flown
    kml_lookup = kml_lookup[kml_lookup['flight_time (h)'] != 0]
    # Create a primary key
    kml_lookup['kmlID'] = np.arange(1, len(kml_lookup) + 1)
    null_id = pd.DataFrame({'kmlID': 0, 'filename': np.nan, 'flight_distance': np.nan, 'flight_time (h)': np.nan},
                           index=[0])
    kml_lookup = pd.concat([null_id, kml_lookup], ignore_index=True)
    # Reorder the columns to have the primary key in the first position and export
    kml_lookup = kml_lookup[['kmlID', 'filename', 'flight_distance', 'flight_time (h)']]
    kml_lookup.to_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'kml_lookup.csv'), index=False)
    detections = add_kml_key_to_detections(detections, kml_lookup)
    return detections, kml_lookup


def add_kml_key_to_detections(detections, kml_lookup):
    # Add in the KML ID key to the original detections database
    detections = pd.merge(detections, kml_lookup, left_on='KML', right_on='filename', validate='many_to_one')
    # Remove species category and species name from detections database
    detections = detections.drop(columns=['KML', 'filename', 'flight_distance', 'flight_time (h)'])
    return detections
