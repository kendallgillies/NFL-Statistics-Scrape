import bs4, os.path
from Player_Class import *
from Website_to_CSV_Functions.NFL_Glossary import *
from Website_to_CSV_Functions.Functions_Needed_For_All_Stats import *

class Career_Stats(Player):
    def __init__(self,player):
        self.player_id = player.player_id
        self.name = player.name
        self.position = None
    
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
    
    def Get_Table_Header(self,stats_type,thead_tags):
        Has_Col_Cats = False
        for thead in thead_tags:
            for tr in thead.find_all('tr',class_='player-table-key'):
                td_tags = tr.find_all('td')
                if 'two-row-top' in tr.attrs['class']:     
                    Col_Cats = self.Get_Column_Categories(td_tags)
                    Has_Col_Cats = True
                else:
                    Col_Names = self.Get_Column_Names(td_tags)
        
        if Has_Col_Cats:
            Header = NFL_Shorthand_to_Headers(stats_type,Col_Cats,Col_Names)
        else:
            Header = NFL_Shorthand_to_Headers(stats_type,[],Col_Names)
        
        return Header
        
    def Get_File_Name_And_Header_Length(self,thead_tags,stats_type):
        File_Names = {'Passing':'Career_Stats_Passing.csv',
            'Rushing':'Career_Stats_Rushing.csv',
            'Receiving':'Career_Stats_Receiving.csv',
            'Defensive':'Career_Stats_Defensive.csv',
            'Fumbles':'Career_Stats_Fumbles.csv',
            'Kick Return':'Career_Stats_Kick_Return.csv',
            'Punt Return':'Career_Stats_Punt_Return.csv',
            'Offensive Line':'Career_Stats_Offensive_Line.csv',
            'Field Goal Kickers':'Career_Stats_Field_Goal_Kickers.csv',
            'Punting Stats':'Career_Stats_Punting.csv',
            'Kickoff Stats':'Career_Stats_Kickoff.csv'}    

        if not os.path.exists(File_Names[stats_type]):        
            Header = ['Player Id','Name','Position']+self.Get_Table_Header(stats_type,thead_tags)
            self.New_CSV_File(File_Names[stats_type],Header)   
        else:
            with open(File_Names[stats_type],newline='') as fout:
                reader = csv.reader(fout)
                Header = next(reader)
        # The NFL website does not use the player id, name and position in 
        # their headers so it is subtracted from the header length
        return [File_Names[stats_type],len(Header)-3]
     
    def Get_and_Store_Career_Stats(self):
        url = 'http://www.nfl.com/player/'+self.player_id+'/careerstats'
        soup = Get_HTML_Document(url,{})  
        
        self.Get_Player_Number_and_Position()

        for table in soup.find_all('table'):
            for div in table.find_all('div'):
                stats_type = div.text
            
            Stats = []
            filename, header_length = self.Get_File_Name_And_Header_Length(table.find_all('thead'),stats_type)
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
            
