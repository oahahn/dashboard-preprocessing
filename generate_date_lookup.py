import pandas as pd
import os


def generate_date_lookup(detections, new_csvs):
    detections['detection_time'] = pd.to_datetime(detections['detection_time'])
    date_lookup = pd.DataFrame({'Date': detections['detection_time']})
    date_lookup['Date'] = pd.to_datetime(date_lookup['Date'])
    date_lookup = date_lookup.drop_duplicates()
    date_lookup['Day'] = date_lookup['Date'].dt.day_name()
    date_lookup['Week'] = date_lookup['Date'].dt.isocalendar().week
    date_lookup['Month'] = date_lookup['Date'].dt.month
    date_lookup['Quarter'] = date_lookup['Date'].dt.quarter
    date_lookup['Year'] = date_lookup['Date'].dt.year
    date_lookup.to_csv(os.path.join(new_csvs, 'date_lookup.csv'), index=False)
    return detections