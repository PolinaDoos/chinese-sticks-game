def took_st(player, sticks):
    while True:
        print("\nпалочек доступно:", sticks)
        try:
            p = int(input(player + ", возьмите палочки: "))
        except ValueError:
            print("\nвведите число")
            continue
        if sticks - p < 0:
            print("\nвыберите из доступного количества")
        elif p > 3 or p < 1:
            print("\nвыберете от 1 до 3 палочек")
        else:
            False
            return p


def ch_sticks(sticks):
    print(
        "Играют два игрока.\nЕсть 10 палочек. "
        "Игроки по очереди берут от одной до трёх палочек.\n"
        "Играют до тех пор, пока не закончатся палочки.\nТот, кто взял последним, проиграл.\n\n")
    p1 = str(input("имя первого игрока: "))
    p2 = str(input("\nимя второго игрока: "))
    chain = True
    while sticks > 0:
        if chain:
            p = p1
        else:
            p = p2
        sticks -= took_st(p, sticks)
        if sticks == 0:
            print("\nпалочек больше нет")
            print('\n******* Игрок ' + p + ' ПРОИГРАЛ *******')
            break
        else:
            chain = not chain

    input("\n\nЭто все. Можете закрыть окно")


ch_sticks(10)