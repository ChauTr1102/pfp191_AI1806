

class tung_ngay:
    def __init__(self,name,start,end):
        self.name = name
        self.start = start
        self.end = end

class data:
    def __init__(self):
        self.data_list = []
        self.tong = list()
        with open('data.txt' , 'r') as file:
            file.seek(3 , 0)
            for line in file.readlines():
                data = tung_ngay(line.split()[0] , float(line.split()[1]) , float(line.split()[2]))
                self.data_list.append(data)

    def chuc_nang_1(self):
        for phieu in self.data_list:
            self.tong.append({'name':phieu.name,'start':phieu.start,'end':phieu.end,'ave': (phieu.end - phieu.start)})
        self.result = sorted(self.tong,key=lambda x: (x['start'],x['end']))
        for name in self.result:
            print('{} {} {} {}'.format(name['name'],name['start'],name['end'],round(name['ave'],3)))
    def chuc_nang_2(self,name):
        for_sort = []
        for co_phieu in self.data_list:
            if co_phieu.name != name:
                continue
            elif co_phieu.name == name:
                for_sort.append(co_phieu.end)
        print('highest: ',max(for_sort))
        print('lowest: ',min(for_sort))

    def chuc_nang_3(self):
        for i in self.data_list:
            if i.end > i.start:
                print(i.name)

    def chucnang4(self):
        for day  in self.data_list:
            if day == max(self.data_list,key= lambda x: (x.end - x.start)):
                print(day.name)


An = data()

def chuc_nang_5():
    print('Trinh Minh chau \nHE186561')
    quit()
def chucnang2():
    while True:
        choice = input('insert here ')
        An.chuc_nang_2(choice)
        break
def Menu():
    while True:
        choice = input("""Chức năng 1 (2đ): Đọc file.
Chức năng 2 (2đ): Tìm kiếm theo mã chứng khoán.
Chức năng 3 (1.5đ): Tìm kiếm những mã chứng khoán có xu hướng tăng.
Chức năng 4 (1.5đ): Tìm mã có số ngày tăng lớn nhất.
Chức năng 5 (1đ): Thoát chương trình.
""")
        if choice == '1':
            An.chuc_nang_1()
        if choice == '2':
            chucnang2()
        if choice == '3':
            An.chuc_nang_3()
        if choice == '4':
            An.chucnang4()
        if choice == '5':
            chuc_nang_5()
Menu()