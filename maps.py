species_name_map = {
    'Arboreal Species': ['Aboreal', 'Medium Sized Arboreal', 'Small Arboreal Sp.', 'Arboreal', 'Arboreal Sp. -Small',
                         'Arboreal Sp.', 'Arboreal Sp. Small', 'Arboreal Sp', 'Arboreal/Canopy',
                         'Unsure. Medium-Sized Detection Half-Way Up Tree.', 'Unsure If Anything',
                         'Detection Down Low On Trunk'],
    'Aerial Species': ['Aerial'],
    'Bandicoot': ['Small Possible Bandicoot', 'Bandicoit', 'Bandicoot/ Pademelon?', 'Bandicoot?', 'Bandicoot/ Potoroo',
                  'Bandicoot (?)', 'Unknown (Bandicoot/Macropod?)', 'Unknown Mammal (Likely Bandicoot)',
                  'Small Unknown (Likely Bandicoot)', 'Rabbit/Bandicoot', 'Long-Nosed Bandicoot'],
    'Bird Species': ['Roosting Birds?', 'Flock Of Birds', 'Bird Of Prey', 'Bird Of Prey On Nest', 'Bird On Nest', 'Birds',
             'Small-Ish Bird Or Sugar Glider? (In Flight)', 'Two Birds', 'Rock And Small Roosting Bird?',
             'Medium Sized Unknown Thermal - Ground/ Very Low Arboreal + Small Roosting Birds',
             'Large Bird, Likely Raptore E.G. Wedge-Tailed Eagle. Maybe Lyrebird',
             'Unsure, Medium Sized Mid-Canopy, Maybe Two Birds', 'Unidentified Birds (X2)', 'Unknown (Small Bird)',
             'Unknown (Likely Bird?)', 'Bird (Parrot)', 'Common Bronzewing', 'Crimson Rosella', 'Currawong',
             'Kookaburra', 'Magpie', 'Musk Lorikeet', 'Lyrebird', 'Parrot', 'Sulphur-Crested Cockatoo',
             'Superb Lyrebird', 'White-Winged Chough', 'Parrot/ Cockatoos ?', 'Parrots', 'Crimson Roaella',
             'Dusky Woodswallows - Communal Roost', 'Birds- Kookaburra', 'Lyre Bird', 'Lyre Bied', 'Magpies',
             'Bronzewings (X2) - Validated By Ground Crew', 'White-winged Chough', 'White Winged Chough', 'Lorikeet',
             'Cockatoos And Warm Hollow', 'Cockatoos (X3)', 'Sulfur-Crested', 'Sulfur-Crested Cockatoo',
             'Yellow-tailed Black Cockatoo', 'Yellow-Tailed Black Cockatoos (Heard Call)', 'Cockatoo',
             'Yellow-Tail Cockatoos (X8) - Validated', 'Yellow-Tailed Black-Cockatoo', 'Owl', 'Owl Sp.',
             'Large Owl', 'Sooty Owl', 'Sooty Owl (Off Transecrt)', 'Powerful Owl', 'Bird', 'Dusky Woodswallow',
             'Australian King-Parrot', 'Black Cockatoo', 'Gang-Gang Cockatoos', 'Laughing Kookaburra', 'Tawny Frogmouth',
             'Topknot Pigeons', 'Musk/Rainbow Lorikeet', 'Galah', 'Galah - Not Listed In Bird List', 'Galahs',
            'Ringneck Parrot (Malleee)', 'Glossy Ibis', 'Crow', 'Crested Pigeon', 'Eastern Rosella', 'Raven',
            'Wedge-Tailed Eagle', 'Quail', 'Rosella', 'White Faced Hero', 'Topknot Pigeon'],
    'Brushtail Possum': ['Brush Tail', 'Brush-Tailed Possum', 'Probable Brushtail Possum', 'Brushtail Possum',
                        'Brush-Tail Possum', 'Brush Tail Possum', 'Brushtail', 'Mountain Brushtail Possum',
                         'Mountain Brush-Tailed Possum', 'Mountain Bobuck', 'Common Brushtail Possum',
                         'Mountain Brushtail'],
    'Ringtail Possum': ['Ring Tail', 'Ring-Tailed Possum', 'Small Canopy - Ringtails?', 'Possum - Ringtail?',
                        'Possum (Ringtail?)', 'Possum - Ringtail ?', 'Probable Possum (Not Koala) - Ringtail?',
                        'Ringtail Possums', 'Ringtail And 3 Small Ground Mammals', 'Ringtail Possum ?',
                        'Possums (Ring-Tail?)', 'Ringtail', 'Common Ringtail Possum'],
    'Cat': ['Feral Cat - Good Footage', '4 Legged Ground Mammal - Maybe Cat?', 'Feral Cat ?'],
    'Deer': ['Dear', 'Deer/Kangaroo'],
    'Eastern Grey Kangaroo': ['Eastern Grey', 'Macropod (Eastern Grey Kangaroos)', 'Macropod (Eastern Grey )',
                              'Grey Kangaroo'],
    'Kangaroo': [],
    'Feathertail Glider': ['Fethertail Glider', 'Feathertail', 'Feather-Tailed Glider Or Bird',
                           'Feathertail Gliders (X2)'],
    'Flying Fox': ['Flying-Fox', 'Flying Fox Fly-By', 'Single Video, Flying Fox Close', 'Pteropus Sp,', 'Bat',
                   'Bats', 'Bats Or Birds', 'Microbat In Flight', 'Microbat', 'Grey-headed Flying Fox',
                   'Grey Headed Flying Foxes', 'Grey Headed Flying Fox', 'Bat Sp.'],
    'Red fox': ['Fox'],
    'Glider': ['Glider - Gliding', 'Glider (Seen Airborne Only)', 'Glider Gliding', 'Glider Sp.', 'Glider And Wombat',
               'Small Glider', 'Large Glider (Greater Glider/Yellow Bellied Glider)', 'Small Other - Possible Glider',
               'Squirrel Glider', 'Sugar\Squirrel Glider'],
    'Goat': ['Goats', 'Goat Residual Body Heat Marks ?', 'Goats (Probable)', 'Goats Off Transect', 'Sheep Or Goat',
             'Goat (X3)', 'Sheep/Goat'],
    'Greater Glider': ['Greater Gliders', 'Greater Glider? Plus 2X Ground',
                       'Probable Greater Glider (Greater Or Yellow-Bellied) Plus Sugar Glider. Cool Footage',
                       'Greater Glider And Microbat', 'Possums ? Likely Greater Gliders',
                       'Greater Glider + 4 Uncertain Canopy (Possums, Gliders, Birds?)',
                       'Probable Greater Glider + Wombat', 'Greater Glider Moving Around Good Video',
                       'Greater Glider/ Brushie', 'Greater Glider/Brush-Tailed Possum', 'Greater Glider (X2)'],
    'Ground Species': ['2 Ground Unsure Medium Size - Review?', 'Unknown Ground', 'Macro? Ground',
                'Ground Macro?', 'Ground',
               'Ground. Not Animal?', 'Small Ground', 'Small Ground. Unknown', 'Small Ground Mammal', 'Ground Mammal',
               'Ground/ Shrub??', 'Ground Unknown', 'Small Ground/ Sub -Canopy Unknown', 'Ground, Macropod',
               'Ground/ Sub-Canopy? Possum/ Macropod?', 'Ground Unknonw', 'Small Ground Unknown',
               'Small Ground Sub-Canopy', 'Unknown Large Ground Detection At Base Of Tree - Sleeping Mammal/S',
               'Unknown Large Ground Detection Under Tree', 'Sleeping Large Mammal/S ?',
               'Unknown Small Ground Detection', 'Small Ground Detections', 'Ground Sp.', 'Small Ground Detection',
               'Ground Sp', 'Small', 'Unsure', 'Australian Brushturkey', 'Brush Turkey', 'Aus Brushturkeys', 'Cow',
                       'Cows', 'Dog', 'Dogs', 'Echidna', 'Australian Brush-Turkey', 'Broad-Toothed Rat', 'Emu',
                'Frog - Tricky To Identify To Species :)'],
    'Horse': ['Horses', 'Horse/Deer', 'Horse/Pig/Other', 'Horse/Pig'],
    'Koala': ['Koala (Same Koala)', 'Koala With Joey',
              'Unknown (Low Probability Koala)'],
    'Kreffts Glider': ['Krefts Glider'],
    'Macropod': ['Small Macropod', 'Macropod?', 'Macropod ?', 'Ground Macropod', 'Macropods', 'Macropod (With Joey)',
                 'Macropod With Joey', 'Ground Prob Macropod', 'Maybe Macropod', 'Probably Macropod',
                 'Macropod And 2 Small Unkown', 'Macropod (X2)', 'Macropod (X3)', 'Macropod (?)', 'Macropod X3',
                 'Unknown, Medium (Sleeping Macropod?)', 'Wallaby/Potoroo?', 'Medium Unknown (Likely Macropod)',
                 'Macropod (Large, Grey Kangaroo From Size)', 'Macopod', 'Macropod And 2 Small Ground Detections'],
    'Pademelon': ['Paddy Melon', 'Pademelon/ Parma Wallaby', 'Pademelon/Parma'],
    'Potoroo': ['Potoroo?'],
    'Possum': ['Possum/ Glider', 'Possum / Glider', 'Possum And 2 Macropods', 'Possum / Glider Plus Wallaby',
               'Sub-Canopy Possum', 'Possum/S', 'Possum/ Greater Glider', 'Possum / Greater Glider',
               'Small Possum/ Glider', 'Possum?', 'Maybe Possum (Check Vid?)', 'Glider/ Possum, Unsure',
               'Possum/ Glider - Cant Get Lower To Confirm', 'Arboreal Unsure (Couldn’T Get Lower) Small, .Ikely Possum',
               'Possums', 'Small Arboreal, Cant Get Closer - Possum?', 'Possum Or Glider', 'Greater Glider/Possum',
               'Glider/Possum', 'Possum Sp.', 'Likely Possum', 'Possum/Glider', 'Possum Maybe Quoll?', 'Possum (X1)',
               'Possum (X2)', 'Unknown (Possum)', 'Possum (X3)', 'Unknown (Small, Likely Possum)',
               'Mammal (Likely Possum)', 'Small Unknown (Likely Possum)', 'Possum/Cat', 'Possum Or Tree Hollow',
               'Brushtail/Ringtail', 'Short-eared Possum', 'Short-Eared Possum W/ Pouch Young', 'Short-Eared Possum'],
    'Quoll': ['Quoll?', 'Quoll/Cat/Fox', 'Possum/Quoll'],
    'Sugar Glider': ['Sugar/ Squirrel Glider', 'Glider - Sugar/ Squirrel?'],
    'Swamp Wallaby': [],
    'Rabbit': ['Rabbits'],
    # 'Termite Nest': ['Termite Mound', 'Termite', 'Arboreal Termite Nest?', 'Tree Growth/ Termites', 'Termite Or Hollow'],
    'Tree Hollow': ['Animal In Chimney Hollow', 'Hollow Possible Occupants', 'Tree Hollow To Rd',
                    'Vertical Hollow', 'Tree Hollow/Bee Hive/Temrites', 'Hollow Plus Maybe Unknown Arboreal', 'Hollow ?',
                    'Occupied Hollow', 'Chimney Tree Hollow', 'Chimney Hollow', 'Chimney Hollows', 'Stag Hollow',
                    'Occupied Hollow (In Fallen Stag)', 'Hollow', 'Termite Mound', 'Termite', 'Arboreal Termite Nest?',
                    'Tree Growth/ Termites', 'Termite Or Hollow', 'Termite Nest'],
    'Yellow-bellied Glider': ['Glider (Prob Yellow-Bellied)',
                              'Several Gliders/ Possums. 4 Probable Yellow-Bellied Gliders? Below (One Seen In Flight) Plus One Sugar Glider At Eye Level',
                              'Yellow-Bellied Glider', 'Yellow Belly Glider', 'Yellow Glider'],
    'Wallaby': ['Wallaby And Other Small Ground Mammals?', 'Maybe Wallaby', 'Wallaby (Multiple)', 'Wallabies',
                'Wallaby (X2)', 'Red-necked Wallaby', 'Red Necked Wallaby', 'Red-Necked Wallaby', 'Rock Wallaby',
                'Hill Wallaroo'],
    'Wombat': ['2 Macropod 1 Wombat', 'Wombat And Wallaby', 'Wombat And Macropod?', 'Wombats',
               'Macropods And Wombat (3 Animals)', 'Wombat/ Deer?', 'Wombat?', 'Wombat Or Deer?',
               'Uncertain, Maybe Wombat', 'Pig Or Wombat', 'Unknown (Wombat)', 'Wombat (X2)',
               'Wombat And Small Unidentified Ground'],
    'no_detection': ['ns west start terrible reception, difficult to descend for closer inspection', 'dummy', 'no detection'],
}

