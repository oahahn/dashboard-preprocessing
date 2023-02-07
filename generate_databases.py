import pandas as pd
from data_cleaning import clean_data
import numpy as np
import os
from ast import literal_eval

OLD_DATABASE_DIRECTORY = './CSVs'
NEW_DATABASE_DIRECTORY = './databases'

def generate_species_lookup(detections):
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
    return detections, species_lookup


def generate_species_category_lookup(species_lookup):
    # Create a new database with a list of unqiue species categories
    species_category_lookup = pd.DataFrame({'species_category': species_lookup['species_category']})
    species_category_lookup = species_category_lookup.drop_duplicates()
    # Create a primary key column
    species_category_lookup['species_categoryID'] = np.arange(len(species_category_lookup))
    # Reorder the columns to have the primary key in the first position
    species_category_lookup = species_category_lookup[['species_categoryID', 'species_category']]
    # Export the database to this folder
    species_category_lookup.to_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'species_category_lookup.csv'), index=False)

    # Add in the species category ID key to the original species lookup database
    species_lookup = pd.merge(species_lookup, species_category_lookup, on='species_category', validate='many_to_one')
    # Remove species category and species name from detections database
    species_lookup = species_lookup.drop(columns=['species_category'])
    species_lookup.to_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'species_lookup.csv'), index=False)


def generate_kml_lookup(detections):
    kml_lookup = pd.DataFrame({'filename': detections['KML']})
    kml_lookup = kml_lookup.drop_duplicates()
    # Create a primary key
    kml_lookup['kmlID'] = np.arange(len(kml_lookup))
    # Reorder the columns to have the primary key in the first position and export
    kml_lookup = kml_lookup[['kmlID', 'filename']]
    kml_lookup.to_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'kml_lookup.csv'), index=False)

    # Add in the KML ID key to the original detections database
    detections = pd.merge(detections, kml_lookup, left_on='KML', right_on='filename', validate='many_to_one')
    # Remove species category and species name from detections database
    detections = detections.drop(columns=['KML', 'filename'])
    return detections, kml_lookup


def generate_airdata_lookup():
    airdata_matches = pd.read_csv('CSVs/airdata_matches.csv')
    # Extract the relevant columns
    airdata_lookup = pd.DataFrame({
        'flight_start': airdata_matches['flight_start'],
        'flight_end': airdata_matches['flight_end'],
        'start_time': airdata_matches['start_time'],
        'finish_time': airdata_matches['finish_time'],
        'filename': airdata_matches['filename'],
        'air_seconds': airdata_matches['Air Seconds'],
        'kml_area': airdata_matches['kml_area'],
        'kml_matches': airdata_matches['kml_matches'],
        'surveyID': airdata_matches['surveyID']
    })
    # Drop any entries which start and end at the same time on the same date to ensure unique entries
    airdata_lookup = airdata_lookup.drop_duplicates(subset=['flight_start', 'flight_end'])
    # Create a primary key
    airdata_lookup['airdataID'] = np.arange(len(airdata_lookup))
    # Reorder the columns to have the primary key in the first position and export
    airdata_lookup = airdata_lookup[['airdataID', 'filename', 'air_seconds', 'kml_area', 'kml_matches', 'surveyID']]

    airdata_lookup = remove_bad_formatting(airdata_lookup)
    airdata_lookup = add_kml_key(airdata_lookup)
    airdata_lookup.to_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'airdata_lookup.csv'), index=False)


def remove_bad_formatting(airdata_lookup):
    """Removes entries where the kml filename has a strange format with index, this should be fixed on the backend"""
    string_indices = []
    list_indices = []
    string_count = 0
    for idx, kml_matches_list in airdata_lookup['kml_matches'].items():
        if isinstance(kml_matches_list, str) and '[' in kml_matches_list:
            airdata_lookup.at[idx, 'kml_matches'] = literal_eval(kml_matches_list)
            list_indices.append(idx)
        elif isinstance(kml_matches_list, str):
            string_indices.append(idx)
            string_count += 1
    print(f'string count: {string_count}')
    return airdata_lookup.filter(items=list_indices, axis=0)


def add_kml_key(airdata_lookup):
    """Replaces the kml filename lists with the kml keys from the kml_lookup table"""
    kml_lookup = pd.read_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'kml_lookup.csv'))
    kmlIDs = []
    kml_filename_list = kml_lookup['filename'].to_list()
    sum = 0
    for idx, kml_matches_list in airdata_lookup['kml_matches'].items():
        # Check if the first kml file listed has a key
        if isinstance(kml_matches_list, list):
            # Look through list of filenames to try associate a kml key with the list
            filename_key_not_found = True
            for kml_filename in kml_matches_list:
                if kml_filename in kml_filename_list:
                    kml_idx = kml_filename_list.index(kml_filename)
                    kmlIDs.append(kml_lookup.at[kml_idx, 'kmlID'])
                    filename_key_not_found = False
                    break
            if filename_key_not_found:
                # If the kml filename doesn't have a key in the kml_lookup table, assign it the na key
                na_index = kml_lookup.index[kml_lookup['filename'].isna()][0]
                kmlIDs.append(na_index)
                sum += 1
        else:
            # If this entry is not a list, assign it the na key
            na_index = kml_lookup.index[kml_lookup['filename'].isna()][0]
            kmlIDs.append(na_index)
    print(f'sum: {sum}')
    airdata_lookup['kmlID'] = kmlIDs
    airdata_lookup = airdata_lookup.drop(columns='kml_matches')
    return airdata_lookup


if __name__ == '__main__':
    det_match = pd.read_csv(os.path.join(OLD_DATABASE_DIRECTORY, 'det_match.csv'))
    detections = clean_data(det_match)
    detections, species_lookup = generate_species_lookup(detections)
    generate_species_category_lookup(species_lookup)
    detections, kml_lookup = generate_kml_lookup(detections)
    generate_airdata_lookup()
    detections.to_csv(os.path.join(NEW_DATABASE_DIRECTORY, 'detections.csv'), index=False)