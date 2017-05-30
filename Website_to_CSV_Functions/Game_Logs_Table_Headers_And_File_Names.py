import os.path
# Not all players have a position assigned to them; therefore identifying the
# type of game logs is done through the table headers on the website.
def Get_File_Name_And_Header_Length_GL(headers,player):
    Player_Info_Headers = ['Player Id','Name','Position']
    
    Stats_For_All = ['Year','Season','Week','Game Date','Home or Away','Opponent',
         'Outcome','Score','Games Played','Games Started']
    
    if headers == ['Passing', 'Rushing', 'Fumbles']:
        Stats = ['Passes Completed','Passes Attempted','Completion Percentage',
           'Passing Yards','Passing Yards Per Attempt','TD Passes',
           'Ints','Sacks','Sacked Yards Lost','Passer Rating',
           'Rushing Attempts','Rushing Yards','Yards Per Carry',
           'Rushing TDs','Fumbles','Fumbles Lost']
        filename = 'Game_Logs_Quarterback.csv'
        
    elif headers == ['Rushing', 'Receiving', 'Fumbles']:
        Stats = ['Rushing Attempts','Rushing Yards','Yards Per Attempt',
            'Longest Rushing Run','Rushing TDs','Receptions',
            'Receiving Yards','Yards Per Reception','Longest Reception',
            'Receiving TDs','Fumbles','Fumbles Lost']
        filename = 'Game_Logs_Runningback.csv'
        
    elif headers == ['Receiving', 'Rushing', 'Fumbles']:
        Stats = ['Receptions','Receiving Yards',
            'Yards Per Reception','Longest Reception','Receiving TDs',
            'Rushing Attempts','Rushing Yards','Yards Per Attempt',
            'Longest Rushing Run','Rushing TDs','Fumbles','Fumbles Lost']
        filename = 'Game_Logs_Wide_Receiver_and_Tight_End.csv'
            
    elif headers == []:
        Stats = []
        filename = 'Game_Logs_Offensive_Line.csv'
        
    elif headers == ['Tackles', 'Interceptions', 'Fumbles']:
        Stats = ['Total Tackles','Solo Tackles',
            'Assisted Tackles','Sacks','Safties','Passes Defended','Ints',
            'Int Yards','Yards Per Int',
            'Longest Int Return','Ints for TDs',
            'Forced Fumbles']
        filename = 'Game_Logs_Defensive_Lineman.csv'
        
    elif headers == ['Overall FGs', 'PAT', 'Kickoffs']:
        Stats = ['Kicks Blocked','Longest FG Made',
            'FGs Attempted','FGs Made','FG Percentage',
            'Extra Points Made','Extra Points Attempted',
            'Percentage of Extra Points Made','Extra Points Blocked',
            'Kick Offs','Average Kick Off Yardage','Touchbacks','Kick Offs Returned',
            'Average Yardage Returned']
        filename = 'Game_Logs_Kickers.csv'
        
    elif headers == ['Punter']:
        Stats = ['Punts Made','Gross Punting Yards',	
            'Net Punting Yards','Longest Punt','Gross Punting Average','Net Punting Average',	
            'Punts Blocked','Out of Bounds Punts','Downed Punts',	
            'Punts Inside 20 Yard Line','Touchbacks','Fair Catches','Punts Returned',
            'Yards Returned on Punts','TDs Returned on Punt']
        filename = 'Game_Logs_Punters.csv'
        
    else:
        print('Missed header for %s' % (player.player_id))
              
    
    Stats_Headers = Stats_For_All + Stats

    if not os.path.exists(filename):        
        Stats_Headers = Player_Info_Headers + Stats_For_All + Stats
        player.New_CSV_File(filename,Stats_Headers)   

    return [filename,len(Stats_For_All + Stats)]