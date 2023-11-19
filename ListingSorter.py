import PlayerList
from Player import Player
from Listing import Listing

#TODO
# Improve matching logic to check if the whole name is being matched. e.g. Rodri matched to James Rodriguez.
## Break entire title iinto terms. Match entire word.

def determine_if_listing_contains_player_name(Listing, player_list):
    match_method = ''
    matched_Player = None

    for player in player_list:
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

    return summarised_listing_list