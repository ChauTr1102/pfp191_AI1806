#Q4 (2.5 marks). Write a program to accept 3 real numbers a, b, c, then:
#1. Display the maximum and minimum values among them.
#2. Arrange them in ascending order, i.e. a ≤ b ≤ c.
def main():
    #1. Display the maximum and minimum values among them
    while True:
        try:
            a = int(input('nhap so a: '))
            b = int(input('nhap so b: '))
            c = int(input('nhap so c: '))
        except:
            print('wrong input')
            continue
        empty = (a, b, c)
        print('the minimum is',min(empty))
        print('the maximum is', max(empty))
    # 2. Arrange them in ascending order, i.e. a ≤ b ≤ c.
        empty = sorted(empty)
        print('Arrange in ascending order:',end=' ')
        for i in empty:
            print(i,end=' ')
        quit()
main()


