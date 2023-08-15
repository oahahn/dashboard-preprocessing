import pandas as pd
import maps
import os


def generate_detections(old_csvs):
    det_match = pd.read_csv(os.path.join(old_csvs, 'det_match.csv')).drop_duplicates()
    detections = select_relevant_columns(det_match)
    detections = standardise_species_name(detections)
    detections = standardise_probability(detections)
    # Filter only high probability of detection
    detections = detections[detections.probability.isin(["High", "100%"])]
    detections = detections.drop(columns=['probability'])
    detections = standardise_species_category(detections)
    detections = correct_species_categories(detections)
    detections = fill_in_null_values(detections)
    detections = use_broader_species_names(detections)
    detections = group_into_coarse_categories(detections)
    detections = remove_geographic_outliers(detections)
    # detections = detections.drop(columns=['latitude', 'longitude'])
    detections = remove_null_rows(detections)
    detections = remove_incorrect_dates(detections)
    detections = correct_categories(detections)
    detections = flag_incorrect_categorisation(detections)
    return detections


def select_relevant_columns(det_match):
    return pd.DataFrame({
        'detection_time': det_match['detection_time'],
        'probability': det_match['probability'],
        'detection_count': det_match['detection_count'],
        'surveyID': det_match['surveyID'],
        'species_category': det_match['species_category'],
        'species_name': det_match['species_name'],
        'latitude': det_match['drone_lat'],
        'longitude': det_match['drone_lon'],
        'client': det_match['client']
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


def use_broader_species_names(detections):
    # This method maps specific names like Brushtail Possum to general names like Possum for display on the dashboard
    for idx, name in detections['species_name'].items():
        for species in maps.species_to_display:
            if species in name:
                detections.at[idx, 'species_name'] = species
                break
    return detections


def group_into_coarse_categories(detections):
    # Label all species that are not important enough to display on the dashboard as 'Other'
    other_detections = []
    for idx, name in detections['species_name'].items():
        not_important = name not in maps.species_to_display
        not_other_category = detections.at[idx, 'species_category'] != 'Other'
        if not_important and not_other_category:
            other_detections.append(detections.loc[idx])
            detections.at[idx, 'species_name'] = 'Other'
    return detections


def remove_geographic_outliers(detections):
    # Cycle through the latitude and longitude columns and search for coordinates outside NSW
    remove_indices = []
    for idx, row in detections.iterrows():
        latitude_outside_nsw = (float(row['latitude']) < -37.505768) or (float(row['latitude']) > -28.156804)
        negative_latitude_in_nsw = (-float(row['latitude']) > -37.505768) or (-float(row['latitude']) < -28.156804)
        longitude_outside_nsw = (float(row['longitude']) < 140.993300) or (float(row['longitude']) > 153.638805)
        # Some latitude coordinates were missing a minus sign
        if latitude_outside_nsw and negative_latitude_in_nsw:
            detections.at[idx, 'latitude'] = -float(row['latitude'])
        elif latitude_outside_nsw or longitude_outside_nsw:
            remove_indices.append(idx)

    # Remove vague detections
    return detections.drop(index=remove_indices)


def remove_null_rows(detections):
    # Drops rows where both species name and category are null
    rows_to_drop = []
    for idx, row in detections.iterrows():
        species_null = pd.isnull(row['species_name']) and pd.isnull(row['species_category'])
        detection_time_null = pd.isnull(row['detection_time'])
        if species_null or detection_time_null:
            rows_to_drop.append(idx)
    return detections.drop(index=rows_to_drop)


def remove_incorrect_dates(detections):
    # Drops rows where the detection date is before the start of the project
    rows_to_drop = []
    for idx, row in detections.iterrows():
        detection_date = pd.to_datetime(row['detection_time']).date()
        incorrect_date = detection_date < pd.Timestamp(year=2020, month=1, day=1).date()
        if incorrect_date:
            rows_to_drop.append(idx)
    return detections.drop(index=rows_to_drop)


def correct_categories(detections):
    # Goes through the species names and makes sure they are properly categorised
    for idx, row in detections.iterrows():
        name = row['species_name']
        category = row['species_category']
        if category == 'Ground Species' and name == 'Wallaby':
            detections.at[idx, 'species_category'] = 'Macropod'
        elif category == 'Glider':
            detections.at[idx, 'species_category'] = 'Arboreal Species'
    return detections


def flag_incorrect_categorisation(detections):
    for index, row in detections.iterrows():
        species_name = row['species_name']
        species_category = row['species_category']

        # Perform your custom validation based on your knowledge or assumptions
        if species_category == 'Aerial Species':
            valid_species = ['Flying Fox', 'Other']
        elif species_category == 'Arboreal Species':
            valid_species = ['Possum', 'Glider', 'Koala', 'Other']
        elif species_category == 'Ground Species':
            valid_species = ['Wombat', 'Deer', 'Rabbit', 'Goat', 'Dingo', 'Other']
        elif species_category == 'Macropod':
            valid_species = ['Wallaby', 'Potoroo', 'Kangaroo', 'Other']
        elif species_category == 'Other':
            valid_species = ['Tree Hollow', 'Other']
        else:
            print(f"Invalid species category: {species_category}")
            # Perform further actions if needed, such as handling the invalid category
            continue

        if species_name not in valid_species:
            print(f"Invalid species name: {species_name} in category: {species_category}")
            # Perform further actions if needed, such as updating the category or handling the invalid entry

    return detections
