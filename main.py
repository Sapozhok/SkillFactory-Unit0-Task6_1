print("ДОБРО ПОЖАЛОВАТЬ В ИГРУ КРЕСТИКИ-НОЛИКИ!")
print("Игроки с помощью двух координат ставят свои знаки на свободные клетки поля.")
print("Координаты вводятся через пробел. Крестики начинают первыми.")

field = [[" ", " ", " "] for i in range(3)]


def field_print():
    print(f"   0   1   2")
    print(" -------------")

    for i in range(3):
        print(f"{i}| {field[i][0]} | {field[i][1]} | {field[i][2]} |")
        print(" -------------")


def choice():
    while True:
        print("Введите две координаты от 0 до 2 через пробел")
        x, y = map(int, input("     Ваш ход: ").split())

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == ' ':
                return x, y
            else:
                print("Клетка занята!")
        else:
            print("Некорректные координаты!")


def winner():
    for i in range(3):
        check_win = []
        for j in range(3):
            check_win.append(field[i][j])

        if check_win == ["X", "X", "X"]:
            print("Выиграли Крестики!")
            return True
        if check_win == ["O", "O", "O"]:
            print("Выиграли Нолики!")
            return True

    for i in range(3):
        check_win = []
        for j in range(3):
            check_win.append(field[j][i])

        if check_win == ["X", "X", "X"]:
            print("Выиграли Крестики!")
            return True
        if check_win == ["O", "O", "O"]:
            print("Выиграли Нолики!")
            return True

    check_win = []
    for i in range(3):
        check_win.append(field[i][i])

        if check_win == ["X", "X", "X"]:
            print("Выиграли Крестики!")
            return True
        if check_win == ["O", "O", "O"]:
            print("Выиграли Нолики!")
            return True

    check_win = []
    for i in range(3):
        check_win.append(field[i][2 - i])

        if check_win == ["X", "X", "X"]:
            print("Выиграли Крестики!")
            return True
        if check_win == ["O", "O", "O"]:
            print("Выиграли Нолики!")
            return True

    return False


count = 0
while True:
    field_print()
    count += 1
    if count % 2 == 1:
        print("Ходит Крестик")
    else:
        print("Ходит Нолик")

    x, y = choice()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if winner():
        field_print()
        print("Конец игры!")
        break

    if count == 9:
        field_print()
        print("Ничья!")
        print("Конец игры!")
        break