broad_species_name_map = {
    'Other': ['Arboreal Species', 'Aerial Species', 'Bird Species', 'Cat', 'Red Fox', 'Goat', 'Horse', 'Pademelon',
              'Potoroo', 'Quoll'],
    'Possum': ['Brushtail Possum', 'Ringtail Possum'],
    'Kangaroo': ['Eastern Grey Kangaroo'],
    'Glider': ['Feathertail Glider', 'Greater Glider', 'Kreffts Glider', 'Sugar Glider', 'Yellow-bellied Glider']
}

to_remove = ['Dummy', 'Human', 'Bulge On Branch', 'Human', 'No Detection', 'Uncertain',
             'Cannot Tell? Wasp Nest?', 'Possibly Hot Rocks', 'Rocks?', 'Rock', 'Maybe Rock?', 'Hbt',
             'Ns West Start Terrible Reception, Difficult To Descend For Closer Inspection',
             'Other - Add Details In Notes', 'NaN', '', ' ', 'Squirrel', 'Unknown - Not A Koala', 'Unknown (X2)',
             'Unknown (Fast?)', 'Unknown, Small', 'Unvalidated', 'Validate Not Found', 'Small Mammal (X3)',
             '2X Small Mammal', 'Small Mammal', 'Small Mammal (X2)', 'Small Unknown', 'Small Mammal Sp', 'Smmall Mammal',
             'Canopy', 'Mammal', 'Small Detection', 'Low', '', 'nan', 'NaN', 'Other', 'Unknown']

