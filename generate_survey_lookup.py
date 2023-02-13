import pandas as pd
import numpy as np
import os
from ast import literal_eval
from generate_airdata import add_kml_key

OLD_DATABASE_DIRECTORY = './CSVs'
NEW_DATABASE_DIRECTORY = './databases'


def generate_survey_lookup(kml_lookup):
    survey_match = pd.read_csv(os.path.join(OLD_DATABASE_DIRECTORY, 'survey_match.csv'))
    # Filter relevant columns
    survey_lookup = survey_match[['surveyID', 'KMLs', 'pilot', 'client', 'mission']]
    # Drop duplicate surveyID entries
    survey_lookup = survey_lookup.drop_duplicates(subset=['surveyID'])
    survey_lookup = clean_kml_column(survey_lookup)
    survey_lookup = add_kml_key(survey_lookup, 'KMLs', kml_lookup)
    survey_lookup.to_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'survey_lookup.csv'), index=False)


def clean_kml_column(survey_lookup):
    for idx, kml_matches_list in survey_lookup['KMLs'].items():
        if isinstance(kml_matches_list, str) and '[' in kml_matches_list:
            survey_lookup.at[idx, 'KMLs'] = literal_eval(kml_matches_list)
        elif (kml_matches_list == "['']") or (kml_matches_list == "no_det"):
            survey_lookup.at[idx, 'KMLs'] = np.nan
        elif isinstance(kml_matches_list, str):
            survey_lookup.at[idx, 'KMLs'] = [kml_matches_list]
    return survey_lookup
