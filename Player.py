class Player:
    def __init__(self, Name: str) -> None:
        self.name = Name
    
    
    def say(self):
        print("my Name is " + self.name)