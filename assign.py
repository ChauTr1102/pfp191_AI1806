

class Book:
    def __init__(self,name,author,nxb,year,price,):
        self.name = name
        self.author = author
        self.nxb = nxb
        self.year = year
        self.price = price

class Library:
    def __init__(self):
        self.book_list = []
        self.for_sort = []
    def enroll_book(self,book):
        self.book_list.append(book)

    def export_to_file(self):
        with open('fu.txt','w') as file:
            file.write(f'{len(self.book_list)}')
            file.write('\n'*2)
            for book in self.book_list:
                file.write(f'''{book.name}
{book.author}
{book.nxb}
{book.year}
{book.price}

''')

    def find_by_author(self,  author):
        for book in self.book_list:
            if book.author != author:
                continue
            else:
                print(f'''{book.name} 
{book.author}
{book.nxb}
{book.year}
{book.price}''')
                break
            print('Không tìm thấy cuốn sách nào.')

    def find_by_name(self,name):
        for book in self.book_list:
            if book.name != name:
                continue
            else:
                print(f'''{book.name} 
{book.author}
{book.nxb}
{book.year}
{book.price}''')
                break
            print('Không tìm thấy cuốn sách nào.')
    def xep(self):
        for book in self.book_list:
            self.for_sort.append({'name': book.name,'author' :book.author, 'year' : book.year, 'price' : book.price})
        self.for_sort = sorted(self.for_sort,key=lambda x: (x['year'],x['price']),reverse=True)
        print("{:<30}{:<30}{:^10}{:^10}".format('Name' , 'Author' , 'Year' , 'Price'))
        print()
        for book in self.for_sort:
            print("{:<30}{:<30}{:^10}{:^10}".format(book['name'],book['author'],book['year'],book['price']))
            print()
        with open('FU2022.txt','w') as file:
            for book in self.for_sort:
                file.write("{:<30}{:<30}{:^10}{:^10}".format(book['name'],book['author'],book['year'],book['price']))
                file.write('\n')

thuvien = Library()
test_book = Book('C_Programming_Language','Dennis_Ritchie','Prentice_Hall',1988,59000)
intro = Book('Programming_in_ANSI_C','Balagurusamy','fsdfdsf',2012,600000)
second = Book('nothing','yes','so',1111,11111111)
thuvien.enroll_book(second)
thuvien.enroll_book(intro)
thuvien.enroll_book(test_book)

# thuvien.find_by_name('Programming_in_ANSI_C')

tohon = []
def nhap():

    global tohon
    count = int(input('Ban muon nhap bao nhieu cuon: '))
    for i in range(count):
        name = input('name: ')
        author = input('Author: ')
        nxb = input('NXB: ')
        year = int(input('Year: '))
        price = int(input('price: '))
        print()
        book = Book(name,author,nxb,year,price)
        thuvien.enroll_book(book)
        tohon.append([name,author,nxb,year,price])
def inra():
    global tohon
    for i in tohon:
        print("{:<30}{:<30}{:^10}{:^10}".format(i[0],i[1],i[3],i[4]))
        print()
def timkiemten():
    name = input('name: ')
    thuvien.find_by_name(name)
def timtacgia():
    tacgia = input('Author')
    thuvien.find_by_author(tacgia)
def Menu():
    while True:
        choice = input("""1. Nhap thong tin cua n cuon sach cua FU
2. In ra man hinh thong tin vua nhap
3. Sap xep thong tin giam dan theo nam xuat ban va hien thi
4. Tim kiem theo ten sach
5. Tim kiem theo ten tac gia
6. Thoat

""")
        if choice == '1':
            nhap()
        elif choice =='2':
            inra()
        elif choice =='3':
            thuvien.xep()
        elif choice =='4':
            timkiemten()
        elif choice =='5':
            timtacgia()
        elif choice =='6':
            quit()
Menu()