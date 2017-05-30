import bs4, requests
import pandas as pd
from Website_to_CSV_Functions import *
from Player_Class import *

def Get_Players_and_Ids_From_CSV_File(filename):
    Players_temp={}
    with open(filename,'r') as fout:
        reader = csv.reader(fout)
        for row in reader:
            if row[0] != 'Player Id':
                player = Player()
                player.Assign_Variables_From_CSV(row)
                Players_temp[player.player_id]=player
    return Players_temp

# NFL does not have stats for all players
def Check_for_Stats_Webpage(player,stats_type):
    profile_url = 'http://www.nfl.com/player/'+player.player_id+'/profile'
    res = requests.get(profile_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')    
    
    Has_Stats_Page = False
    for div in soup.find_all('div',{'id':'player-profile-tabs'}):
        if stats_type in div.text:
            Has_Stats_Page = True
    return Has_Stats_Page

# Only one should be executed based on if you want to get the player names and
# ids from a csv file or from the website.
Players = Get_and_Store_All_Players_Names_and_Ids('Player_Ids_Urls.csv')
#Players = Get_Players_and_Ids_From_CSV_File('Player_Ids_Urls.csv')


# Get Basic Statistics
count = 1
for player_id in Players:
    player = Player_Basic_Stats(Players[player_id])
    player.Get_and_Store_Basic_Stats('Basic_Stats.csv')
    if count % 10 == 0:
        print('Processed basic stats for %d out of %d players' % (count,len(Players)))
    count+=1
    
# Get Career Stats
count = 1
for player_id in Players:
    player = Career_Stats(Players[player_id])
    if Check_for_Stats_Webpage(player,'Career Stats'):
        player.Get_and_Store_Career_Stats()
    if count % 10 == 0:
        print('Processed career stats for %d out of %d players' % (count,len(Players)))
    count+=1

# Get Game Logs
count = 1
for player_id in Players:
    player = Game_Logs(Players[player_id])
    if Check_for_Stats_Webpage(player,'Game Logs'):
        player.Get_and_Store_Game_Logs()
    if count % 10 == 0:
        print('Processed game logs for %d out of %d players' % (count,len(Players)))
    count+=1


