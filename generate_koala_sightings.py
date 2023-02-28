import pandas as pd
import os


def generate_koala_sightings(old_csvs, new_csvs):
    koala_sightings_original = pd.read_csv(os.path.join(old_csvs, 'koala_sightings.txt'), sep='\t')
    # Reduce database to relevant columns
    # columns_to_keep = ['DatasetName', 'CommonName', 'DateFirst', 'DateLast', 'NumberIndividuals', 'Latitude_GDA94', 'Longitude_GDA94', 'Accuracy']
    # koala_sightings = koala_sightings.filter(items=columns_to_keep)
    koala_sightings = pd.DataFrame({
        'DatasetName': koala_sightings_original['DatasetName'],
        'Species': koala_sightings_original['CommonName'],
        'Date': koala_sightings_original['DateFirst'],
        'Count': koala_sightings_original['NumberIndividuals']
    })
    # Convert the date columns to pandas datetime format
    koala_sightings['Date'] = pd.to_datetime(koala_sightings['Date'], dayfirst=True).dt.date
    # Filter sightings that have taken place since the drone hub has been operational
    detections = pd.read_csv(os.path.join(new_csvs, 'detections.csv'))
    first_drone_survey = pd.Timestamp(detections['date'].min()).date()
    # first_drone_survey = pd.Timestamp('2022-06-01').date()
    koala_sightings = koala_sightings[koala_sightings['Date'] >= first_drone_survey]
    koala_sightings = fill_in_counts(koala_sightings)
    # Filter sightings to a single client
    state_forests_biodata = koala_sightings[koala_sightings['DatasetName'] == 'State Forests Biodata']
    byron_coast_survey = koala_sightings[koala_sightings['DatasetName'] == 'Byron Coast Koala Monitoring Survey']
    i_spy_app = koala_sightings[koala_sightings['DatasetName'] == 'I Spy Koala app']
    wild_count_fauna = koala_sightings[koala_sightings['DatasetName'] == 'Wild Count Fauna']
    state_forests_biodata.to_csv(os.path.join(new_csvs, 'state_forests_biodata.csv'), index=False)
    byron_coast_survey.to_csv(os.path.join(new_csvs, 'byron_coast_survey.csv'), index=False)
    i_spy_app.to_csv(os.path.join(new_csvs, 'i_spy_app.csv'), index=False)
    wild_count_fauna.to_csv(os.path.join(new_csvs, 'wild_count_fauna.csv'), index=False)


def fill_in_counts(koala_sightings):
    for idx, count in koala_sightings['Count'].items():
        if pd.isnull(count) or (count == 0):
            koala_sightings.at[idx, 'Count'] = 1
    return koala_sightings
