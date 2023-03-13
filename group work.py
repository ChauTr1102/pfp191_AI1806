
class Gadget_control:
    def __init__(self):
        self.gadget_list = []
        self.ram_list = ['1','2','4','8','12']
        self.cpu_list = ['I7','I5','I3']
    def enroll(self,gadget):
        self.gadget_list.append(gadget)

    def print_infor(self):
        print(len(self.gadget_list))
        for gadget in self.gadget_list:
            print(gadget.cpu,gadget.ram)

    def cpu_upadate(self,number,name):
        self.gadget_list[number - 1].cpu = name.upper()

    def ram_update(self,number,name):
        self.gadget_list[number - 1].ram = name

    def search_by_ram_or_cpu(self,name):
        if name.upper() in self.cpu_list + self.ram_list:
            for gadget in self.gadget_list:
                if name.upper() == gadget.cpu:
                    gadget.print_infor_of_gadget()
                elif name == gadget.ram:
                    gadget.print_infor_of_gadget()
        else:
            print('Gia tri tim kiem khong hop le')
            
control = Gadget_control()

class Gadget:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def print_infor_of_gadget(self):
        print(self.cpu,self.ram)

def function_1():
    choice = input('your file: ')
    try:
        flag = False
        file = open(choice,'r+')
        file.seek(3,0)
        for line in file.readlines():
            if any([line.split()[0] not in control.cpu_list,line.split()[1] not in control.ram_list]):
                flag = False
            else:
                gadet = Gadget(line.split()[0],line.split()[1])
                control.enroll(gadet)
                flag = True
        if  flag:
            file.seek(0 , 0)
            print(f'So may vua them moi: {file.readline()}')
        if not flag:
            print('invalid')
    except:
        print('File khong ton tai')

def function_2():
    choice = int(input('Choose your id: '))
    if int(choice) not in range(1,len(control.gadget_list)+1):
        print('invalid')
    else:
        while choice <= len(control.gadget_list) and choice != 'STOP':
            new_cpu = input('your new cpu: ')
            if new_cpu == 'STOP':
                break
            if new_cpu.upper() not in control.cpu_list:
                print('invalid')
                continue
            control.cpu_upadate(choice,new_cpu)
            choice+=1

def function_3():
    choice = int(input('Choose your id: '))
    if choice not in range(1,len(control.gadget_list)+1):
        print('invalid')
    else:
        while choice <= len(control.gadget_list) :
            new_ram = input('your new ram: ')
            if new_ram == 'STOP':
                break
            if new_ram not in control.ram_list:
                print('unvalid')
                continue
            control.ram_update(choice,new_ram)
            choice+=1

def function_4():
    choice = input('your cpu or ram name: ')
    control.search_by_ram_or_cpu(choice)

def menu():
    while True:
        choice = input(f'''====Program for management computers====
1) Load Data Files:
2) Update CPU info:
3) Update Ram info:
4) Search:
5) Quit
''')

        count = 0
        if choice == '1':
            if count > 20:
                print('Danh sach da day, khong them duoc.')
            count += 1
            function_1()
        elif choice == '2':
            function_2()
        elif choice == '3':
            function_3()
        elif choice == '4':
            function_4()
        elif choice  == '5':
            quit()
menu()
