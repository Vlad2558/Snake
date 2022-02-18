import random

tables = ['.', '.', '.', '.', '.', '.', '.', '.', '.']


def show(table):
    for num in range(9):
        print(table[num], end=' ')
        if num % 3 == 2:
            print()


def check(table):
    if table[0] == table[1] == table[2] or table[0] == table[4] == table[8] or table[0] == \
            table[3] == table[6]:
        if table[0] == "X":
            print('X WIN')
            return True
        elif table[0] == "O":
            print("O WIN")
            return True
    elif table[3] == table[4] == table[5] or table[1] == table[4] == table[7]:
        if table[4] == "X":
            print('X WIN')
            return True
        elif table[4] == "O":
            print("O WIN")
            return True
    elif table[6] == table[7] == table[8] or table[6] == table[4] == table[2]:
        if table[6] == "X":
            print('X WIN')
            return True
        elif table[6] == "O":
            print("O WIN")
            return True
    elif table[2] == table[5] == table[8]:
        if table[2] == "X":
            print('X WIN')
            return True
        elif table[2] == "O":
            print("O WIN")
            return True
        return False


used_list = []
game_end = False
show(tables)
for i in range(9):
    if i % 2 == 0:
        j = int(input("Enter X position(1-9)"))
        while j in used_list or j not in range(1, 10):
            j = int(input("Enter X position(1-9)"))
        tables[j - 1] = "X"
        used_list.append(j)
    else:
        j = random.randrange(1, 10)  # For playing with PC
        # j = int(input("Enter O position(1-9)")) #For 2 players playing
        while j in used_list or j not in range(1, 10):
            j = random.randrange(1, 10)  # For playing with PC
            # j = int(input("Enter O position(1-9)")) #For 2 players playing
        tables[j - 1] = "O"
        used_list.append(j)
        print(" ")
    show(tables)
    if check(tables):
        game_end = True
        break
if not game_end:
    print("No one win")
print("end game")
