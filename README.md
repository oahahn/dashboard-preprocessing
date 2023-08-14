## Data Preprocessing Methods

This repo contains a collection of preprocessing methods to clean and organise data from a raw backend form into a structured data model connected by primary and foreign keys. This data model is intended to be imported into a Power BI project for data visualisation. 

### Requirements

In order to run the preprocessing, you need a folder containing the following databases:

* det_match.csv
* kml_matches.csv
* survey_match.csv
* location_dataframe.csv
* video_matches.csv

If you run the main script `generate_databases.py` in the command line, with the flag `--download_databases`, shown below, these databases will be downloaded automatically. 

``python generate_databases.py --download_databases``

By default, the folder containing these databases is named `old-csvs` but you can specify a different location. The following command would save the databases in a folder called `original_databases`

`python generate_databases.py --old_csv_dir original_databases`

The preprocessing methods will clean and organise these databases into new databases related by keys. A new folder named `new-csvs` is created with the new databases that form the data model. The databases that are generated include:
* detections.csv
* pilot_lookup.csv
* survey_lookup.csv
* videos.csv

These can be imported directly into Power BI, which should recognise the primary/foreign key relationships and automatically create a data model. 


If you would like to specify an alternative location for the new databases that are generated, you can use the following command:

`python generate_databases.py --new_csv_dir generated_databases`
