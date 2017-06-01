def Try_Glossary(Item,Glossary,Header):
    if Item in Glossary.keys():
        return Header.append(Glossary[Item])
    else:
        print(Item)
        return Header

def NFL_Shorthand_to_Headers(stats_type,Col_Cats,Col_Names):
    Stats_Type = stats_type.upper()
    Repeats = []
    Header = []
    
    for index in range(0,len(Col_Names)):
        # for game logs
        if stats_type == 'GET_CATS':
            Stats_Type = Col_Cats[index].upper()
            
        Item = Col_Names[index]
        Common_Glossary = {'G':'Games Played','GS':'Games Started','Year':'Year',
                        'Team':'Team','Int':'Ints','Sck':'Sacks','FUM':'Fumbles',
                        'TB':'Touchbacks','FC':'Fair Catches','WK':'Week',
                        'Game Date':'Game Date'}
        if Item == 'Result':
            Header += ['Outcome','Score']
            
        elif Item == 'Opp':
            Header += ['Home or Away','Opponent']
            
        elif Item in Common_Glossary:
            Header.append(Common_Glossary[Item])
            
        elif 'PASSING' in Stats_Type:
            Glossary = {'Att':'Passes Attempted','Comp':'Passes Completed',
                'Pct':'Completion Percentage','Att/G':'Pass Attempts Per Game',
                'Yds':'Passing Yards','Avg':'Passing Yards Per Attempt',
                'Yds/G':'Passing Yards Per Game','TD':'TD Passes',
                'TD%':'Percentage of TDs per Attempts','Int%':'Int Rate',
                'Lng':'Longest Pass','20+':'Passes Longer than 20 Yards',
                '40+':'Passes Longer than 40 Yards',
                'SckY':'Sacked Yards Lost','Rate':'Passer Rating',
                '1st':'First Down Passes','1st%':'Percentage First Downs per Attempts'}
            Try_Glossary(Item,Glossary,Header)

        elif 'RUSHING' in Stats_Type:
            Glossary = {'Att':'Rushing Attempts','Att/G':'Rushing Attempts Per Game',
                'Yds':'Rushing Yards','Avg':'Yards Per Carry',
                'Yds/G':'Rushing Yards Per Game','TD':'Rushing TDs',
                'Lng':'Longest Rushing Run','1st':'Rushing First Downs',
                '1st%':'Percentage of Rushing First Downs',
                '20+':'Rushing More Than 20 Yards','40+':'Rushing More Than 40 Yards'}
            Try_Glossary(Item,Glossary,Header)

        elif 'RECEIVING' in Stats_Type:
            Glossary = {'Rec':'Receptions','Yds':'Receiving Yards',
                'Avg':'Yards Per Reception','Yds/G':'Yards Per Game',
                'Lng':'Longest Reception','TD':'Receiving TDs',
                '20+':'Receptions Longer than 20 Yards',
                '40+':'Receptions Longer than 40 Yards','1st':'First Down Receptions',
                '1st%':'Percentage First Down Receptions'}
            Try_Glossary(Item,Glossary,Header)

        elif 'KICK RETURN' in Stats_Type or 'PUNT RETURN' in Stats_Type:
            Glossary = {'Ret':'Returns','Yds':'Yards Returned','RetY':'Yards Returned',
                'Avg':'Yards Per Return','Lng':'Longest Return','TD':'Returns for TDs',
                '20+':'Returns Longer than 20 Yards',
                '40+':'Returns Longer than 40 Yards'}
            Try_Glossary(Item,Glossary,Header)
            
        elif 'DEFENSIVE' in Stats_Type or Stats_Type in ['TACKLES','INTERCEPTIONS']:
            Glossary = {'Comb':'Total Tackles','Total':'Solo Tackles',
                'Ast':'Assisted Tackles','SFTY':'Safties',
                'PDef':'Passes Defended','TDs':'Ints for TDs','Yds':'Int Yards',
                'Avg':'Yards Per Int','Lng':'Longest Int Return'}
            Try_Glossary(Item,Glossary,Header)
            
        elif 'PUNT' in Stats_Type:
            Glossary = {'Punts':'Punts','Yds':'Gross Punting Yards',
                'Net Yds':'Net Punting Yards','Lng':'Longest Punt',
                'Avg':'Gross Punting Average','Net Avg':'Net Punting Average',	
                'Blk':'Punts Blocked','OOB':'Out of Bounds Punts',
                'Dn':'Downed Punts','IN 20':'Punts Inside 20 Yard Line',
                'Ret':'Punts Returned',
                'RetY':'Yards Returned on Punts','TD':'TDs Returned on Punt'}
            Try_Glossary(Item,Glossary,Header)

        elif 'KICKOFF' in Stats_Type.upper():
            Glossary = {'KO':'Kickoffs','Yds':'Kickoff Yards',
                'OOB':'Out of Bounds Kickoffs','Pct':'Touchback Percentage',
                'Ret':'Kickoffs Returned','TD':'Kickoffs Resulting in TDs',
                'OSK':'On Sides Kicks','OSKR':'On Sides Kicks Returned'}
            if Item in Glossary.keys():
                Header.append(Glossary[Item])
            elif Item == 'Avg' and 'Avg' not in Repeats:
                Header.append('Yards Per Kickoff')
                Repeats.append(Item)
            elif Item == 'Avg':
                Header.append('Average Returned Yards')
            else:
                print(Item)
            
        elif 'FUMBLES' in Stats_Type:
            Glossary = {'Lost':'Fumbles Lost','FF':'Forced Fumbles',
                'TD':'Fumble Return TDs','OOB':'Out of Bounds Fumbles',
                'Sfty':'Saftey Fumbles'}
            if Item in Glossary.keys():
                Header.append(Glossary[Item])
            elif Item == 'Rec' and 'Rec' not in Repeats:
                Header.append('Own Fumbles Recovered')
                Repeats.append('Rec')
            elif Item == 'Rec':
                Header.append('Opponent Fumbles Recovered')
            elif Item == 'Yds' and 'Yds' not in Repeats:
                Header.append('Own Fumble Return Yards')
                Repeats.append('Yds')
            elif Item == 'Yds':
                Header.append('Opponent Fumble Return Yards')
            else:
                print(Item)
        
        elif 'FIELD GOAL' in Stats_Type or Stats_Type in ['OVERALL FGS','PAT','KICKOFFS']:
            Item_Type = Col_Cats[index]
            Glossary = {'Blk':'Kicks Blocked','Lng':'Longest FG Made',
                'FGM':'FGs Made','FG Att':'FGs Attempted'}
            PAT_Glossary = {'XP Att':'Extra Points Attempted','XPM':'Extra Points Made',
                'Pct':'Percentage of Extra Points Made','Blk':'Extra Points Blocked'}
            Repeat_Glossary = { 'M':'FGs Made','Att':'FGs Attempted','Pct':'FG Percentage'}
            
            if Item in PAT_Glossary and Item_Type == 'PAT':
                Header.append(PAT_Glossary[Item])
            elif Item in Glossary.keys():
                Header.append(Glossary[Item])
            elif Item in Repeat_Glossary and Item_Type == 'Overall FGs':
                Header.append(Repeat_Glossary[Item])
            elif Item in Repeat_Glossary:
                Header.append(' '.join([Repeat_Glossary[Item],Item_Type]))
            else:
                print(Item)

        else:
            print('%s: %s' % (Stats_Type,Col_Names[index]))
        
    return Header
    
    
    
    
    
    
    