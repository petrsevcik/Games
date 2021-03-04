
import string

def create_battlefield(N):
    alphabet_list= list(string.ascii_uppercase)
    numbers = list(range(1,27))
    battlefield = []
    for number in range(N):#N +- 1
        for letter in alphabet_list[0:N]:
            field = (str(number+1) + letter)
            battlefield.append(field)
    return(battlefield)

def split_boats(S):
    boats = S.split(",")
    boat_one = boats[0].split(" ")
    boat_two = boats[1].split(" ")
    boat_two.remove("")
    result = boat_one, boat_two
    boat_list = list(result)
    return boat_list

def boat_list(boat_one):#['10A', '20B']
    alphabet_list = list(string.ascii_uppercase)
    if len(boat_one[0]) == 2  and len(boat_one[1]) == 2:
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

    if boat_one[0] == boat_one[1]:# ['1A', '1A']
        first_boat = []
        first_boat.append(boat_one[0])
    elif boat_one[0] != boat_one[1] and boat_one[0][1] == boat_one[1][1] and int(boat_one[0][0]) + 1 == int(boat_one[1][0]):
        #two fields, same column ['1A', '2A']
        first_boat = boat_one
    elif boat_one[0] != boat_one[1] and boat_one[0][0] == boat_one[1][0] and alphabet_list.index(x) + 1 == alphabet_list.index(y):
        #two fields, same row
        first_boat = boat_one
    elif boat_one[0] != boat_one[1] and boat_one[0][1] == boat_one[1][1] and int(boat_one[0][0]) + 2 == int(boat_one[1][0]):
        #three fields, same column
        element = str(no_one + 1) + x
        boat_one.append(element)
        first_boat = boat_one
    elif boat_one[0] != boat_one[1] and boat_one[0][0] == boat_one[1][0] and alphabet_list.index(x) + 2 == alphabet_list.index(y):
        #three fields, same row
        temp_number = alphabet_list.index(x) + 1
        element = str(no_one) + str(alphabet_list[temp_number])
        boat_one.append(element)
        first_boat = boat_one
    elif boat_one[0] != boat_one[1] and boat_one[0][1] == boat_one[1][1] and int(boat_one[0][0]) + 3 == int(boat_one[1][0]):
        element = str(no_one + 1) + x
        element_one = str(no_one + 2) + x
        boat_one.append(element)
        boat_one.append(element_one)
        first_boat = boat_one
        #four fields, same column
    elif boat_one[0] != boat_one[1] and boat_one[0][0] == boat_one[1][0] and alphabet_list.index(x) + 3 == alphabet_list.index(y):
        temp_number = alphabet_list.index(x) + 1
        element = str(no_one) + str(alphabet_list[temp_number])
        element_one = str(no_one) + str(alphabet_list[temp_number+1])
        boat_one.append(element)
        boat_one.append(element_one)
        first_boat = boat_one
        #four fields, same row
    else:
        element = str(no_one) + y
        element_one = str(no_two) + x
        boat_one.append(element)
        boat_one.append(element_one)
        first_boat = boat_one
    return first_boat

def shots_list(T):
    x = T.split(" ")
    return x

def solution(N, S, T):
    first_step = create_battlefield(N)
    second_step = split_boats(S)
    first_boat_list = boat_list(second_step[0])
    second_boat_list = boat_list(second_step[1])
    list_of_shots = shots_list(T)
    len_boat_one = len(first_boat_list)
    len_boat_two = len(second_boat_list)
    for shot in list_of_shots:
        if shot in first_boat_list:
            first_boat_list.remove(shot)
        elif shot in second_boat_list:
            second_boat_list.remove(shot)
        else:
            continue
    result1 = 0
    result2 = 0
    if not first_boat_list and not second_boat_list:
        result1 += 2
    elif not first_boat_list:
        result1 += 1
        result2 = len_boat_two - len(second_boat_list)
    elif not second_boat_list:
        result1 += 1
        result2 = len_boat_one - len(first_boat_list)
    elif first_boat_list and second_boat_list:
        result2 = (len_boat_one - len(first_boat_list)) + (len_boat_two - len(second_boat_list))
    else:
        pass
    output = result1, result2
    return output


print(solution(12,"12A 12D, 9C 9C", "1A 12A 2B 1B 1C 2C 3E 4D 9C"))
