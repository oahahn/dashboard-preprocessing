import pandas as pd
import os


def generate_video_lookup(old_csvs, new_csvs):
    video_matches = pd.read_csv(os.path.join(old_csvs, 'video_matches.csv'))

    video_lookup = pd.DataFrame({
        'date': pd.to_datetime(video_matches['creation_time']).dt.date,
        'file_size': video_matches['file_size'],
        'duration': video_matches['duration']
    })
    video_lookup = remove_null_rows(video_lookup)
    video_lookup.to_csv(os.path.join(new_csvs, 'video_lookup.csv'), index=False)


def remove_null_rows(video_lookup):
    # Drops rows where date, file_size and duration are all null
    rows_to_drop = []
    for idx, row in video_lookup.iterrows():
        if pd.isnull(row['date']) or pd.isnull(row['file_size']):
            rows_to_drop.append(idx)
    return video_lookup.drop(index=rows_to_drop)
