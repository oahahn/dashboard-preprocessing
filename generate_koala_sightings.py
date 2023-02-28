import pandas as pd
import os


def generate_koala_sightings(old_csvs, new_csvs):
    koala_sightings = pd.read_csv(os.path.join(old_csvs, 'koala_sightings.txt'), sep='\t')
    # Reduce database to relevant columns
    columns_to_keep = ['DatasetName', 'CommonName', 'DateFirst', 'DateLast', 'NumberIndividuals', 'Latitude_GDA94', 'Longitude_GDA94', 'Accuracy']
    koala_sightings = koala_sightings.filter(items=columns_to_keep)
    # Convert the date columns to pandas datetime format
    koala_sightings['DateFirst'] = pd.to_datetime(koala_sightings['DateFirst'], dayfirst=True).dt.date
    koala_sightings['DateLast'] = pd.to_datetime(koala_sightings['DateLast'], dayfirst=True).dt.date
    # Filter sightings that have taken place since the drone hub has been operational
    detections = pd.read_csv(os.path.join(new_csvs, 'detections.csv'))
    first_drone_survey = pd.Timestamp(detections['date'].min()).date()
    koala_sightings = koala_sightings[koala_sightings['DateFirst'] >= first_drone_survey]
    koala_sightings.to_csv(os.path.join(new_csvs, 'koala_sightings.csv'), index=False)
