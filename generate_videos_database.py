import pandas as pd
import os
from ast import literal_eval


def generate_videos_database(old_csvs, new_csvs, null_location_ids):
    video_matches = pd.read_csv(os.path.join(old_csvs, 'video_matches.csv'))

    videos_database = pd.DataFrame({
        'date': pd.to_datetime(video_matches['creation_time']).dt.date,
        'file_size': video_matches['file_size'],
        'duration': video_matches['duration'],
        'surveyID': video_matches['surveyID'],
        'location_id': video_matches['kml_location_id']
    })
    videos_database = remove_null_rows(videos_database, null_location_ids)
    videos_database = clean_survey_id_column(videos_database)
    videos_database.to_csv(os.path.join(new_csvs, 'videos.csv'), index=False)


def remove_null_rows(videos_database, null_location_ids):
    # Drops rows where date or file_size are null
    rows_to_drop = []
    for idx, row in videos_database.iterrows():
        if pd.isnull(row['date']) or pd.isnull(row['file_size']):
            rows_to_drop.append(idx)
        elif row['location_id'] in null_location_ids:
            rows_to_drop.append(idx)
    return videos_database.drop(index=rows_to_drop)

def clean_survey_id_column(videos_database):
    for idx, surveyID_matches_list in videos_database['surveyID'].items():
        if isinstance(surveyID_matches_list, str) and '[' in surveyID_matches_list:
            videos_database.at[idx, 'surveyID'] = literal_eval(surveyID_matches_list)[0]
    return videos_database
