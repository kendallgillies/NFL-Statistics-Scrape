import bs4, requests
import pandas as pd
from Player_Class import *
from Website_to_CSV_Functions.Game_Logs_Table_Headers_And_File_Names import *

class Game_Logs(Player):
    def __init__(self,player):
        self.player_id = player.player_id
        self.name = player.name
        self.position= None
        
    def Get_Game_Years(self,soup):
        game_years = []
        for div in soup.find_all('div', id = 'game-log-year'):
            for option in div.find_all('option'):
                game_years.append(option.text)
        return game_years

    
    def Get_and_Store_Game_Logs(self):
        url = 'http://www.nfl.com/player/'+self.player_id+'/gamelogs'
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text,'lxml')    

        self.Get_Player_Number_and_Position()
        
        game_years = self.Get_Game_Years(soup)
        Stats = []
        for year in game_years:
            res = requests.get(url, params = {'season':year})
            soup = bs4.BeautifulSoup(res.text,'lxml')    
            for table in soup.find_all('table'):
                headers = [td.text for td in table.find('tr').find_all('td')]
                season = headers[0]

                filename, header_length = Get_File_Name_And_Header_Length_GL(headers[2:],self)
               
                In_Totals = False
                for table_body in table.find_all('tbody'):
                    for tr in table_body.find_all('tr'):
                        string = tr.stripped_strings
                        count = 0
                        Stats = [year,season]
                        for s in string:
                            if s == 'TOTAL':
                                In_Totals = True
                            if not In_Totals:
                                if len(Stats) == 4:
                                    if '@' in s:
                                        s = s.split(' ')
                                        Stats.append('Away')
                                        Stats.append(s[1].strip())
                                    else:
                                        Stats.append('Home')
                                        Stats.append(s)
                                elif len(Stats) == 7:
                                    s = s.replace('-',' to ')
                                    Stats.append(s)
                                else:
                                    Stats.append(s)
                            if len(Stats) == header_length:
                                Stats = [self.player_id,self.name,self.position]+Stats
                                self.Write_Stats_to_CSV(filename,Stats)
                                Stats = [year,season]
