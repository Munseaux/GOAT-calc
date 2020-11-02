import pandas as pd
from tqdm import trange
import time
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

def main():
    print("Determining GOAT please wait...")
    for i in trange(100):
        time.sleep(.1)
    print("The GOAT is " + GOAT())


def GOAT():
    return "Bill Russell"







#def total_offense_score(player_stats):


#def total_defense_score(player_stats):


#def total_playoff_offense(player_stats):


#def total_playoff_defense(player_stats):









if __name__ == "__main__":
    main()
