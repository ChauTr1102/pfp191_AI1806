# đề bài kiểm tra xem trong hai số đầu là max:
def main():
    while True:
        x = input('nhap so dau tien: ')
        if x == 'xong':
            quit()
        y = input('nhap so thu hai: ')
        if x == 'xong':
            quit()
        try:
            a = int(x)
            b = int(y)
        except:
            print('hay nhap lai')
            continue
        if a > b :
            print('so lon nhat la:',a)
        if b > a :
            print('so lon nhat la:',b)
main()
