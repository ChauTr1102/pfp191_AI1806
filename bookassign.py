class Book_control:
    def __init__(self):
        self.book_list = []
        self.for_print = []
    def enroll_book(self,book):
        self.book_list.append(book)

    def print_infor(self):
        for book in self.book_list:
            print('{:<30}{:<30}{:<10}{:<10}'.format(book.name,book.author,book.year,book.price))

    def sort_by_year(self):
        self.book_list = sorted(self.book_list,key= lambda x: x.year,reverse= True)

        self.print_infor()

    def search_by_name(self,name):
        found = False
        for books in self.book_list:
            if  name == books.name:
                books.print_infor()
                found = True
        if not found:
            print('NOT FOUND')

    def search_by_author(self,author):
        found = False
        for books in self.book_list:
            if  author == books.author:
                books.print_infor()
                found = True
        if not  found:
            print('NOT FOUND')

    def print_at_input_list(self,book):
        self.for_print.append(book)

    def print_input(self):
        for book in self.for_print:
            print('{:<30}{:<30}{:<10}{:<10}'.format(book.name,book.author,book.year,book.price))
        self.for_print.clear()

class Book:
    def __init__(self,name,author,nxb,year,price):
        self.name = name
        self.author = author
        self.nxb = nxb
        self.year = year
        self.price = price
    def print_infor(self):
        print('{:<30}{:<30}{:<10}{:<10}'.format(self.name , self.author , self.year , self.price))

library = Book_control()
book_1 = Book('C_Programming_Language','Dennis_Ritchie','Prentice_Hall'
              ,1988,59000)
book_2 = Book('Programming_in_ANSI_C','Balagurusamy','unknown',2012,600000)
library.enroll_book(book_1)
library.enroll_book(book_2)

def cau4():
    choice = input('Enter name of the book: ')
    library.search_by_name(choice)

def cau5():
    choice = input('Enter name of author: ')
    library.search_by_author(choice)

def input_():
    while True:
        number = int(input('How many Books: '))
        for i in range(number):
            name = input('Name: ')
            author = input('Author: ')
            nxb = input('NXB: ')
            year = int(input('Year of puplication: '))
            price = int(input('Price: '))
            book = Book(name,author,nxb,year,price)
            library.enroll_book(book)
            library.print_at_input_list(book)
        break

def Menu():
    while True:
        choice = input(f'''===========================================
1. Nhap thong tin cua n cuon sach cua FU
2. In ra man hinh thong tin vua nhap
3. Sap xep thong tin giam dan theo nam xuat ban va hien thi
4. Tim kiem theo ten sach
5. Tim kiem theo ten tac gia
6. Thoat
========================================'''
                       )
        if choice == '1':
            input_()
        elif choice =='2':
            library.print_input()
        elif choice  =='3':
            library.sort_by_year()
        elif choice == '4':
            cau4()
        elif choice =='5':
            cau5()
        elif choice == '6':
            quit()

Menu()