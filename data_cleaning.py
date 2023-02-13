import pandas as pd

import maps


def select_relevant_columns(det_match):
    return pd.DataFrame({
        'detection_time': det_match['detection_time'],
        'probability': det_match['probability'],
        'detection_count': det_match['detection_count'],
        'latitude': det_match['drone_lat'],
        'longitude': det_match['drone_lat'],
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


def clean_data(det_match):
    detections = select_relevant_columns(det_match)
    detections = standardise_species_name(detections)
    detections = standardise_probability(detections)
    detections = standardise_species_category(detections)
    detections = correct_species_categories(detections)
    return detections
