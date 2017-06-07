import csv, bs4, re
from Website_to_CSV_Functions.Functions_Needed_For_All_Stats import *

class Player(object):
    def __init__(self):
        self.name = None
        self.player_id = None
        self.current_status = None 
        self.years_played = None
        self.number = None
        self.position = None
        
    def __repr__(self):
        return "<Player: %s>" % self.name
    
    def New_CSV_File(self,filename,headers):
        with open(filename,'w',newline='') as fin:
            writer = csv.writer(fin)
            writer.writerow(headers)

    def Write_Stats_to_CSV(self,filename,Stats):
        with open(filename,'a',newline='') as fin:
            writer = csv.writer(fin)
            writer.writerow(Stats)

    # row is read in from csv file    
    def Assign_Variables_From_CSV(self,row):
        self.player_id = row[0]
        self.name = row[1]
        self.current_status = row[2]
        self.years_played = row[3]

    def Get_Player_Number_and_Position(self):
        profile_url = 'http://www.nfl.com/player/'+self.player_id+'/profile'
        soup = Get_HTML_Document(profile_url,{})
        for player_num in soup.find_all('span',class_ = 'player-number'): 
            try:
                player_num = player_num.text
                player_num = re.split('#| ',player_num)
            
                self.number = player_num[1] if player_num[1] != '' else None
                self.position = player_num[2]
            except:
                pass
                
