import pandas as pd
import os
import numpy as np


def generate_date_lookup(detections, new_csvs):
    detections['detection_time'] = pd.to_datetime(detections['detection_time'])
    detections['date'] = pd.to_datetime(detections['detection_time'].dt.date)
    date_lookup = pd.DataFrame({'Date': detections['date']})
    date_lookup['Date'] = pd.to_datetime(date_lookup['Date'])
    date_lookup = date_lookup.drop_duplicates()
    date_lookup['dateID'] = np.arange(len(date_lookup))
    detections = add_date_key_to_detections(detections, date_lookup)

    date_lookup['Day Name'] = date_lookup['Date'].dt.day_name()
    date_lookup['Day of Week'] = date_lookup['Date'].dt.dayofweek
    date_lookup['Week'] = date_lookup['Date'].dt.isocalendar().week
    date_lookup['Start of Week'] = date_lookup['Date'].dt.to_period('W').dt.start_time
    date_lookup['Month'] = date_lookup['Date'].dt.month
    date_lookup['Start of Month'] = date_lookup['Date'].dt.to_period('M').dt.start_time
    date_lookup['Quarter'] = date_lookup['Date'].dt.quarter
    date_lookup['Year'] = date_lookup['Date'].dt.year
    date_lookup['Start of Year'] = date_lookup['Date'].dt.to_period('Y').dt.start_time
    date_lookup.to_csv(os.path.join(new_csvs, 'date_lookup.csv'), index=False)
    return detections


def add_date_key_to_detections(detections, date_lookup):
    # Add in the date ID key to the detections database
    detections = pd.merge(detections, date_lookup, left_on='date', right_on='Date', validate='many_to_one')
    # Remove species category and species name from detections database
    detections = detections.drop(columns=['Date', 'date'])
    return detections
