import os.path

def Get_File_Name_And_Header_Length_CS(stats_type,player):
    Player_Info_Headers = ['Player Id','Name','Position']
    
    Stats_For_All = ['Year','Team','Games Played']

    Passing = ['Passes Attempted','Passes Completed',
        'Completion Percentage', 'Pass Attempts Per Game','Passing Yards',
        'Passing Yards Per Attempt','Passing Yards Per Game','TD Passes',
        'Percentage of TDs per Attempts','Ints','Int Rate','Longest Pass',
        'Passes Longer than 20 Yards','Passes Longer than 40 Yards','Sacks',
        'Sacked Yards Lost','Passer Rating']
    
    
    Rushing = ['Rushing Attempts','Rushing Attempts Per Game','Rushing Yards',
        'Yards Per Carry','Rushing Yards Per Game','Rushing TDs','Longest Run',
        'Rushing First Downs','Percentage of Rushing First Downs',
        'Rushing More Than 20 Yards','Rushing More Than 40 Yards','Fumbles']
    
    Receiving = ['Receptions','Receiving Yards','Yards Per Reception',
        'Yards Per Game','Longest Reception','Receiving TDs',
        'Receptions Longer than 20 Yards','Receptions Longer than 40 Yards',
        'First Down Receptions','Fumbles']
    
    Defensive = ['Total Tackles','Solo Tackles','Assisted Tackles',
        'Sacks','Safties','Passes Defended','Passes Intercepted','Ints for TDs',
        'Int Yards','Yards Per Int','Longest Int Return']
    
    Fumbles = ['Fumbles','Fumbles Lost','Forced Fumbles','Own Fumbles Recovered',
        'Opponent Fumbles Recovered','Own Fumble Return Yards',
        'Opponent Fumble Return Yards','Fumble Return TDs',
        'Out of Bounds Fumbles','Saftey Fumbles','Touchback Fumbles']
    
    Kick_Return = ['Returns','Return Yards','Yards Per Return','Longest Return',
        'Returns for TDs','Returns Longer than 20 Yards',
        'Returns Longer than 40 Yards','Fair Catches','Fumbles']
    
    Punt_Return = ['Returns','Yards Returned','Yards Per Return','Longest Return',
        'TD Returns','Returns Longer than 20 Yards',
        'Returns Longer than 40 Yards','Fair Catches','Fumbles']
    
    Offensive_Line = ['Games Started']
    
    Field_Goal_Kickers = ['Kicks Blocked','Longest FG Made','FGs Made',
        'FGs Attempted','FG Percentage','FGs Made 20 to 29 Yards',
        'FGs Attempted 20 to 29 Yards','FG Percentage 20 to 29 Yards',
        'FGs Made 30 to 39 Yards','FGs Attempted 30 to 39 Yards',
        'FG Percentage 30 to 39 Yards','FGs Made 40 to 49 Yards',
        'FGs Attempted 40 to 49 Yards','FG Percentage 40 to 49 Yards',
        'FGs Made 50 Plus Yards','FGs Attempted 50 Plus Yards',
        'FG Percentage 50 Plus Yards','Extra Points Attempted',
        'Extra Points Made','Percentage of Extra Points Made','Extra Points Blocked']
    
    Punting = ['Punts','Gross Punting Yards','Net Punting Yards',
        'Longest Punt','Gross Punting Average','Net Punting Average',	
        'Punts Blocked','Out of Bounds Punts','Downed Punts',	
        'Punts Inside 20 Yard Line','Touchbacks','Fair Catches','Punts Returned',
        'Yards Returned on Punts','TDs Returned on Punt']
    
    Kickoff = ['Kickoffs','Kickoff Yards','Out of Bounds Kickoffs',
        'Yards Per Kickoff','Touchback','Touchback Percentage',
        'Kickoffs Returned','Average Returned Yards','Kickoffs Resulting in TDs',
        'On Sides Kicks','On Sides Kicks Returned']
    
    Table_Headers = {'Passing':Passing,'Rushing':Rushing,'Receiving':Receiving,
             'Defensive':Defensive,'Fumbles':Fumbles,'Kick Return':Kick_Return,
             'Punt Return':Punt_Return,'Offensive Line':Offensive_Line,
             'Field Goal Kickers':Field_Goal_Kickers,'Punting Stats':Punting,
             'Kickoff Stats':Kickoff}          

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
        Stats_Headers = Player_Info_Headers + Stats_For_All + Table_Headers[stats_type]
        player.New_CSV_File(File_Names[stats_type],Stats_Headers)   

    return [File_Names[stats_type],len(Stats_For_All + Table_Headers[stats_type])]