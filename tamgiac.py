#kiem tra xem ba so co tao thanh hinh tma giac

def main():

    while True:
        a = input('nhap so a: ')
        b = input('nhap so b: ')
        c = input('nhap so c: ')
        try:
            x = int(a)
            y = int(b)
            z = int(c)
        except:
            print('your input wrong')
            continue
        if x + y > z or x + z > y or z + y > x and x > 0 and y > 0 and z > 0 :
            print('day la mot hinh tam giac')
        else:
            print('day ko phai la hinh tam giac')
        continue
main()

