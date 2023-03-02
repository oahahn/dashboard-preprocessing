import pandas as pd


def generate_detections(detections, kml_lookup):
    detections = add_kml_key_to_detections(detections, kml_lookup)
    detections = add_coarse_probability_column(detections)
    return detections


def add_kml_key_to_detections(detections, kml_lookup):
    # Add in the KML ID key to the original detections database
    kml_lookup_to_merge = kml_lookup[['kmlID', 'filename']]
    detections = pd.merge(detections, kml_lookup_to_merge, left_on='KML', right_on='filename', validate='many_to_one')
    # Remove species category and species name from detections database
    detections = detections.drop(columns=['KML', 'kml_matches', 'filename', 'surveyID'])
    return detections


def add_coarse_probability_column(detections):
    coarse_probability_list = []
    for probability in detections['probability'].values:
        if probability in ['High', '100%']:
            coarse_probability_list.append('High')
        else:
            coarse_probability_list.append('Other')
    detections['high_probability'] = coarse_probability_list
    return detections
