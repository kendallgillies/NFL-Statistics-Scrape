import bs4, re, os.path, string
from Player_Class import *
from Website_to_CSV_Functions.Functions_Needed_For_All_Stats import *

def Obtain_Number_of_Pages(soup,initial_url):
    Pages = [1]
    for page in soup.find_all(title=re.compile('Go to page')):
        try:
            Pages.append(int(page.contents[0]))
        except:
            pass
    return max(Pages)

def Get_Player_Name_and_Id(player,td,Players):
    for a in td.find_all('a'):
        player.name = a.text
        
        Attributes = a.attrs
        pid = Attributes['href']
        pid = pid.split('/')
        player.player_id = '/'.join([pid[2],pid[3]])
        
def Get_Players_Current_Status(player,td,Is_Current):
    Status_Abbrev = {'ACT':'Active','RES':'Injured reserve',
                     'NON':'Non football related injured reserve',
                     'SUS':'Suspended','PUP':'Physically unable to perform',
                     'UDF':'Unsigned draft pick','UFA':'Unsigned free agent',
                     'EXE':'Exempt'}
    if Is_Current:
        player.current_status = Status_Abbrev[td.text]
    else:
        player.current_status = 'Retired'

def Get_Years_Played(player,td,Is_Current):
    if not Is_Current:
        player.years_played = td.text

def Get_Player_Information(Players,td_tags,col_num,name_index,status_index,
                           years_played_index,Is_Current,filename):
    count = 0
    player=Player()
    for td in td_tags:
        index = count % col_num
        if index == name_index:
            Get_Player_Name_and_Id(player,td,Players)
        elif index == status_index:
            Get_Players_Current_Status(player,td,Is_Current)
        elif index == years_played_index:
            Get_Years_Played(player,td,Is_Current)
        elif index == col_num-1:
            Players[player.player_id] = player
            if not os.path.exists(filename):        
                headers = ['Player Id','Name','Current Status','Years Played']
                player.New_CSV_File(filename,headers)
            Stats = [player.player_id,player.name,player.current_status,player.years_played]
            player.Write_Stats_to_CSV(filename,Stats)
            player=Player()
        count+=1   
   
def Obtain_Players_And_Status(initial_url,url_parameters,Max_Page,Players,soup,filename):
    for page_number in range(1,Max_Page+1):
        # NFL website parameter name for page number
        url_parameters['d-447263-p'] = page_number
        soup = Get_HTML_Document(initial_url,url_parameters)
        
        for table in soup.find_all('table', id = 'result'):
            td_tags = table.find_all('td')
            if url_parameters['playerType'] == 'current':
                Get_Player_Information(Players,td_tags,13,2,3,4,True,filename)
            else:
                Get_Player_Information(Players,td_tags,12,0,1,2,False,filename)

# Storing happens when Get_Player_Information is called
def Get_and_Store_All_Players_Names_and_Ids(filename):
    Players = {}
    PlayerType = ['current','historical']
    for playertype in PlayerType:
        for Last_Name_Beginning in list(string.ascii_uppercase):
            print('Getting %s players whose last name starts with %s' % (playertype,
                                                             Last_Name_Beginning))
            
            url_parameters = {'category':'lastName','filter':Last_Name_Beginning,
                          'playerType':playertype}
            initial_url = 'http://www.nfl.com/players/search'
            soup = Get_HTML_Document(initial_url,url_parameters)
    
            Max_Page = Obtain_Number_of_Pages(soup,initial_url)
    
            Obtain_Players_And_Status(initial_url,url_parameters,Max_Page,Players,
                                      soup,filename)
    return Players
 

