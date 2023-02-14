## Data Preprocessing Methods

This repo contains a collection of preprocessing methods to clean and organise data from a raw backend form into a structured data model connected by primary and foreign keys. This data model is intended to be imported into a Power BI project for data visualisation. 

### Requirements

In order to run the preprocessing, you need a folder containing the following databases:

* airdata_matches.csv
* det_match.csv
* kml_matches.csv
* survey_match.csv

The preprocessing methods will clean and organise these databases into new databases related by keys. By default, the folder containing these databases is named *old-csvs* but you can specify a different location. This is explained in the following section. 

A new folder named *new-csvs* is created with the new databases that form the data model. These can be imported directly into Power BI and will automatically be linked. 

### Running the Preprocessing

You can run the preprocessing methods using the command: 

<code>python generate_databases.py</code>

If you would like to specify an alternative location for the database files to be read from, you can use the following command line argument:

<code>python generate_databases.py --old\_csv\_dir alternative\_folder\_path</code>

If you would like to specify an alternative location for the new database files to be created in, you can use the following command line argument:

<code>python generate_databases.py --new\_csv\_dir alternative\_folder\_path</code>