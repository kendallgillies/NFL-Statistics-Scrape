import bs4, os.path
from Player_Class import *
from Website_to_CSV_Functions.NFL_Glossary import *
from Website_to_CSV_Functions.Functions_Needed_For_All_Stats import *

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

    def Get_Column_Categories(self,td_tags):
        Col_Cats = []
        for td in td_tags:
            if 'colspan' in td.attrs.keys():
                Col_Cats += [td.text]*int(td.attrs['colspan'])
            else:
                Col_Cats.append(td.text)            
            
        return Col_Cats
    
    def Get_Column_Names(self,td_tags):
        Col_Names = []
        for td in td_tags:
            Col_Names.append(td.text)
        return Col_Names
    
    def Get_Table_Header(self,thead_tags):
        Has_Col_Cats = False
        for thead in thead_tags:
            for tr in thead.find_all('tr'):
                td_tags = tr.find_all('td')
                if 'player-table-header' in tr.attrs['class']:     
                    Col_Cats = self.Get_Column_Categories(td_tags)
                else:
                    Col_Names = self.Get_Column_Names(td_tags)
        
        Header = NFL_Shorthand_to_Headers('GET_CATS',Col_Cats,Col_Names)
        
        return Header
    
    def Get_File_Identifier(self,thead_tags):
        for thead in thead_tags:
            file_identifier = [td.text for td in thead.find('tr').find_all('td')]
        return file_identifier[2:]
        
    def Get_File_Name_And_Header_Length(self,thead_tags):
        file_identifier = self.Get_File_Identifier(thead_tags)
        
        if file_identifier == ['Passing', 'Rushing', 'Fumbles']:
            filename = 'Game_Logs_Quarterback.csv'
        elif file_identifier == ['Rushing', 'Receiving', 'Fumbles']:
            filename = 'Game_Logs_Runningback.csv'
        elif file_identifier == ['Receiving', 'Rushing', 'Fumbles']:
            filename = 'Game_Logs_Wide_Receiver_and_Tight_End.csv'
        elif file_identifier == []:
            filename = 'Game_Logs_Offensive_Line.csv'
        elif file_identifier == ['Tackles', 'Interceptions', 'Fumbles']:
            filename = 'Game_Logs_Defensive_Lineman.csv'
        elif file_identifier == ['Overall FGs', 'PAT', 'Kickoffs']:
            filename = 'Game_Logs_Kickers.csv'
        elif file_identifier == ['Punter']:
            filename = 'Game_Logs_Punters.csv'   

        if not os.path.exists(filename):        
            NFL_Headers = self.Get_Table_Header(thead_tags)
            Header = ['Player Id','Name','Position','Year','Season']+NFL_Headers
            self.New_CSV_File(filename,Header)   
        else:
            with open(filename,newline='') as fout:
                reader = csv.reader(fout)
                Header = next(reader)
        # The NFL website does not use the player id, name and position in 
        # their headers so it is subtracted from the header length
        return [filename,len(Header)-3]
       
    def Get_and_Store_Game_Logs(self):
        url = 'http://www.nfl.com/player/'+self.player_id+'/gamelogs'
        soup = Get_HTML_Document(url,{})  

        self.Get_Player_Number_and_Position()
        
        game_years = self.Get_Game_Years(soup)
        Stats = []
        for year in game_years:
            soup = Get_HTML_Document(url,{'season':year})    
            for table in soup.find_all('table'):
                headers = [td.text for td in table.find('tr').find_all('td')]
                season = headers[0]
                
                thead_tags = table.find_all('thead')
                filename, header_length = self.Get_File_Name_And_Header_Length(thead_tags)
               
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
