from gdrive import download_files
from detections import generate_detections
from surveys import generate_survey_lookup
from videos import generate_videos_database
from pilots import generate_pilot_lookup
from locations import generate_location_lookup
import os
import argparse


def generate_databases(args):
    if args.download_databases:
        download_files()
        
    # If the location for the new databases doesn't exist, create it
    if not os.path.isdir(args.new_csv_dir):
        os.makedirs(args.new_csv_dir)

    detections = generate_detections(args.old_csv_dir)
    generate_survey_lookup(args.old_csv_dir, args.new_csv_dir)
    generate_location_lookup(args.old_csv_dir, args.new_csv_dir)
    generate_videos_database(args.old_csv_dir, args.new_csv_dir)
    generate_pilot_lookup(args.new_csv_dir)
    detections.to_csv(os.path.join(args.new_csv_dir, 'detections.csv'), index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-od', '--old_csv_dir', default='old-csvs')
    parser.add_argument('-nd', '--new_csv_dir', default='new-csvs')
    parser.add_argument('-dd', '--download_databases', action='store_true', default=False)
    args = parser.parse_args()
    generate_databases(args)
