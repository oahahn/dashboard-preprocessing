import pandas as pd
import numpy as np
import os

OLD_DATABASE_DIRECTORY = './old-csvs'
NEW_DATABASE_DIRECTORY = './new-csvs'

def generate_species_lookup(detections, new_csvs):
    # Create a new database with a list of unqiue species names
    species_lookup = pd.DataFrame({
        'species_name': detections['species_name'],
        'species_category': detections['species_category']
    })
    species_lookup = species_lookup.drop_duplicates(subset=['species_name'])
    # Create a primary key
    species_lookup['speciesID'] = np.arange(len(species_lookup))
    # Reorder the columns to have the primary key in the first position and export
    species_lookup = species_lookup[['speciesID', 'species_name', 'species_category']]

    # Add in the species ID key to the original detections database
    detections = pd.merge(detections, species_lookup[['speciesID', 'species_name']], on='species_name',
                          validate='many_to_one')
    # Remove species category and species name from detections database
    detections = detections.drop(columns=['species_category', 'species_name'])
    generate_species_category_lookup(species_lookup, new_csvs)
    return detections, species_lookup


def generate_species_category_lookup(species_lookup, new_csvs):
    # Create a new database with a list of unqiue species categories
    species_category_lookup = pd.DataFrame({'species_category': species_lookup['species_category']})
    species_category_lookup = species_category_lookup.drop_duplicates()
    # Create a primary key column
    species_category_lookup['species_categoryID'] = np.arange(len(species_category_lookup))
    # Reorder the columns to have the primary key in the first position
    species_category_lookup = species_category_lookup[['species_categoryID', 'species_category']]
    # Export the database to this folder
    species_category_lookup.to_csv(os.path.join(new_csvs, 'species_category_lookup.csv'), index=False)

    # Add in the species category ID key to the original species lookup database
    species_lookup = pd.merge(species_lookup, species_category_lookup, on='species_category', validate='many_to_one')
    # Remove species category and species name from detections database
    species_lookup = species_lookup.drop(columns=['species_category'])
    species_lookup.to_csv(os.path.join(new_csvs, 'species_lookup.csv'), index=False)
