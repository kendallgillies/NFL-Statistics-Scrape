import bs4, re, os.path
from Player_Class import *
from Website_to_CSV_Functions.Functions_Needed_For_All_Stats import *

class Player_Basic_Stats(Player):
    def __init__(self,player):
        self.player_id = player.player_id
        self.name = player.name
        self.current_status = player.current_status
        self.years_played = player.years_played
        self.number = None
        self.position = None
        self.current_team = None
        self.height = None
        self.weight = None
        self.age = None
        self.birthday = None
        self.birth_place = None
        self.college = None
        self.high_school = None
        self.high_school_location = None
        self.experience = None
        
    def Get_Player_Team(self,div_bio):
        player_team_tag = div_bio.find('p',class_ = 'player-team-links')
        try:
            team = player_team_tag.text
            team = team.split('|')
            team = team[0].strip()
            self.current_team = team
        except:
            pass
    
    def Get_Height(self,s):
        s = re.split(':|-| ',s)
        while '' in s: s.remove('')
        if s:
            ft = int(s[0])
            inch = int(s[1])
            self.height = 12*ft + inch
    
    def Get_Weight(self,s):
        s = re.split(':|-| ',s)
        while '' in s: s.remove('')
        if s:
            self.weight = int(s[0])
            
    def Get_Age(self,s):
        s = re.split(':|-| ',s)
        while '' in s: s.remove('')
        if s:
            self.age = int(s[0])
            
    def Get_Birth_Info(self,s):
        s = re.split(':|-| ',s)
        while '' in s: s.remove('')
        if s:
            self.birthday = s[0]
            if len(s) >= 2:
                self.birth_place = ' '.join(s[1:len(s)])
    
    def Get_College_Info(self,s):
        s = re.split(':| ',s)
        while '' in s: s.remove('')
        if s:
            s = ' '.join(s)
            self.college = s
    
    def Get_Experience(self,s):
        s = re.split(':| ',s)
        while '' in s: s.remove('')
        if s:
            s = ' '.join(s)
            self.experience = s
    
    def Get_High_School_Info(self,s):
        s = re.split(' HS| \[|: |;',s)
     
        while '' in s: s.remove('')
    
        if len(s) > 0 and s[0] != ':':
            self.high_school = s[0] + ' HS'
        
        if len(s) > 1:
            self.high_school_location = s[1].strip('[]')
    
    def Get_and_Store_Basic_Stats(self,filename):
        if not os.path.exists(filename):        
            Basic_Stats_Headers = ['Age','Birth Place','Birthday','College',
               'Current Status','Current Team','Experience','Height (inches)',
               'High School','High School Location','Name','Number','Player Id',
               'Position','Weight (lbs)','Years Played']
            self.New_CSV_File(filename,Basic_Stats_Headers)        
            
        profile_url = 'http://www.nfl.com/player/'+self.player_id+'/profile'
        soup = Get_HTML_Document(profile_url,{})   
    
        counter = 1
        fn_name = None
        Player_Stats = {'Height':self.Get_Height,
                        'Weight':self.Get_Weight,
                        'Age':self.Get_Age,
                        'Born':self.Get_Birth_Info,
                        'College':self.Get_College_Info,
                        'Experience':self.Get_Experience,
                        'High School':self.Get_High_School_Info}
    
        counter = 1
        for div_bio in soup.find_all('div', id = 'player-bio'):
            self.Get_Player_Team(div_bio)
            for p in div_bio.find_all('p'):
                strings = p.stripped_strings
                for s in strings:
                    fn_name = s if counter%2==0 else fn_name
                    if counter%2==1 and fn_name in Player_Stats.keys():
                        Player_Stats[fn_name](s)
                    counter+=1

        self.Get_Player_Number_and_Position()

        attrs = vars(self)
        basic_stats = [attrs[k] for k in sorted(attrs)]
        self.Write_Stats_to_CSV(filename,basic_stats)
    

   
    
    
