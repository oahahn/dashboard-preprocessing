import pandas as pd
import os


def generate_survey_lookup(old_csvs):
    survey_match = pd.read_csv(os.path.join(old_csvs, 'survey_match.csv'))
    # Filter relevant columns
    survey_lookup = pd.DataFrame({
        'surveyID': survey_match['surveyID'],
        'client': survey_match['client'],
        'mission': survey_match['mission'],
        'date': survey_match['start_time'],
        'location_id': survey_match['location_id']
    })
    # Drop duplicate surveyID entries
    survey_lookup = survey_lookup.drop_duplicates(subset=['surveyID'])
    survey_lookup = remove_null_rows(survey_lookup)
    survey_lookup['date'] = pd.to_datetime(survey_lookup['date']).dt.date
    return survey_lookup


def remove_null_rows(survey_lookup):
    """Drops rows which are not useful for Power BI"""
    rows_to_drop = []
    for idx, row in survey_lookup.iterrows():
        if row['mission'] == '?':
            rows_to_drop.append(idx)
    return survey_lookup.drop(index=rows_to_drop)
