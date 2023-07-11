import pandas as pd
import os
import numpy as np


pilot_list = [
    # First Intake
    'Brian Adam',
    'Fin Murphey',
    'George Madani',
    'Lachlan Hall',
    'Matt Clements',
    'Nathan Browne',
    'Pearce Thomas',
    # NPWS
    'Adam Baus',
    'Andrew Baker',
    # UON
    'Chad Beranek',
    'Ryan Witt',
    'Sabrina Velasco',
    'Sam Turbill',
    'Shelby Ryan',
    'Lachlan Howell',
    # KS Intake
    'Liam Stephen',
    'Stephen Mahony',
    'Shaymus Gooley',
    'Adrian Sujaraj',
    'Sophie Hall',
    'Paul Manzoni',
    'Robbie Birkett',
    # Koala Strat
    'Tim Jessop',
    'Ben Hope',
    'Elliot Webb',
    'Renae Hockey',
    'Allen McIlwee',
    'Madison Caseley',
    # UON Intake
    'Samantha Sanders',
    'Oliver Brynes',
    'Jarrod Daly',
    'Tim Johnson',
    'Shawn Ryan',
    'Jarrad Prangell',
    'Kevin Fallon',
    # KS intake 2
    'James Mitchell-Williams',
    'Alison Shilling',
    'Jeffrey McKee',
    'Robert Johnston',
    'Bastian Steinrucken',
    'Matthew Elsley',
    'Kieran Richardt',
    'Jake Smith-Maloney',
    'Kade Slater',
    'Freya Dodd',
    'Matthew Harvey',
    'Jedd Browne',
    # KS intake 2 extra
    'Josh Whitehead',
    'Nazly Teller',
    'Charlotte Rigolot',
    'Wally Hammond',
    'Rebecca Seeto',
    # Hub
    'Adam Roff',
    'Maquel Brandimarti',
    'Jared Wood',
    # Never Active
    'James Tawdrous',
    'Hayden Griffith',
    'Sam Provost',
    'Daryn McKenny',
]


def generate_pilot_lookup(new_csvs):
    pilot_lookup = pd.DataFrame({
        'index': np.arange(len(pilot_list)),
        'name': pilot_list
    })

    pilot_lookup.to_csv(os.path.join(new_csvs, 'pilot_lookup.csv'), index=False)
