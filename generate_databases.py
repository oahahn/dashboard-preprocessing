import pandas as pd
from data_cleaning import clean_data

if __name__ == '__main__':
    det_match = pd.read_csv('det_match.csv')
    det_match = clean_data(det_match)
    det_match.to_csv('det_match_clean.csv')