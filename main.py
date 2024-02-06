from generateprimer import GeneratePrimer

sostav_chisla = 30
action = '-'
count = 0
genprimer = GeneratePrimer(sostav_chisla)

list_random_index = genprimer.get_random_index()
list_random_primer = genprimer.enter_action(action)
for index in list_random_index:
    print(list_random_primer[index])
    # Выполнение логики игры!
    number1,number2 = list_random_primer[index].split(action)
    vvod_otveta = int(input('VVod '))
    if action == '+':
        if vvod_otveta == (int(number1)+int(number2)):
            count += 1
            print('You win!!')
            print(f'you have {count}')
        else:
            print('You Lose!')
    elif action == '-':
        if vvod_otveta == (int(number1)-int(number2)):
            count += 1
            print('You win!!')
            print(f'you have {count}')
        else:
            print('You Lose!')