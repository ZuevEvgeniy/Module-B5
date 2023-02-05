def Hello():
    print("      Добро пожаловать  ")
    print("           в игру      ")
    print("      крестики-нолики!  ")
    print("             =)          ")
    print("        Формат ввода:  ")
    print(" первое число - номер строки  ")
    print(" второе число - номер столбца ")
    print("      Let's battle begins!         ")
z= "|"
def see():
    print (f"=)| 0 | 1 | 2 |")
    print ("---------------")
    for i in range (3):
        row_see =" | ".join(field[i])+ " |"
        print (f"{i} {z} {row_see}")
        print("---------------")
def turn():
    while True:
        cords = input("Введите координаты: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y
def win():
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cords in win_cords:
        a = cords[0]
        b = cords[1]
        c = cords[2]
        if field[a[0]][a[1]]==field[b[0]][b[1]]==field[c[0]][c[1]] and field[a[0]][a[1]]!=" ":
            see()
            print (f'{field[a[0]][a[1]]} - победитель!')
            return True
    return False
field = [[" "] * 3 for i in range(3)]
turns=0
Hello()
while True:
    turns += 1
    see()
    if turns % 2 == 1:
        print("Ходит X!")
    else:
        print("Ходит 0!")

    x, y = turn()

    if turns % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if turns == 9:
        print("Ничья!")
        break