doubles = ['2 Macropod 1 Wombat', 'Possum And 2 Macropods', 'Wombat And Wallaby',
           'Pademelon/ Parma Wallaby (Plus Koala)', 'Greater Glider? Plus 2X Ground',
           'Several Gliders/ Possums. 4 Probable Yellow-Bellied Gliders? Below (One Seen In Flight) Plus One Sugar Glider At Eye Level',
           'Greater Glider And Microbat', 'Greater Glider + 4 Uncertain Canopy (Possums, Gliders, Birds?)',
           'Probable Greater Glider + Wombat', 'Wombat And Macropod?',
           'Medium Sized Unknown Thermal - Ground/ Very Low Arboreal + Small Roosting Birds',
           'Macropods And Wombat (3 Animals)', 'Ringtail And 3 Small Ground Mammals', 'Glider And Wombat',
           'Wombat And Small Unidentified Ground']

probability_map = {
    'Low': ['0%'],
    'Med': ['Medium', 'Probable'],
    'High': ['high', 'Med/High'],
    '100%': ['Certain', 'Definite']
}

species_category_map = {
    'Arboreal Species': ['Aboreal', 'Abroreal', 'Arboeal', 'Arborea', 'Arboreal (Sub-Canopy)', 'Arboreal Mid-Canopy',
                         'Arboreal Sub-Canopy', 'Arboreal/Canopy', 'Arboreal/Ground', 'Arboreal?', 'Arboreral',
                         'Canopy', 'Ground/ Sub Canopy', 'Ground/ Sub-Canopy', 'Ground/Subcanopy', 'Mid-Canopy',
                         'Arboreal', 'Arboreal Sp.', 'Arboreal Sp. Small', 'Koala', 'Possum', 'Brush Tail',
                         'Ring Tail', 'Greater Glider', 'Sugar Glider'],
    'Aerial Species': ['Aerial', 'Airborne', 'Airborne, Arboreal', 'Bird', 'Flying-Fox'],
    'Ground Species': ['Deer', 'Ground', 'Ground?', 'Wombat'],
    'Other': ['Hollow', 'No Detection', 'Other', 'Other - Add Details In Notes', 'Stag Hollow', 'Uncertain', 'Unknown',
             'Unsure', 'nan', 'Both', 'NaN', 'None']
}

