import pandas as pd
import os


pilot_list = ['Matt Clements', 'Chad Beranek', 'Lachlan Hall', 'Sabrina Velasco', 'Pearce Thomas', 'George Madani',
              'Brian Adam', 'Adam Baus', 'Sam Turbill', 'Fin Murphey', 'Finlay Murphey', 'Nathan Browne', 'Shelby Ryan',
              'Ryan Witt', 'Andrew Baker', 'Stephen Mahony', 'Shaymus Gooley', 'Adrian Sujaraj', 'Sophie Hall',
              'Paul Manzoni', 'Robbie Birkett', 'Liam Stephen', 'Tim Jessop', 'Madison Casley', 'Renae Hockey',
              'Allen McIlwee', 'Elliot Webb', 'Ben Hope', 'Maquel Brandimarti', 'Jared Wood', 'Adam Roff',
              'Samantha Sanders', 'Oliver Brynes', 'Jarrod Daly', 'Tim Johnson', 'Shawn Ryan', 'Jarrad Prangell',
              'Kevin Fallon', 'Darryn ?', 'James Tawdrous', 'Sam Provost', 'Hayden ?']

def generate_pilot_lookup(new_csvs):
    pilot_lookup = pd.DataFrame({
        'name': pilot_list
    })

    pilot_lookup.to_csv(os.path.join(new_csvs, 'pilot_lookup.csv'), index=False)
