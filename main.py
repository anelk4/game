class GameSite:
    def __init__(self, name, url, games):
        self.name = name
        self.url = url
        self.games = games

    def add_game(self, game):
        self.games.append(game)

    def remove_game(self, game):
        if game in self.games:
            self.games.remove(game)

    def get_game_names(self):
        return [game.name for game in self.games]

    def __str__(self):
        return f"{self.name} ({self.url}) has {len(self.games)} games."

class Game:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

    def rate(self, new_rating):
        self.rating = new_rating

    def __str__(self):
        return f"{self.name} ({self.genre}) has a rating of {self.rating}."

# Create a new instance of the GameSite class
my_game_site = GameSite("My Game Site", "http://www.mygamesite.com", [])

# Create some new Game objects
game1 = Game("Pac-Man", "Arcade", 4.5)
game2 = Game("Tetris", "Puzzle", 4.2)
game3 = Game("Super Mario Bros.", "Platformer", 4.8)

# Add the games to the game site
my_game_site.add_game(game1)
my_game_site.add_game(game2)
my_game_site.add_game(game3)

# Print out some information about the game site and its games
print(my_game_site)
print("На этом сайте представлены следующие игры:", my_game_site.get_game_names())

# Rate a game and print out its new rating
game1.rate(4.7)
print(game1)
