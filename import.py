import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import time

def main():
    player_dict = players.get_players()
    player_id = [0]
    for i in range(len(player_dict)):
        player_id.append(player_dict[i].get('id'))

        player_stats = [0]
        #for i in range(len(player_id)):
        #    career = playercareerstats.PlayerCareerStats(player_id=player_id[i])
        #    career = career.get_data_frames()[0]
        #    player_stats[i] = career
        #    print(career)

    time.sleep(.600)
    career = playercareerstats.PlayerCareerStats(player_id=player_id[1])
    career = career.get_data_frames()[0]
    player_stats[0] = career
    print(career)

if __name__ == "__main__":
    main()
