from Player import Player

def fetch_player_list():
    # Open file
    player_name_list_file = open('player_name_list.txt', 'r')
    # Read data from file
    player_name_list_data = player_name_list_file.read()
    # Split into lines
    split_player_name_list_data = player_name_list_data.splitlines()

    # Loop through each line and create player_list
    player_list = []
    for player in split_player_name_list_data:
        player_data_split = player.split(',')
        player_list.append(Player(player_data_split[0].strip(), player_data_split[1].strip(), player_data_split[2].strip()))

    # Close file
    player_name_list_file.close()

    return player_list