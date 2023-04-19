import pandas as pd
import os
import numpy as np


def generate_individual_databases(new_csvs, detections, survey_lookup):
    detections_only = detections[['detection_time', 'detection_count', 'speciesID']]
    detections_only['detection_time'] = pd.to_datetime(detections_only['detection_time']).dt.date
    detections_only.to_csv(os.path.join(new_csvs, 'detections_only.csv'), index=False)

    pilot_lookup = pd.DataFrame({'pilot': survey_lookup['pilot']})
    pilot_lookup = pilot_lookup.dropna()
    pilot_lookup = pilot_lookup.drop_duplicates()
    pilot_lookup['pilotID'] = np.arange(len(pilot_lookup))
    pilot_lookup.to_csv(os.path.join(new_csvs, 'pilot_lookup.csv'), index=False)
