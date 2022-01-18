class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)
    def __getitem__(self, i):
        return self.players[i]

some_club = Club('Arsenal')
my_club = Club('Local')

my_club.players.append('rolf')
my_club.players.append('Anne')

print(len(my_club))
print(my_club[1])