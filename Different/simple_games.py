# simple game
# demonstrates import modul
import games, random

again = None
while again != 'n':
    players = []
    num = games.ask_number(question = "Сколько игроков учавствует?(2-5)", low = 2, high = 5)
    for i in range(num):
        name = input('name is player: ')
        score = random.randrange(2) + 1
        player = games.Player(name, score)
        players.append(player)
    print("\nResults are games: ")
    for player in players:
        print(player)
    again = games.ask_yes_no("\n do want to play one more time?(y/n): ")
input('\n Press enter for exit.')