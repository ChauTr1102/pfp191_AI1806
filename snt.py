#kiểm tra xem có phải số nguyên tố hay ko
def main():
    while True:
        snt = input('nhap so vao day: ')
        if snt == 'xong':
            quit()
        try:
            nt = int(snt)
        except:
            print('error')
            continue
        def checkso(x):
            def ksnt():
                return 'khong phai so nguyen to'
            def snt():
                return 'la so nguyen to'
            if x == 2:
                return snt()
            if x < 2:
                 return 'khong phai so nguyen to'
            for i in range(2, x - 1 ):
                if x / i == 0:
                    return ksnt()
                else:
                    return snt()
        print(checkso(nt))


main()


