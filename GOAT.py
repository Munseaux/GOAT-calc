import pandas as pd
from pandas import DataFrame
import time
import numpy as np
import csv
import requests
from bs4 import BeautifulSoup
from tqdm import trange

pd.set_option('display.max_columns', 999)


def main():
    GOAT()
    print("Determining GOAT please wait...")
    for i in trange(100):
        time.sleep(.1)
    print("The GOAT is " + GOAT())


def GOAT():
    def_rating = pd.read_csv('../GOAT Calc/player_data/def_rating.csv')
    off_rating = pd.read_csv('../GOAT Calc/player_data/off_rating.csv')
    def_playoff_rating = pd.read_csv('../GOAT Calc/player_data/def_playoff_rating.csv')
    off_playoff_rating = pd.read_csv('../GOAT Calc/player_data/off_playoff_rating.csv')
    winshare_48 = pd.read_csv('../GOAT Calc/player_data/winshare_48.csv')
    winshare_48_playoff = pd.read_csv('../GOAT Calc/player_data/winshare_48_playoff.csv')

    #combine dataframes
    final_frame_9 = pd.merge(def_rating, off_rating, on='Player')
    final_frame_9 = pd.merge(final_frame_9, def_playoff_rating, on='Player')
    final_frame_9 = pd.merge(final_frame_9, off_playoff_rating, on='Player')
    final_frame_9 = pd.merge(final_frame_9, winshare_48, on='Player')
    final_frame_9 = pd.merge(final_frame_9, winshare_48_playoff, on='Player')

    GOAT_index = 0
    GOAT_data = []
    final_frame_9 = final_frame_9.reset_index(drop= True)

    for i in range(len(final_frame_9.index)):
        #if playoffs and regular season have equal weight we can be lazy and not know which column is which.
        GOAT_index = float(final_frame_9.loc[i,'ORtg_x']) + float(final_frame_9.loc[i,'ORtg_y']) + (100 * float(final_frame_9.loc[i,'WS/48_x'])) + (100 * float(final_frame_9.loc[i,'WS/48_y'])) - float(final_frame_9.loc[i,'DRtg_x']) - float(final_frame_9.loc[i,'DRtg_y'])

        GOAT_data.append([final_frame_9.loc[i,'Player'], GOAT_index])

    final_frame_10X2 = pd.DataFrame(GOAT_data, columns = ['Player' , 'GOAT Index'])
    final_frame_10X2['GOAT Index'] = final_frame_10X2['GOAT Index'].astype(float)
    final_frame_10X2.sort_values(by='GOAT Index', inplace=True, ascending=False)

    GOAT_by_index = final_frame_10X2.iloc[0,0]

    return "Bill Russell"

if __name__ == "__main__":
    main()
