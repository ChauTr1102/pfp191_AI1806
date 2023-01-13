#Q3 (2.5 marks). Write a program that performs the following tasks:
def main():
    import math
    def check():
#1. Input 4 real numbers a, b, c and x.
        while True:
            try:
                a = int(input("nhap so a: "))
                b = int(input('nhap so b: '))
                c = int(input('nhap so c: '))
                x = int(input('nhap so x: '))
            except:
                print('error')
                continue
#2. Calculate S1 = ax 2 + bx + c.
            S_1 = a * x ** 2 + b * x + c
            print('gia tri s1 la:',S_1)
#3. Calculate S2 = acb42 if b 2 - 4ac &gt; 0, otherwise S2 = 0
            if (b ** 2 - 4 * a * c) > 0:
                print('S2 =',round(math.sqrt(b ** 2 - 4 * a * c),2))
            else:
                print('S2 = 0')
            break
    check()
#4. Re-input a, b and c. Check whether a, b and c are sides of a triangle or not
    def q():
        while True:
            try:
                a = int(input("nhap so a: "))
                b = int(input('nhap so b: '))
                c = int(input('nhap so c: '))
            except:
                print('your input wrong')
                continue
#If a, b, c are sides of a triangle, then calculate its perimeter and area, otherwise display on the
#screen a message &quot;a, b, c are not side of a triangle&quot;. The area is calculated by the Heron formula
#below:

            if a + b > c and a + c > b and b + c > a and a > 0 and a > 0 and b > 0 and c > 0 :
                print('a,b,c are side of a triangle')
                perimeter = a + b + c
                p = perimeter / 2
                erea = math.sqrt(p * (p - a) * (p - b) * (p - c))
                print('perimeter =', perimeter)
                print('erea =',p)
            else:
                print('a,b,c are not side of a triangle')
            quit()
    q()
main()



