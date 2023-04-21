import pandas as pd
import os
import numpy as np


def generate_individual_databases(new_csvs, detections, survey_lookup):
    detections_only = detections[['detection_time', 'detection_count', 'speciesID']]
    detections_only['detection_time'] = pd.to_datetime(detections_only['detection_time']).dt.date
    detections_only.to_csv(os.path.join(new_csvs, 'detections_only.csv'), index=False)

    pilot_lookup = pd.DataFrame({'pilot': survey_lookup['pilot']})
    pilot_lookup = pilot_lookup.dropna()
    pilot_lookup = pilot_lookup.drop_duplicates()
    pilot_lookup['pilotID'] = np.arange(len(pilot_lookup))
    pilot_lookup.to_csv(os.path.join(new_csvs, 'pilot_lookup.csv'), index=False)


# import pandas as pd
# import numpy as np
#
# pilot_list = ['Matt Clements', 'Chad Beranek', 'Lachlan Hall', 'Sabrina Velasco', 'Pearce Thomas', 'George Madani',
#               'Brian Adam', 'Adam Baus', 'Sam Turbill', 'Fin Murphey', 'Finlay Murphey', 'Nathan Browne', 'Shelby Ryan',
#               'Ryan Witt', 'Andrew Baker', 'Stephen Mahony', 'Shaymus Gooley', 'Adrian Sujaraj', 'Sophie Hall',
#               'Paul Manzoni', 'Robbie Birkett', 'Liam Stephen', 'Tim Jessop', 'Madison Casley', 'Renae Hockey',
#               'Allen McIlwee', 'Elliot Webb', 'Ben Hope', 'Maquel Brandimarti', 'Jared Wood', 'Adam Roff',
#               'Samantha Sanders', 'Oliver Brynes', 'Jarrod Daly', 'Tim Johnson', 'Shawn Ryan', 'Jarrad Prangell',
#               'Kevin Fallon', 'Darryn ?', 'James Tawdrous', 'Sam Provost', 'Hayden ?']
#
# pilot_loookup = pd.DataFrame({
#     'name': pilot_list
# })
#
# pilot_loookup.to_csv('pilot_lookup.csv', index=False)