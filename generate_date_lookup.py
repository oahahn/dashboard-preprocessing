import pandas as pd
import os


def generate_date_lookup(detections, new_csvs):
    detections['detection_time'] = pd.to_datetime(detections['detection_time'])
    start_date = detections['detection_time'].min()
    end_date = detections['detection_time'].max()
    date_lookup = pd.DataFrame({"Date": pd.date_range(start_date, end_date)})
    date_lookup["Day"] = date_lookup.Date.dt.day_name()
    date_lookup["Week"] = date_lookup.Date.dt.isocalendar().week
    date_lookup["Quarter"] = date_lookup.Date.dt.quarter
    date_lookup["Year"] = date_lookup.Date.dt.year
    date_lookup.to_csv(os.path.join(new_csvs, 'date_lookup.csv'), index=False)
    return detections