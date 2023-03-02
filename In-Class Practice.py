
def problem1():
    import random
    print('Dice Thrower')
    print('='*12)
    sought = random.randint(2,12)
    print(f'Total sought: {sought}')
    count = 0
    while True:
        dice = [random.randint(1,6) for i in range(2) ]
        count += 1
        print(f'Result of throw {count} : {dice[0]} + {dice[1]}')
        if sum(dice) == sought:
            print(f'You got your total in {count} throws!')
            print()
            break
problem1()
def problem2():
    import random

    sought = random.randint(2,20)
    print(f'Total sought: {sought}')
    count = 1
    while True:
        dice = [random.randint(1,6) for i in range(2) ]
        dice2 = [random.randint(1,6) for i in range(2) ]
        print(f'Result of picks {count} and {count + 1}: {sum(dice)} + {sum(dice2)}')
        count += 2
        if sum(dice) + sum(dice2) == sought:
            print(f'You got your total in {count-1} throws!')
            print()
            break


problem2()
def precessing_data():
    def ktra(date,month,year):
        day_nam_nhuan = [0,31,29,31,30,31,30,31,31,30,31,30,31]
        day_nam_ko_nhuan = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if month not in range(1, 13):
            return False
        if year % 4 == 0:
            if date not in  range(1,day_nam_nhuan[month]+1):
                return False
        elif year % 4 != 0:
            if date not in  range(1,day_nam_ko_nhuan[month]+1):
                return False
        return True

    date = int(input('Date: '))
    month = int(input('mothn: '))
    year = int(input('year: '))
    if ktra(date,month,year):
        print('Valid')
    else:
        print('Invalid')
def charater_data():
    start_char = input("Enter the starting character: ")
    end_char = input("Enter the ending character: ")

    start_code = ord(start_char)
    end_code = ord(end_char)

    if start_code < end_code:
        for code in range(end_code - 1, start_code, -1):
            print(chr(code) + ": " + str(code) + ", " + hex(code))
    else:
        for code in range(end_code + 1, start_code, 1):
            print(chr(code) + ": " + str(code) + ", " + hex(code))

def menu():
    while True:
        print('''1- Processing date data
2- Character data
3- Quit''')
        choice = input()
        if choice == '1':
            precessing_data()
        elif choice == '2':
            charater_data()
        elif choice =='3':
            break
menu()
import math

def ptbac2():
    a = float(input("Enter the coefficient of x^2: "))
    b = float(input("Enter the coefficient of x: "))
    c = float(input("Enter the constant term: "))

    delta = b**2 - 4*a*c


    if delta > 0:
        # Calculate the two real roots and print them
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        print("The roots are real and different:")
        print("x1 = ", root1)
        print("x2 = ", root2)

    elif delta == 0:
        root = -b / (2*a)
        print("The root is real and repeated:")
        print("x = ", root)
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-delta) / (2*a)
        print("The roots are complex conjugates:")
        print("x1 = ", real_part, "+", imag_part, "i")
        print("x2 = ", real_part, "-", imag_part, "i")



def amount():
    while True:
        deposti = float(input('Your depost: '))
        if deposti <=0:
            print('deposit must be >0')
            continue
        rate = float(input('Yearly rate: '))
        if rate <0 or rate > 1:
            print('Rate must be from 0.1 to 1.0')
            continue
        years = float(input('Number of years: '))
        if years <=0:
            print('Invalid year')
            continue
        amount = deposti * (1 +rate) **years
        print(f'Amount = {amount}')
        break

def menu2():
    while True:
        print('''1- Quadratic equation ( phương trình bậc 2)
2- Bank deposit problem
3- Quit''')
        choice = input()
        if choice ==  '1':
            ptbac2()
        elif choice == '2':
            amount()
        elif choice == '3':
            quit()
menu2()