species_category_corrections = {
    'Aerial Species': ['Musk Lorikeet', 'Kookaburra', 'Flying Fox', 'Microbat', 'Sooty Owl', 'Parrot', 'Cockatoo',
                       'Yellow-tailed Black Cockatoo', 'Dusky Woodswallow', 'Powerful Owl', 'Grey-headed Flying Fox',
                       'Common Bronzewing', 'Magpie', 'Bat', 'Bird Species'],
    'Arboreal Species': ['Mountain Brushtail Possum', 'Ringtail Possum', 'Short-eared Possum', 'Kreffts Glider',
                         'Yellow-bellied Glider', 'Glider', 'Feathertail Glider', 'Greater Glider', 'Sugar Glider',
                         'Possum'],
    'Ground Species': ['Cat', 'Fox', 'Cow', 'Goat', 'Rodent', 'Deer', 'Wombat', 'Bandicoot', 'Ground Species', 'Horse',
                       'Red fox', 'Dingo'],
    'Macropod': ['Potoroo', 'Pademelon', 'Rock Wallaby', 'Kangaroo', 'Wallaby', 'Macropod', 'Eastern Grey Kangaroo',
                 'Swamp Wallaby'],
    'Other': ['Tree Hollow']
}

null_species_category_corrections = {
    'Brushtail Possum': 'Arboreal Species',
    'Possum': 'Arboreal Species',
    'Ringtail Possum': 'Arboreal Species',
    'Deer': 'Ground Species',
    'Macropod': 'Macropod',
    'Unknown': 'None',
    'Tree Hollow': 'None',
    'Bird Species': 'Aerial Species',
    'Koala': 'Arboreal Species',
    'Wallaby': 'Macropod',
    'Glider': 'Arboreal Species',
    'Sugar Glider': 'Arboreal Species',
    'Horse': 'Ground Species',
    'Quoll': 'Ground Species',
    'Goat': 'Ground Species',
    'Rabbit': 'Ground Species',
    'Wombat': 'Ground Species',
    'Pig': 'Ground Species',
    'Swamp Wallaby': 'Macropod'
}

convert_to_other = ['Ground Species', 'Arboreal Species', 'Aerial Species', 'Macropod']

species_categories_to_display = {
    'Aerial Species': ['Flying Fox', 'Other'],
    'Arboreal Species': ['Possum', 'Glider', 'Koala', 'Other'],
    'Ground Species': ['Wombat', 'Deer', 'Rabbit', 'Goat', 'Dingo', 'Other'],
    'Macropod': ['Wallaby', 'Potoroo', 'Kangaroo'],
    'Other': ['Tree Hollow']
}

species_to_display = ['Flying Fox', 'Possum', 'Glider', 'Koala', 'Wombat', 'Deer', 'Rabbit', 'Goat', 'Kangaroo',
                      'Wallaby', 'Potoroo', 'Dingo']

