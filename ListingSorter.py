#TODO
# Create player name list.
# Loop through listings to check for player names - last name, full name, nickname.
import PlayerList
from Player import Player
from Listing import Listing

def filter_listings_by_player_name_list(Listing_list):
    #Fetch player_list
    player_list = PlayerList.fetch_player_list()

    final_listing_list = []

    for listing in Listing_list:
        print("Hi")

def determine_if_listing_contains_player_name(Listing, player_list):
    match_method = ''
    matched_Player = None

    for player in player_list:
        print(Listing.title)
        print(player.last_name, player.first_name, player.nick_name)
        if str(player.last_name).strip() in str(Listing.title):
            print('Matched player last name!')
            print(player.first_name)
            if str(player.first_name) in str(Listing.title) and len(player.first_name) > 0:
                print('Matched player full name!')
                match_method = 'full'
                matched_Player = player
                break
            else:
                match_method = 'lastname'
                matched_Player = player
                break
        elif str(player.nick_name) in str(Listing.title) and len(player.nick_name) > 0:
            print('Matched player nick name!')
            match_method = 'nickname'
            matched_Player = player
            break

    print(match_method)
    return match_method, matched_Player

def summarise_Listing_list(filtered_Listing_list):
    summarised_listing_list = {}

    for listing in filtered_Listing_list:
        if listing.matched_Player in summarised_listing_list:
            current_value = summarised_listing_list.get(listing.matched_Player)
            new_dictionary_value = {listing.matched_Player : current_value + 1}
            summarised_listing_list.update(new_dictionary_value)
        else:
            new_dictionary_value = {listing.matched_Player: 1}
            summarised_listing_list.update(new_dictionary_value)

    for matched_Player, count in summarised_listing_list.items():
        print(matched_Player.__dict__)
        print(str(count))