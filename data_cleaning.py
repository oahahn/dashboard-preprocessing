import pandas as pd
import numpy as np
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

    # Cycle through the species category column and correct alternate spelling
    for idx, name in detections['species_category'].items():
        for correct_name, alias_list in maps.species_category_map.items():
            if name in alias_list:
                detections.at[idx, 'species_category'] = correct_name
                break

    return detections


def correct_species_categories(detections):
    # Goes through the species names and makes sure they are properly categorised
    for idx, name in detections['species_name'].items():
        for correct_category, alias_list in maps.species_category_corrections.items():
            if name in alias_list:
                detections.at[idx, 'species_category'] = correct_category
                break
    return detections


def fill_in_null_values(detections):
    # Fills in categories that are recorded as null, which have an associated species name
    for idx, row in detections.iterrows():
        category = row['species_category']
        name = row['species_name']
        category_null_name_present = (not isinstance(category, str)) and isinstance(name, str)
        identified_species_name = (name != 'Unspecified')
        if category_null_name_present and identified_species_name:
            try:
                species_category = maps.null_species_category_corrections[name]
                detections.at[idx, 'species_category'] = species_category
            except:
                print(f"Species name '{row['species_name']}' not present in the null_species_category_corrections "
                      f"dictionary in maps.py")
    return detections


def add_unspecified_labels(detections):
    # If a pilot has labelled a detection with a general species category, this fills in the species name as unspecified
    for idx, name in detections['species_name'].items():
        if name in maps.unspecifieed_species:
            detections.at[idx, 'species_name'] = 'Unspecified ' + name
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


def remove_null_rows(detections):
    # Drops rows where both species name and category are null
    rows_to_drop = []
    for idx, row in detections.iterrows():
        species_name_null = not isinstance(row['species_name'], str)
        species_category_null = not isinstance(row['species_category'], str)
        if species_name_null and species_category_null:
            rows_to_drop.append(idx)

    return detections.drop(index=rows_to_drop)


def clean_data(det_match):
    detections = select_relevant_columns(det_match)
    detections = standardise_species_name(detections)
    detections = standardise_probability(detections)
    detections = standardise_species_category(detections)
    detections = correct_species_categories(detections)
    detections = fill_in_null_values(detections)
    detections = add_unspecified_labels(detections)
    detections = remove_geographic_outliers(detections)
    detections = remove_null_rows(detections)
    return detections
