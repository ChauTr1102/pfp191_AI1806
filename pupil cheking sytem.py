
school= {'12': {'Trinh Minh Chau': [{'English': 9}, {'Maths': 9}, {'Physics': 9}, {'Chemistry': 9}, {'CS': 9}]}, '11': {'Trinh Hoang Anh ': [{'English': 8}, {'Maths': 8}, {'Physics': 8}, {'Chemistry': 8}, {'CS': 8}]}, '10': {'Khong Duy Tung ': [{'English': 7}, {'Maths': 8}, {'Physics': 7}, {'Chemistry': 8}, {'CS': 7}]}}

def func1_store_data():
    while True:
        global school
        roll = dict()
        student = dict()
        mark = []
        lop = input('Enter roll number: ')
        name = input('Enter your name ')
        catagories = ['English', 'Maths','Physics','Chemistry','CS']
        for i in catagories:
            print('enter marks in',i,end=' ')
            subject = int(input(''))
            mark.append({i:subject})
        student[name] = mark
        roll[lop] = student
        school.update(roll)

        end_loop = input('if you want to add quit type \'done\' ')
        if end_loop == 'done':
            break

def create_pupil_record():
    while True:
        choice = input('do you want add more type \'yes\' if you don\'t wish to just press any key : ')
        if choice == 'yes':
            func1_store_data()
        else:
            break

def funtion_print():
    print()
    print()
    print('PUPIL DTEAIL...')
    for roll in school:
        print('Roll Number',roll)
        for name in school[roll]:
            print('Name',name)
            for i in school[roll][name]:
                for k,v in i.items():
                    print(k,v)
            print()

def search_pupil():
    roll = (input('Roll Number '))
    name = input('Name ')
    for name in school[roll]:
        print('Name', name)
        for i in school[roll][name]:
            for k, v in i.items():
                print(k, v)
        print()

def modify():
    roll  = input('Enter roll number: ')
    name = input('Name: ')
    n = 0
    catagories = ['English', 'Maths','Physics','Chemistry','CS']
    while n < 5:
        command = input('Wants to edit (y/n)? ')
        if command == 'y':
            new_name = input('Enter the name ')
            school[roll][new_name] = (school[roll]).pop(name)
        if command == 'n':
            print('Mark',catagories[n],end=' ')
            point = int(input())
            school[roll][name][n][catagories[n]] = point
            n = n + 1
    for name in school[roll]:
        print('Name', name)
        for i in school[roll][name]:
            for k, v in i.items():
                print(k, v)
        print()

def delete_record():
    roll= input('Roll Number: ')
    print()
    print('Pupli detail ')
    for name in school[roll]:
        print('Name', name)
        for i in school[roll][name]:
            for k, v in i.items():
                print(k, v)
    print('record found and deleted')
    print()
    school.pop(roll)
    print()
def clases_result():
    choice = input('Enter the roll you want to search: ')
    print()
    print()
    print('PUPIL DTEAIL...')
    for name in school[choice]:
        print('Name:', name)
        for i in school[choice][name]:
            for k, v in i.items():
                print(k, v)
    print()
def pupil_record():
    print()
    print('Roll  Name',' '*10,'English Maths Physics Chemistry CS ')
    for roll in school:
        print(roll,end= '    ')
        for name in school[roll]:
            print('{:<20}'.format(name),end='')
            for i in school[roll][name]:
                for k,v in i.items():
                    print(v,end='      ')
            print()
            print()

def Report():

    while True:
        print('''REPORT MENU
1. CLASS RESULT
2. PUPIL REPORT CARD
3. BACK TO MAIN MENU''')
        choice = input('Enter choice (1-4): ')
        if choice == '1':
            clases_result()
        elif choice =='2':
            pupil_record()
        elif choice == '3':
            break
    print()
def admin():
    while True:
        print('''1. CREATE PUPIL RECORD
2. DISPLAY ALL PUPILS RECORD
3. SEARCH PUPIL RECORD
4. MODIFY PUPIL RECORD
5. DELETE PUPIL RECORD
6. BACK TO MAIN MENU''')
        choice = input('Enter your choice (1-6): ')
        if choice == '1':
            func1_store_data()
        elif choice == '2':
            funtion_print()
        elif choice == '3':
            search_pupil()
        elif choice == '4':
            modify()
        elif choice =='5':
            delete_record()
        elif choice == '6':
            break
    print()
def main_ui_ux():
    while True:
        print('{:->15}{}{:->15}'.format('', 'Choose option', ''))
        command = ['Report', 'Admin', 'Exit']
        j = 1
        for i in command:
            print(j, i)
            j += 1
            print()
        choice = input('Enter your choice: ')
        if choice == '1':
            Report()
        elif choice == '2':
            admin()
        elif choice =='3':
            quit()
    print()
main_ui_ux()