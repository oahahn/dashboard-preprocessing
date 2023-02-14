import pandas as pd
from data_cleaning import clean_data
from generate_species_lookup import generate_species_lookup
from generate_kml_lookup import generate_kml_lookup
from generate_airdata import generate_airdata
from generate_survey_lookup import generate_survey_lookup
import os

OLD_DATABASE_DIRECTORY = './CSVs'
NEW_DATABASE_DIRECTORY = './databases'


if __name__ == '__main__':
    det_match = pd.read_csv(os.path.join(OLD_DATABASE_DIRECTORY, 'det_match.csv'))
    detections = clean_data(det_match)
    detections, species_lookup = generate_species_lookup(detections)
    detections, kml_lookup = generate_kml_lookup(detections)
    generate_airdata(kml_lookup)
    generate_survey_lookup(kml_lookup)
    detections.to_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'detections.csv'), index=False)
