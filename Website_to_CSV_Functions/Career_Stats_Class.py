import bs4, requests, re
import pandas as pd
from Player_Class import *
from Website_to_CSV_Functions.Career_Stats_Table_Headers_And_File_Names import *

class Career_Stats(Player):
    def __init__(self,player):
        self.player_id = player.player_id
        self.name = player.name
        self.position = None
    
    def Get_and_Store_Career_Stats(self):
        url = 'http://www.nfl.com/player/'+self.player_id+'/careerstats'
        res = requests.get(url)
    
        soup = bs4.BeautifulSoup(res.text,'lxml')    
        
        self.Get_Player_Number_and_Position()

        for table in soup.find_all('table'):
            for div in table.find_all('div'):
                stats_type = div.text
                filename, header_length = Get_File_Name_And_Header_Length_CS(stats_type,self)
            
            Stats = []
            for table_body in table.find_all('tbody'):
                tr_tags = table_body.find_all('tr')
                tr_tags = filter(lambda x: x.attrs != {'class': ['datatabledatahead']},
                                     tr_tags) # Excludes total amounts
                
                for tr in tr_tags:
                    strings = tr.stripped_strings
                    for s in strings:
                        if len(Stats) == header_length-1:
                            Stats.append(s)
                            Stats = [self.player_id,self.name,self.position]+Stats
                            self.Write_Stats_to_CSV(filename,Stats)
                            Stats = []
                        else:
                            Stats.append(s)
            
