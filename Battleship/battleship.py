import string

class Battlefield:
    """return game plan in list['1A', '1B', '1C',]"""

    def __init__(self, N):
        "N is size of the battlefield"
        self.alphabet_list= list(string.ascii_uppercase)
        self.N = N

    def create_battlefield(self):
        "Creates battlefield in size of N"
        battlefield = []
        for row in range(self.N):  # N +- 1
            for column in self.alphabet_list[0:self.N]:
                field = (str(row + 1) + column)
                battlefield.append(field)
        return battlefield

class Boats:
    "spliting and creating boats from string"

    def __init__(self, S):
        self.S = S

    def split_boats(self):
        "spliting string of boats e.g. '12A 12D, 9C 9C' to two lists e.g.[['12A', '12D'], ['9C', '9C']]"
        boats = self.S.split(",")
        boat_one = boats[0].split(" ")
        boat_two = boats[1].split(" ")
        boat_two.remove("")
        result = boat_one, boat_two
        boat_list = list(result)
        return boat_list

    @staticmethod
    def create_boat(boat_one):
        "create boat list, taken from my previous code, messy function which does the magic"
        alphabet_list = list(string.ascii_uppercase)
        if len(boat_one[0]) == 2 and len(boat_one[1]) == 2:
            no1 = str(boat_one[0])
            no_one = int(no1[0])
            no2 = str(boat_one[1])
            no_two = int(no2[0])
            letter_one = str(boat_one[0])
            x = letter_one[1]
            letter_two = str(boat_one[1])
            y = letter_two[1]
        if len(boat_one[0]) == 3 and len(boat_one[1]) == 3:
            no1 = str(boat_one[0][0:2])
            no_one = int(no1)
            no2 = str(boat_one[1][0:2])
            no_two = int(no2)
            letter_one = str(boat_one[0])
            x = letter_one[-1]
            letter_two = str(boat_one[1])
            y = letter_two[-1]

        if len(boat_one[0]) == 2 and len(boat_one[1]) == 3:
            no1 = str(boat_one[0])
            no_one = int(no1[0])
            no2 = str(boat_one[1][0:2])
            no_two = int(no2)
            letter_one = str(boat_one[0])
            x = letter_one[1]
            letter_two = str(boat_one[1])
            y = letter_two[-1]

        if boat_one[0] == boat_one[1]:  # ['1A', '1A']
            first_boat = []
            first_boat.append(boat_one[0])
        elif boat_one[0] != boat_one[1] and boat_one[0][1] == boat_one[1][1] and int(boat_one[0][0]) + 1 == int(
                boat_one[1][0]):
            # two fields, same column ['1A', '2A']
            first_boat = boat_one
        elif boat_one[0] != boat_one[1] and boat_one[0][0] == boat_one[1][0] and alphabet_list.index(
                x) + 1 == alphabet_list.index(y):
            # two fields, same row
            first_boat = boat_one
        elif boat_one[0] != boat_one[1] and boat_one[0][1] == boat_one[1][1] and int(boat_one[0][0]) + 2 == int(
                boat_one[1][0]):
            # three fields, same column
            element = str(no_one + 1) + x
            boat_one.append(element)
            first_boat = boat_one
        elif boat_one[0] != boat_one[1] and boat_one[0][0] == boat_one[1][0] and alphabet_list.index(
                x) + 2 == alphabet_list.index(y):
            # three fields, same row
            temp_number = alphabet_list.index(x) + 1
            element = str(no_one) + str(alphabet_list[temp_number])
            boat_one.append(element)
            first_boat = boat_one
        elif boat_one[0] != boat_one[1] and boat_one[0][1] == boat_one[1][1] and int(boat_one[0][0]) + 3 == int(
                boat_one[1][0]):
            element = str(no_one + 1) + x
            element_one = str(no_one + 2) + x
            boat_one.append(element)
            boat_one.append(element_one)
            first_boat = boat_one
            # four fields, same column
        elif boat_one[0] != boat_one[1] and boat_one[0][0] == boat_one[1][0] and alphabet_list.index(
                x) + 3 == alphabet_list.index(y):
            temp_number = alphabet_list.index(x) + 1
            element = str(no_one) + str(alphabet_list[temp_number])
            element_one = str(no_one) + str(alphabet_list[temp_number + 1])
            boat_one.append(element)
            boat_one.append(element_one)
            first_boat = boat_one
            # four fields, same row
        else:
            element = str(no_one) + y
            element_one = str(no_two) + x
            boat_one.append(element)
            boat_one.append(element_one)
            first_boat = boat_one
        return first_boat

class Shots(Boats):
    "spliting and creating list of shots"
    def __init__(self, S, T):
        super().__init__(S)
        self.T = T

    def create_shots_list(self):
        "transforming string of shots to list of shots '1A 12A' --> ['1A', '12A'...]"
        shotlist = self.T.split(" ")
        return shotlist

    def shooting(self):
        """shooting on boats function taking list of shots and compares it with list of boats
        result is list of remaining fields of boats
        if boat is fully hit --> return empty list"""
        shotlist = self.T.split(" ")
        boatlist = Boats(self.S)
        boat1 = boatlist.split_boats()[0]
        boat2 = boatlist.split_boats()[1]
        boat1 = Boats.create_boat(boat1)
        boat2 = Boats.create_boat(boat2)
        for shot in shotlist:
            if shot in boat1:
                boat1.remove(shot)
            elif shot in boat2:
                boat2.remove(shot)
            else:
                continue
        boats_after_shots = boat1, boat2
        return list(boats_after_shots)

def boats_after_shooting(S,T):
    """function returning tuple with amount of sunk ships and hits"""
    result1 = 0
    result2 = 0
    boatlist = Boats(S)
    boat1 = boatlist.split_boats()[0]
    boat2 = boatlist.split_boats()[1]
    boat1 = Boats.create_boat(boat1)
    boat2 = Boats.create_boat(boat2)
    len_boat_one = len(boat1)
    len_boat_two = len(boat2)
    battle = Shots(S,T)
    boat1 = battle.shooting()[0]
    boat2 = battle.shooting()[1]
    if not boat1 and not boat2:
        result1 += 2
    elif not boat1:
        result1 += 1
        result2 = len_boat_two - len(boat2)
    elif not boat2:
        result1 += 1
        result2 = len_boat_one - len(boat1)
    elif boat1 and boat2:
        result2 = (len_boat_one - len(boat1)) + (len_boat_two - len(boat2))
    else:
        pass
    output = result1, result2
    return(output)

def solution(N, S, T):
    if N < 27:
        result = boats_after_shooting(S,T)
        return(result)
    else:
        return "You have to have smaller battlefield"


print(solution(15,"12A 12D, 9A 9C", "1A 12A 2B 1B 1C 2C 3E 4D 9C")) # result (0, 2)
print(solution(12,"12A 12D, 9C 9C", "1A 12A 2B 1B 1C 2C 3E 4D 9C")) #result (1, 1)
print(solution(125,"12A 12D, 9A 9C", "1A 12A 2B 1B 1C 2C 3E 4D 9C")) # result "You have to have smaller battlefield"
