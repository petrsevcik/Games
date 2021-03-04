
def battle(string1, string2):
    cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    result = 0
    for round in range(len(string1)):
        if cards.index(string1[round]) < cards.index(string2[round]):
            result += 1
    return result

A = "A586QK"
B = "JJ653K"
C = "JJJJJJ"
D = "JJJJJJ"

print(battle(A,B))