import pandas as pd
from data_cleaning import clean_data
from generate_species_lookup import generate_species_lookup
from generate_kml_lookup import generate_kml_lookup
from generate_airdata import generate_airdata
from generate_survey_lookup import generate_survey_lookup
from generate_date_lookup import generate_date_lookup

import os
import argparse


def generate_databases(args):
    # If the location for the new databases doesn't exist, create it
    if not os.path.isdir(args.new_csv_dir):
        os.makedirs(args.new_csv_dir)

    det_match = pd.read_csv(os.path.join(args.old_csv_dir, 'det_match.csv'))
    detections = clean_data(det_match)
    detections, species_lookup = generate_species_lookup(detections, args.new_csv_dir)
    detections, kml_lookup = generate_kml_lookup(detections, args.old_csv_dir, args.new_csv_dir)
    generate_airdata(kml_lookup, args.old_csv_dir, args.new_csv_dir)
    generate_survey_lookup(kml_lookup, args.old_csv_dir, args.new_csv_dir)
    detections = generate_date_lookup(detections, args.new_csv_dir)
    detections.to_csv(os.path.join(args.new_csv_dir, 'detections.csv'), index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-od', '--old_csv_dir', default='old-csvs')
    parser.add_argument('-nd', '--new_csv_dir', default='new-csvs')
    args = parser.parse_args()
    generate_databases(args)
