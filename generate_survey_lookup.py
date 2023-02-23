import pandas as pd
import numpy as np
import os
from ast import literal_eval
from generate_airdata import add_kml_key


def generate_survey_lookup(old_csvs, new_csvs):
    survey_match = pd.read_csv(os.path.join(old_csvs, 'survey_match.csv'))
    # Filter relevant columns
    survey_lookup = pd.DataFrame({
        'surveyID': survey_match['surveyID'],
        'KMLs': survey_match['KMLs'],
        'pilot': survey_match['pilot'],
        'client': survey_match['client'],
        'mission': survey_match['mission'],
        'video_length (s)': survey_match['video_length(s)'],
    })
    # Drop duplicate surveyID entries
    survey_lookup = survey_lookup.drop_duplicates(subset=['surveyID'])
    survey_lookup = clean_kml_column(survey_lookup)
    # survey_lookup = add_kml_key(survey_lookup, 'KMLs', kml_lookup)
    survey_lookup = remove_null_rows(survey_lookup)
    survey_lookup.to_csv(os.path.join(new_csvs, 'survey_lookup.csv'), index=False)
    return survey_lookup


def clean_kml_column(survey_lookup):
    for idx, kml_matches_list in survey_lookup['KMLs'].items():
        if isinstance(kml_matches_list, str) and '[' in kml_matches_list:
            survey_lookup.at[idx, 'KMLs'] = literal_eval(kml_matches_list)
        elif (kml_matches_list == "['']") or (kml_matches_list == "no_det"):
            survey_lookup.at[idx, 'KMLs'] = np.nan
        elif isinstance(kml_matches_list, str):
            survey_lookup.at[idx, 'KMLs'] = [kml_matches_list]
    return survey_lookup


def remove_null_rows(survey_lookup):
    # Drops rows where mission is labelled '?'
    rows_to_drop = []
    for idx, mission in survey_lookup['mission'].items():
        if mission == '?':
            rows_to_drop.append(idx)

    return survey_lookup.drop(index=rows_to_drop)
