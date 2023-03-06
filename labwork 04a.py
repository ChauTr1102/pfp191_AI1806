def q1():
    import datetime

    # get current date and time
    now = datetime.datetime.now()

    # create filename with timestamp
    filename = f"file_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    # create file
    with open(filename, "w") as f:
        f.write("This is a file created with a timestamp.")
    q1()
# import os
#q3

# file_path = 'C:\Users\LENOVO\Documents\code\code thiếu nhi\26'
# os.umask(0)
# open(file_path, 'a').close()
# os.chmod(file_path, 0o600)


with open('q2.txt','w') as file:
    file.write('Done writing \n')
    file.write('This is new content')
with open('test.txt','w')as file:
    file.write('this is new content\n')
    file.write('Opening file again\n')
    file.write('This is overwriten file')
def q3():
    with open('q2.txt','w') as file:
        file.write('''Name: Emma
    Adress: 221 Backer street
    City: London''')
    with open('test2.txt','r+')as file:
        print(file.readline(),end='')
        print(f'file handle at {file.tell()}')
        print(file.readline(),end= '')
        print(f'file handle at {file.tell()}')
        file.seek(2,0)
        print(file.readline(),end='')
        file.seek(0,1)
        print(file.readline(),end='')
        print(f'file handle at {file.tell()}')
#
import os


old_file_name = 'old_file.txt'
new_file_name = 'new_file.txt'


if os.path.exists(old_file_name):
    os.rename(old_file_name, new_file_name)
    print(f"File '{old_file_name}' has been renamed to '{new_file_name}'")
else:
    print(f"File '{old_file_name}' does not exist")
import os
def rename_file():

    dir_path = 'C:\Users\LENOVO\Documents\code\code thiếu nhi\26' #this may not work in your computer

    file_list = os.listdir(dir_path)

    for file_name in file_list:

        if 'old_string' in file_name:

            new_file_name = file_name.replace('old_string' , 'new_string')


            old_file_path = os.path.join(dir_path , file_name)
            new_file_path = os.path.join(dir_path , new_file_name)


            os.rename(old_file_path , new_file_path)
            print(f"File '{file_name}' has been renamed to '{new_file_name}'")
def rename_with_time():
    import os
    import datetime


    dir_path = 'C:\Users\LENOVO\Documents\code\code thiếu nhi\26'


    file_list = os.listdir(dir_path)

    for file_name in file_list:

        file_path = os.path.join(dir_path , file_name)


        if os.path.isfile(file_path) and not file_name.startswith('new_'):

            now = datetime.datetime.now()


            new_file_name = f"new_{now.strftime('%Y-%m-%d_%H-%M-%S')}_{file_name}"
            new_file_path = os.path.join(dir_path , new_file_name)


            os.rename(file_path , new_file_path)
            print(f"File '{file_name}' has been renamed to '{new_file_name}'")
import os


old_file_path = 'C:\Users\LENOVO\Documents\code\code thiếu nhi\26'


new_file_path = 'C:\Users\LENOVO\Documents\code\code thiếu nhi\26'

# check if the old file exists
if os.path.exists('C:\Users\LENOVO\Documents\code\code thiếu nhi\26'):
    # rename the file    os.rename(old_file_path , new_file_path)
    print(f"File '{C:\Users\LENOVO\Documents\code\code thiếu nhi\26}' has been renamed to '{C:\Users\LENOVO\Documents\code\code thiếu nhi\23}'")

    # move the file to the new location
    os.replace('C:\Users\LENOVO\Documents\code\code thiếu nhi\26' , '/path/to/new_location/new_file.txt')
    print(f"File '{C:\Users\LENOVO\Documents\code\code thiếu nhi\23}' has been moved to the new location")
else:
    print(f"File '{C:\Users\LENOVO\Documents\code\code thiếu nhi\26}' does not exist")
