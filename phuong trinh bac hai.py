
# đề bài: giải phương trình bậc hai bất kỳ
def main():
    import math
    while True:
        x = input('nhap he so a: ')
        y = input('nhap he so b: ')
        z = input('nhap he so c: ')
        if x == 'done':
            quit()
        try:
            a = int(x)
            b = int(y)
            c = int(z)
        except:
            print('he so khong thoa man hay nhap lai. ')
            continue
        delta = b ** 2 - 4 * a * c
        if delta < 0 :
            print('phuong trinh vo nghiem')
        else:
            print('x1 =',(b ** 2 - math.sqrt(delta) / 2 * a),end='')
            print( ' x2 =',(b ** 2 - math.sqrt(delta) / 2 * a))
main()



