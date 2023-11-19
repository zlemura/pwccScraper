from Player import  Player

class Listing:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.match_method = ''
        self.matched_Player = None

    def update_match_method(self, match_method):
        self.match_method = match_method

    def update_matched_Player(self, matched_Player):
        self.matched_Player = matched_Player