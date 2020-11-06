import pandas as pd
from pandas import DataFrame
import numpy as np
import csv
import requests
from bs4 import BeautifulSoup
from tqdm import trange
pd.set_option('display.max_columns', 999)

#this entire program shoudl be rewritten using basketball refrence scraper API
#nba is too slow


def main():
    def_rating = career_def_rating()
    off_rating = career_off_rating()
    def_playoff_rating = career_def_playoffs()
    off_playoff_rating = career_off_playoffs()
    winshare_48 = winshare_per_48()
    winshare_48_playoff = winshare_48_playoffs()

    def_rating.to_csv("/Users/lucasmunson/Desktop/nokogiri tutorial/GOAT Calc/player_data/def_rating.csv")
    off_rating.to_csv("/Users/lucasmunson/Desktop/nokogiri tutorial/GOAT Calc/player_data/off_rating.csv")
    def_playoff_rating.to_csv("/Users/lucasmunson/Desktop/nokogiri tutorial/GOAT Calc/player_data/def_playoff_rating.csv")
    off_playoff_rating.to_csv("/Users/lucasmunson/Desktop/nokogiri tutorial/GOAT Calc/player_data/off_playoff_rating.csv")
    winshare_48.to_csv("/Users/lucasmunson/Desktop/nokogiri tutorial/GOAT Calc/player_data/winshare_48.csv")
    winshare_48_playoff.to_csv("/Users/lucasmunson/Desktop/nokogiri tutorial/GOAT Calc/player_data/winshare_48_playoff.csv")

def career_def_rating():
    page = requests.get('https://www.basketball-reference.com/leaders/def_rtg_career.html')
    df_list = pd.read_html(page.content)

    def_rating = df_list[0]
    def_rating['Player'] = def_rating['Player'].str.replace('*','')
    return def_rating

def career_off_rating():
    page = requests.get('https://www.basketball-reference.com/leaders/off_rtg_career.html')
    off_list = pd.read_html(page.content)

    off_rating = off_list[0]
    off_rating['Player'] = off_rating['Player'].str.replace('*','')
    return off_rating

def career_def_playoffs():
    page = requests.get('https://www.basketball-reference.com/leaders/def_rtg_career_p.html')
    def_playoffs_list = pd.read_html(page.content)

    def_playoff_rating = def_playoffs_list[0]
    def_playoff_rating['Player'] = def_playoff_rating['Player'].str.replace('*','')
    return def_playoff_rating

def career_off_playoffs():
    page = requests.get('https://www.basketball-reference.com/leaders/off_rtg_career_p.html')
    off_playoffs_list = pd.read_html(page.content)

    off_playoff_rating = off_playoffs_list[0]
    off_playoff_rating['Player'] = off_playoff_rating['Player'].str.replace('*','')
    return off_playoff_rating

def winshare_per_48():
    page = requests.get('https://www.basketball-reference.com/leaders/ws_per_48_career.html')
    winshare_48_list = pd.read_html(page.content)

    winshare_48 = winshare_48_list[0]
    winshare_48['Player'] = winshare_48['Player'].str.replace('*','')
    return winshare_48

def winshare_48_playoffs():
    page = requests.get('https://www.basketball-reference.com/leaders/ws_per_48_career_p.html')
    winshare_48_playoff = pd.read_html(page.content)

    winshare_48_playoff = winshare_48_playoff[0]
    winshare_48_playoff['Player'] = winshare_48_playoff['Player'].str.replace('*','')
    return winshare_48_playoff

if __name__ == "__main__":
    main()
