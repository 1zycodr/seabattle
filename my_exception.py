class Wrong_move(Exception):
    def __init__ (self, text):
        self.text = text

class Hit_move(Exception):
    def __init__(self, text):
        self.text = text

class Destroy_move(Exception):
    def __init__(self, text):
        self.text = text