import bs4, requests, time

# NFL does not have stats for all players
def Check_for_Stats_Webpage(player,stats_type):
    profile_url = 'http://www.nfl.com/player/'+player.player_id+'/profile'
    res = requests.get(profile_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')    
    
    Has_Stats_Page = False
    for div in soup.find_all('div',{'id':'player-profile-tabs'}):
        if stats_type in div.text:
            Has_Stats_Page = True
    return Has_Stats_Page

# If the internet goes out, program will wait 20 seconds then try again.
def Get_HTML_Document(url,parameters):
    start_time = time.time()
    while True:
        try: 
            res = requests.get(url,params = parameters)
            soup = bs4.BeautifulSoup(res.text,'lxml')
            return soup
        except:
            print('Internet has been out for %.2f minutes' % ((time.time()-start_time)/60))
            time.sleep(20)
        