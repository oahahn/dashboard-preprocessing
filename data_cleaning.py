import numpy as np
import pandas as pd

import maps


def select_relevant_columns(det_match):
    return pd.DataFrame({
        'detection_time': det_match['detection_time'],
        'probability': det_match['probability'],
        'detection_count': det_match['detection_count'],
        'latitude': det_match['drone_lat'],
        'longitude': det_match['drone_lon'],
        'surveyID': det_match['surveyID'],
        'KML': det_match['KML'],
        'species_category': det_match['species_category'],
        'species_name': det_match['species_name']
    })


def standardise_species_name(detections):
    # Strip text, remove underscores and add capitalised first letters
    detections['species_name'] = detections['species_name'].str.strip()
    detections['species_name'] = detections['species_name'].str.title()
    detections['species_name'] = detections['species_name'].str.replace('_', ' ')

    # Cycle through the species_name column and correct alternate spelling
    remove_indices = []
    for idx, name in detections['species_name'].items():
        if name in maps.to_remove:
            remove_indices.append(idx)
            continue
        for correct_name, alias_list in maps.species_name_map.items():
            if name in alias_list:
                detections.at[idx, 'species_name'] = correct_name
                break

    # Remove vague detections
    return detections.drop(index=remove_indices)


def standardise_probability(detections):
    # Trim whitespace and add capitalised first letters
    detections['probability'] = detections['probability'].str.strip()
    detections['probability'] = detections['probability'].str.title()

    # Cycle through the probability column and correct alternate spelling
    for idx, name in detections['probability'].items():
        for correct_name, alias_list in maps.probability_map.items():
            if (name in alias_list):
                detections.at[idx, 'probability'] = correct_name
                break

    return detections


def standardise_species_category(detections):
    # Trim whitespace and add capitalised first letters
    detections['species_category'] = detections['species_category'].str.strip()
    detections['species_category'] = detections['species_category'].str.title()
    detections['species_category'] = detections['species_category'].str.replace('_', ' ')

    # Cycle through the probability column and correct alternate spelling
    for idx, name in detections['species_category'].items():
        for correct_name, alias_list in maps.species_category_map.items():
            if name in alias_list:
                detections.at[idx, 'species_category'] = correct_name
                break

    return detections


def correct_species_categories(detections):
    for idx, name in detections['species_name'].items():
        for correct_category, alias_list in maps.species_category_corrections.items():
            if name in alias_list:
                detections.at[idx, 'species_category'] = correct_category
                break
    return detections


def fill_in_null_values(detections):
    for idx, row in detections.iterrows():
        if not isinstance(row['species_category'], str) and isinstance(row['species_name'], str):
            try:
                species_category = maps.null_species_category_corrections[row['species_name']]
                detections.at[idx, 'species_category'] = species_category
            except:
                print("Spceies name not present in maps.null_species_category_corrections")
    return detections


def remove_geographic_outliers(detections):
    # Cycle through the latitude and longitude columns and search for coordinates outside NSW
    remove_indices = []
    for idx, row in detections.iterrows():
        latitude_outside_nsw = (row['latitude'] < -37.505768) or (row['latitude'] > -28.156804)
        negative_latitude_in_nsw = (-row['latitude'] > -37.505768) or (-row['latitude'] < -28.156804)
        longitude_outside_nsw = (row['longitude'] < 140.993300) or (row['longitude'] > 153.638805)
        # Some latitude coordinates were missing a minus sign
        if latitude_outside_nsw and negative_latitude_in_nsw:
            detections.at[idx, 'latitude'] = -row['latitude']
        elif latitude_outside_nsw or longitude_outside_nsw:
            remove_indices.append(idx)

    # Remove vague detections
    return detections.drop(index=remove_indices)


def clean_data(det_match):
    detections = select_relevant_columns(det_match)
    detections = standardise_species_name(detections)
    detections = standardise_probability(detections)
    detections = standardise_species_category(detections)
    detections = correct_species_categories(detections)
    detections = fill_in_null_values(detections)
    detections = remove_geographic_outliers(detections)
    return detections
