import random
from time import sleep
user_digits = []
balance = 100
bet = 100
text_choose = {}
text_eng = {
    1:'Write your 12 digits with spaces:',
    2:'You need to enter 12 digits. Try again Y/N?',
    3:'Come next time',
    4:'Checking the win numbers....',
    5:'Win numbers are:',
    6:'Checking for winners.....',
    7:'You guessed %d numbers',
    8:'Superprize! Your balance: %d',
    9:'You win! Your balance: %d',
    10:'You loose( Your balance: %d',
    11:'Do you want to play more? Y/N',
    12:'New game starting...',
    13:'Sorry, You have not enough credits. Do You want to restart game? Y/N',
    14:'This is the game All or Nothing!',
    15:'Do You want to learn the rules? Y/N',
    16:'You need to write 12 digits with ta space between them.\n' 
            'After that the program will choose 12 digits too.\n' 
            'If 12 or 0 coincidences found, You will get a superprize. Also you win if there 1,2,3,4,8,9,10,11 coincidences.'
            'Otherwise You loose.\n' 
            'At the start of the game You have got 100 credits on your balance. Every game cost 100 credits.\n'
            '',
    17:'Your balance now: %d'
}
text_rus = {
    1:'Напишите 12 чисел через пробел:',
    2:'Нужно внести 12 чисел. Попробовать еще раз Д/Н?',
    3:'Приходите еще',
    4:'Проверка выигрышных чисел....',
    5:'Выпали числа:',
    6:'Проверка совпадений.....',
    7:'Вы угадали %d чисел',
    8:'Суперприз! Ваш баланс: %d',
    9:'Вы выиграли! Ваш баланс: %d',
    10:'Вы проиграли( Ваш баланс: %d',
    11:'Сыграем еще раз? Д/Н',
    12:'Начало новой игры...',
    13:'На Вашем балансе недостаточно кредитов. Перезапустить игру? Д/Н',
    14:'Это игра Все или ничего!',
    15:'Хотите узнать правила? Д/Н',
    16:'Вам нужно указать 12 чисел с пробелами между ними.\n' 
            'Программа случайно выберет 12 чисел из 22.\n' 
            'Если получено 12 или 0 совпадений с Вашим выбором, Вы выишрали суперприз. Выйгрышными считаются также 1,2,3,4,8,9,10,11 совпадений.'
            'В ином случае Вы проиграли.\n' 
            'На старте игры у Вас 100 кредитов на балансе. Каждая игра стоит 100 кредитов.\n'
            '',
    17:'Ваш баланс сейчас: %d'
}

def user_guess():
    global balance
    global bet
    guess = [int(x) for x in input(text_choose.get(1)).split()]
    if len(guess) == 12:
        for x in guess:
            user_digits.append(x)
    else:
        print(text_choose.get(2))
        try_again = input()
        if try_again == 'Y' or try_again == 'Д':
            user_guess()
        else:
            print(text_choose.get(3))
            exit()
    balance = balance - bet
    return user_digits

def check_if_win():
    global balance
    global bet
    win_numbers = random.sample(range(1, 24), 12)
    usr_guess = user_guess()
    print (text_choose.get(4))
    sleep(2)
    print (text_choose.get(5), win_numbers)
    print (text_choose.get(6))
    sleep(1)
    coincidence = 0
    for x in range(0,len(user_digits)):
        if user_digits[x] in win_numbers:
            coincidence += 1
    print (text_choose.get(7) % coincidence)
    sleep(1)
    if coincidence == 12 or coincidence == 0:
        balance = balance + bet * 50000
        print (text_choose.get(8) % balance)
    elif coincidence == 11 or coincidence == 1:
        balance = balance + bet * 500
        print (text_choose.get(9) % balance)
    elif coincidence == 10 or coincidence == 2:
        balance = balance + bet * 25
        print (text_choose.get(9) % balance)
    elif coincidence == 9 or coincidence == 3:
        balance = balance + bet * 5
        print (text_choose.get(9) % balance)
    elif coincidence == 8 or coincidence == 4:
        balance = balance + bet * 1
        print (text_choose.get(9) % balance)
    else:
        print (text_choose.get(10) % balance)
    new_game()

def new_game():
    global balance
    global bet
    if balance >= bet:
        print(text_choose.get(11))
        game2 = input()
        if game2 == 'Y' or game2 == 'Д':
            user_digits.clear()
            print(text_choose.get(12))
            sleep(1)
            check_if_win()
        else:
            print(text_choose.get(3))
            exit()
    else:
        print(text_choose.get(13))
        restart = input()
        if restart == 'Y' or restart == 'Д':
            balance = 100
            user_digits.clear()
            print(text_choose.get(17) % balance)
            print(text_choose.get(12))
            sleep(1)
            check_if_win()
        else:
            print(text_choose.get(3))
            exit()

def rules():
    print(text_choose.get(14))
    print(text_choose.get(15))
    rules = input()
    if rules == 'Y' or rules == 'Д':
        print(text_choose.get(16))
        sleep(1)
        check_if_win()
    else:
        check_if_win()

def lang():
    print('Choose language RUS/ENG:')
    lang = input()
    if lang.lower() == 'rus':
        text_choose.update(text_rus)
    elif lang.lower() == 'eng':
        text_choose.update(text_eng)
    else:
        text_choose.update(text_rus)
    rules()


lang()