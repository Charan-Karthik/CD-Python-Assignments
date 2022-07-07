class Player:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age = dictionary["age"]
        self.position = dictionary["position"]
        self.team = dictionary["team"]

    def display_player_info(self):
        print("Name:", self.name)
        print("age:", self.age)
        print("position:", self.position)
        print("team:", self.team)
        print()

    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for player in team_list:
            new_team.append(cls(player))

        return new_team

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32, "position": "Point Guard",
    "team": "Brooklyn Nets"
}

player1 = Player(kevin)
player2 = Player(jason)
player3 = Player(kyrie)

player1.display_player_info()
player2.display_player_info()
player3.display_player_info()

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# Challenge 3
player_instances = []

for i in range(len(players)):
    new_player = Player(players[i])
    player_instances.append(new_player)
    print(player_instances)