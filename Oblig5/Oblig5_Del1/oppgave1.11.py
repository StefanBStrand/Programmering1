class Game:
    def __init__(self, name, genre, age_rating=18):
        self.name = name
        self.genre = genre
        self.age_rating = age_rating

    def description(self):
        return f"The game {self.name} is of the genre {self.genre} and has an age rating of {self.age_rating}"


game1 = Game("Hades", "Rogue-lite", 12)
game2 = Game("God of War", "Action")
print(game1.age_rating)
print(game2.description())

# first print is 12
# second print is: The game god of war is of the genre Action and has an age rating of 18


