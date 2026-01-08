import random


class Team:
    def __init__(self, name, nation, position):
        self.name = name
        self.nation = nation
        self.position = position

# print("Enter 16 teams (name, nation, position - 1 or 2): ")

# for i in range(16):
#     print(f"Team {i + 1}: ")
#     name = str(input("Name: "))
#     nation = str(input("Nation: "))
#     position = int(input("Position (1 or 2): "))
#     teams.append(Team(name, nation, position))


teams = [
    Team("PSG", "France", 2),
    Team("Liverpool", "England", 1),
    Team("Inter", "Italy", 1),
    Team("Manchester City", "England", 1),
    Team("Leipzig", "Germany", 2),
    Team("Eintracht Frankfurt", "Germany", 2),
    Team("Napoli", "Italy", 1),
    Team("Porto", "Portugal", 2),
    Team("Club Brugge", "Belgium", 2),
    Team("Benfica", "Portugal", 1),
    Team("Tottenham", "England", 2),
    Team("Milan", "Italy", 1),
    Team("Bayern", "Germany", 1),
    Team("Real Madrid", "Spain", 2),
    Team("Chelsea", "England", 2),
    Team("Dortmund", "Germany", 1)
]

frist_place = [t for t in teams if t.position == 1]
second_place = [t for t in teams if t.position == 2]

matches = []

while len(matches) < 8:
    team1 = random.choice(frist_place)
    team2 = random.choice(second_place)

    if team1.nation != team2.nation and not (team1.nation == "Ukraine" and team2.nation == "Russia") and not (team1.nation == "Russia" and team2.nation == "Ukraine"):
        matches.append((team1, team2))
        frist_place.remove(team1)
        second_place.remove(team2)

for i in matches:
    print(f"{i[0].name} vs {i[1].name}")
