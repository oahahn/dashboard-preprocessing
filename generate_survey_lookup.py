import pandas as pd
import numpy as np
import os
from ast import literal_eval
import time


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
        'date': survey_match['survey_start']
    })
    # Drop duplicate surveyID entries
    survey_lookup = survey_lookup.drop_duplicates(subset=['surveyID'])
    survey_lookup = clean_kml_column(survey_lookup)
    # survey_lookup = add_kml_key(survey_lookup, 'KMLs', kml_lookup)
    survey_lookup = remove_null_rows(survey_lookup)
    survey_lookup['date'] = pd.to_datetime(survey_lookup['date']).dt.date
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
    """Drops rows where mission is labelled '?'"""
    rows_to_drop = []
    for idx, mission in survey_lookup['mission'].items():
        if mission == '?':
            rows_to_drop.append(idx)

    return survey_lookup.drop(index=rows_to_drop)


def fill_in_dates(survey_lookup):
    min_date = pd.to_datetime(survey_lookup['date']).dt.date.min()
    max_date = pd.to_datetime(survey_lookup['date']).dt.date.axn()
    for idx, date in survey_lookup['date'].items():
        if pd.isnull(date):
            survey_lookup.at[idx, 'date'] = generate_random_date()


def generate_random_date(start, end):
    """Get a random date between two dates"""
    date_format = '%d/%m/%Y'
    start_date = time.mktime(time.strptime(start, date_format))
    end_date = time.mktime(time.strptime(end, date_format))
    random_sample = np.random.beta(a=5, b=2)

    ptime = start_date + random_sample * (end_date - start_date)

    return time.strftime(date_format, time.localtime(ptime))
