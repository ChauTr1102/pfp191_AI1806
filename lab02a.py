def q1():
    def func1(*argument):
        print('Printing values')
        print(*argument,sep='\n', end='\n'*3)

    #call function with 3 arguments
    func1(20,40,60)

    #call function with 2 arguments
    func1(80,100)

    #Return multiple values from a function
    def caculation(a,b):
        return f'{a+b}, {a-b}'

    res = caculation(40,10)
    print(res)
q1()

def q2():
    def showemployee(a,b):
        print(f'Name: {a} salary: {b}')
    showemployee('Ben',12000)
    showemployee('Jessa',9000)

    def outer(a,b):
        var = a + b
        return var
    def outer_fun(a,b):
        return outer(a,b) + 5
    result = outer_fun(5,10)
    print(result)
q2()

def q3():
    def addition(n):
        if n == 0:
            return 0
        else:
            return n + addition(n-1)
    print(addition(10))

    def display_student(name,age):

        print(name,age)
    show_student = display_student
    display_student('Emma', 26)
    show_student('Emma', 26)


q3()
def q4():
    while True:
        so = input('original number ' )
        if so == 'done':
            break
        if so[::1] == so[::-1]:
            print('Given number palindrome')
        else:
            print('Given number is not palindrome')
    #tìm số lớn nhất trong một list, ở đây cách thứ nhất em sẽ dùng hàm max
    x = [4, 6, 8, 24, 12, 2]
    print(max(x))
    #cách hai là sẽ chọn biến đêr so sánh:
    largest = None
    for i in x :
        if largest is None:
            largest = i
        elif i > largest:
            largest = i
    print(largest)
q4()




