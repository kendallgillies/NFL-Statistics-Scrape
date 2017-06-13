# NFL-Statistics-Scrape
This code gathers basic statistics, career statistics and game logs provided by the NFL on their website for all players past and present.  The dataset can be found at https://www.kaggle.com/kendallgillies/nflstatistics.

## Summary
This code gathers some of the statistics provided by the NFL on their website for all players past and present.  Given not all players are assigned a position, the code will use the “find player by name” page to first scrape all of the player’s names, unique url identifier and years played (if retired).  The code then scrapes three main groups of statistics (basic statistics, career statistics and game logs) independently of each other and stores the data in various CSV files.  

## Files and Explanation
### Files and Folders
1. Base_File_NFL_Stats.py
2. Player_Class.py
3. Website_to_CSV_Functions (Folder)
    1. Basic_Stats_Class.py
    2. Career_Stats_Class.py
    3. Functions_Needed_For_All_Stats.py
    4. Game_Logs_Class.py
    5. NFL_Glossary.py
    6. Obtain_Players_from_Website.py

### Files Explanation
1. The base file, the player class file and Functions_Needed_For_All_Stats file are all needed to run any of the other parts of the code.  
2. The file Obtain_Players_from_Website is used to gather the player names and URL identifiers from the NFL website.  For retired players the easiest place to gather the years they played is on the webpage used to gather their names and identifiers, so it is also taken and stored at this point in time.  For active players the years played are not as easily accessible, but can be gathered at a later time from the basic statistics, career stats or game logs.
3. The first main group of statistics is the basic statistics provided for each player and can be obtained through the basic statistics class.  The variables are stored in a CSV file titled Basic_Stats.csv along with the player’s name and URL identifier.  The variables pulled for each player are as follows:
    1.	Number
    2.	Position
    3.	Current Team
    4.	Height
    5.	Weight
    6.	Age
    7.	Birthday
    8.	Birth Place
    9.	College Attended
    10.	High School Attended
    11.	High School Location
    12.	Experience
4. NFL_Glossary.py is used to translate the NFL shorthand found in the table headers.  It is needed for both Career_Stats_Class.py and Game_Logs_Class.py.
5. The second main group of statistics gathered for each player are their career statistics and can be obtain through the career statistics class.  While each player has a main position they play, they will have statistics in other areas; therefore, the career statistics are divided into statistics types.  The statistics are then stored in CSV files based on statistic type along with the player name, URL identifier and position (if available).  The following are the career statistics types and accompanying CSV file names:
    1.	Defensive Statistics – Career_Stats_Defensive.csv
    2.	Field Goal Kickers - Career_Stats_Field_Goal_Kickers.csv
    3.	Fumbles - Career_Stats_Fumbles.csv
    4.	Kick Return - Career_Stats_Kick_Return.csv
    5.	Kickoff - Career_Stats_Kickoff.csv
    6.	Offensive Line - Career_Stats_Offensive_Line.csv
    7.	Passing - Career_Stats_Passing.csv
    8.	Punt Return - Career_Stats_Punt_Return.csv
    9.	Punting - Career_Stats_Punting.csv
    10.	Receiving - Career_Stats_Receiving.csv
    11.	Rushing - Career_Stats_Rushing.csv
6. The final group of statistics is the game logs for each player and can be obtained through the game logs class.  The game logs are stored by position and have the player name, URL identifier and position (if available).  The following are the game log types and accompanying CSV file names:
    1.	Quarterback – Game_Logs_Quarterback.csv
    2.	Running back – Game_Logs_Runningback.csv
    3.	Wide Receiver and Tight End – Game_Logs_Wide_Receiver_and_Tight_End.csv
    4.	Offensive Line – Game_Logs_Offensive_Line.csv
    5.	Defensive Lineman – Game_Logs_Defensive_Lineman.csv
    6.	Kickers – Game_Logs_Kickers.csv
    7.	Punters – Game_Logs_Punters.csv
