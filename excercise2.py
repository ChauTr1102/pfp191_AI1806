
class Phieu:
    def __init__(self,name,open,end):
        self.name = name
        self.open = float(open)
        self.end = float(end)
        self.ave = round(self.end - self.open,3)

    def print_co_phieu(self):
        print(self.name , self.open , self.end , self.ave)

class Thi_truong:
    def __init__(self):
        self.list_co_phieu = []

    def enroll_co_phieu(self,co_phieu):
        self.list_co_phieu.append(co_phieu)

    def print_infor(self):

        for co_phieu in self.list_co_phieu:
            print(co_phieu.name , co_phieu.open , co_phieu.end , co_phieu.ave)

    def function1(self):
        self.list_co_phieu = sorted(self.list_co_phieu,key= lambda x: (x.name,x.ave))
        Thi_truong.print_infor(self)

    def search_by_name(self,name):
        found = False
        for co_phieu in self.list_co_phieu:
            if co_phieu.name == name:
                co_phieu.print_co_phieu()
                found = True
        if not found:
            print('NOT FOUND')
        if found:
            self.list_co_phieu = list(filter(lambda x : x.name == name,self.list_co_phieu))
            print(f'''max = {max(self.list_co_phieu,key= lambda x: x.end).end } 
min = {min(self.list_co_phieu,key= lambda x: x.end).end}''')
    def function_3(self):
        sort = []
        empty = []
        for phieu in sorted(self.list_co_phieu,key=lambda x: x.name):
            sort.append({'name':phieu.name,'ave':phieu.ave})
        i = 0
        j = 3
        while j <= len(sort):
            empty.append(sort[i:j])
            i += 3
            j += 3
        j = 0
        found = False
        for co_phieu in empty:
            if [n['ave'] for n in co_phieu] == [ n['ave'] for n in sorted(co_phieu,key=lambda x: x['ave'])]:
                print(co_phieu[0]['name'])
                found = True
        if not found:
            print('NOT FOUND')
    def function4(self):
        self.list_co_phieu = sorted(self.list_co_phieu,key=lambda x:x.ave)
        print(f'the day has higest value {self.list_co_phieu[0].name}')
    def function_5(self):
        print('Trịnh Minh Châu AI-1806')
        quit()
thi_truong = Thi_truong()

with open('data.txt') as file:
    file.seek(3,0)
    for line in file:
        student = Phieu(line.split()[0],line.split()[1],line.split()[2])
        thi_truong.enroll_co_phieu(student)

    while True:
        choice = input('chose your selection: ')
        if choice == '1':
            thi_truong.print_infor()
        elif choice == '2':
            choice = input('name of share: ')
            thi_truong.search_by_name(choice)
        elif choice  == '3':
            thi_truong.function_3()
        elif choice =='4':
            thi_truong.function4()
        elif choice == '5':
            thi_truong.function_5()

