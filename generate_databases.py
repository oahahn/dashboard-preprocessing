from data_cleaning import clean_data
from generate_species_lookup import generate_species_lookup
from generate_kml_lookup import generate_kml_lookup
from generate_survey_lookup import generate_survey_lookup
from generate_date_lookup import generate_date_lookup
from generate_detections import generate_detections
from generate_videos_database import generate_videos_database
from generate_pilot_lookup import generate_individual_databases
from generate_location_lookup import generate_location_lookup
from generate_mission_lookup import generate_mission_lookup

import os
import argparse


def generate_databases(args):
    # If the location for the new databases doesn't exist, create it
    if not os.path.isdir(args.new_csv_dir):
        os.makedirs(args.new_csv_dir)

    detections = clean_data(args.old_csv_dir)
    detections, species_lookup = generate_species_lookup(detections, args.new_csv_dir)
    survey_lookup = generate_survey_lookup(args.old_csv_dir, args.new_csv_dir)
    generate_location_lookup(args.old_csv_dir, args.new_csv_dir, survey_lookup)
    # generate_mission_lookup(survey_lookup, args.new_csv_dir)
    # detections, kml_lookup = generate_kml_lookup(detections, survey_lookup, args.old_csv_dir, args.new_csv_dir)
    detections = generate_detections(detections)
    detections = generate_date_lookup(detections, args.new_csv_dir)
    generate_videos_database(args.old_csv_dir, args.new_csv_dir)
    detections.to_csv(os.path.join(args.new_csv_dir, 'detections.csv'), index=False)
    generate_individual_databases(args.new_csv_dir, detections, survey_lookup)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-od', '--old_csv_dir', default='old-csvs')
    parser.add_argument('-nd', '--new_csv_dir', default='new-csvs')
    args = parser.parse_args()
    generate_databases(args)
