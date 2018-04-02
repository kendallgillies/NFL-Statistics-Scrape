from Player_Class import *
from Website_to_CSV_Functions.Functions_Needed_For_All_Stats import *

import string
import os


def obtain_number_of_pages(soup):
    pages = [1]
    for page in soup.find_all(title=re.compile('Go to page')):
        try:
            pages.append(int(page.contents[0]))
        except Exception as e:
            pass
    return max(pages)


def get_player_name_and_id(player, td):
    for a in td.find_all('a'):
        player.name = a.text
        
        attributes = a.attrs
        pid = attributes['href']
        pid = pid.split('/')
        player.player_id = '/'.join([pid[2], pid[3]])


def get_players_current_status(player, td, is_current):
    status_abbrev = {'ACT': 'Active',
                     'RES': 'Injured reserve',
                     'NON': 'Non football related injured reserve',
                     'SUS': 'Suspended',
                     'PUP': 'Physically unable to perform',
                     'UDF': 'Unsigned draft pick',
                     'UFA': 'Unsigned free agent',
                     'EXE': 'Exempt'}

    if is_current:
        player.current_status = status_abbrev[td.text]
    else:
        player.current_status = 'Retired'


def get_years_played(player, td, is_current):
    if not is_current:
        player.years_played = td.text


def get_player_information(players, td_tags, col_num, name_index, status_index,
                           years_played_index, is_current, filename):
    count = 0
    player = Player()
    for td in td_tags:
        index = count % col_num
        if index == name_index:
            get_player_name_and_id(player, td)
        elif index == status_index:
            get_players_current_status(player, td, is_current)
        elif index == years_played_index:
            get_years_played(player, td, is_current)
        elif index == col_num-1:
            players[player.player_id] = player
            if not os.path.exists(filename):        
                headers = ['Player Id', 'Name', 'Current Status', 'Years Played']
                player.New_CSV_File(filename, headers)
            stats = [player.player_id, player.name, player.current_status, player.years_played]
            player.Write_Stats_to_CSV(filename, stats)
            player = Player()
        count += 1


def obtain_players_and_status(initial_url, url_parameters, players, soup, filename):
    page_number = 1
    max_page_estimate = obtain_number_of_pages(soup)

    while page_number <= max_page_estimate:
        # NFL website parameter name for page number
        url_parameters['d-447263-p'] = page_number
        soup = Get_HTML_Document(initial_url, url_parameters)

        # Update estimate of maximum number of pages, based on what number we can currently see
        max_page_estimate = obtain_number_of_pages(soup)

        for table in soup.find_all('table', id='result'):
            td_tags = table.find_all('td')
            if url_parameters['playerType'] == 'current':
                get_player_information(players, td_tags, 13, 2, 3, 4, True, filename)
            else:
                get_player_information(players, td_tags, 12, 0, 1, 2, False, filename)

        page_number += 1


# Storing happens when get_player_information is called
def get_and_store_all_players_names_and_ids(filename):
    players = {}
    player_types = ['current', 'historical']
    for player_type in player_types:
        for last_name_beginning in list(string.ascii_uppercase):
            print('Getting %s players whose last name starts with %s' % (player_type, last_name_beginning))
            
            url_parameters = {'category': 'lastName',
                              'filter': last_name_beginning,
                              'playerType': player_type}

            initial_url = 'http://www.nfl.com/players/search'
            soup = Get_HTML_Document(initial_url, url_parameters)

            obtain_players_and_status(initial_url, url_parameters, players, soup, filename)

    return players
