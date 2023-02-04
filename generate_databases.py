import pandas as pd
from data_cleaning import clean_data
import numpy as np


def generate_species_lookup(dataframe):
    # Create a new database with a list of unqiue species names
    species_lookup = pd.DataFrame({
        'species_name': dataframe['species_name'],
        'species_category': dataframe['species_category']
    })
    species_lookup = species_lookup.drop_duplicates(subset=['species_name'])
    # Create a primary key
    species_lookup['speciesID'] = np.arange(len(species_lookup))
    # Reorder the columns to have the primary key in the first position and export
    species_lookup = species_lookup[['speciesID', 'species_name', 'species_category']]
    species_lookup.to_csv('species_lookup.csv', index=False)

    # Add in the species ID key to the original detections database
    dataframe = pd.merge(dataframe, species_lookup[['speciesID', 'species_name']], on='species_name',
                         validate='many_to_one')
    # Remove species category and species name from detections database
    return dataframe.drop(columns=['species_category', 'species_name'])


if __name__ == '__main__':
    det_match = pd.read_csv('det_match.csv')
    detections = clean_data(det_match)
    detections = generate_species_lookup(detections)
