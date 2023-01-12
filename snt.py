#kiểm tra xem có phải số nguyên tố hay ko
def main():
    flag = True
    while True:
        a = input('nhap so vao day: ')
        if a == 'xong':
            break
        try:
            st = int(a)
        except:
            print('hay nhap lai so ')
            continue
        if st < 2:
            flag = False
        elif st == 2:
            flag = True
        else:
            for i in range (2, st):
                if st % i == 0:
                    flag = False
        if flag == True:
            print(st, " là số nguyên tố")
        else:
            print(st, " không phải là số nguyên tố")
main()







