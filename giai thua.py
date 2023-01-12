# đề bài: tính n giai thừa
def main():
    while True:
        a = input('nhap so can tinh giai thua vao day: ' )
        try:
            x = int(a)
        except:
            print('hay nhap lai so')
        def so(x):
            gt = 1
            if x == 1:
                return 1
            else:
                for i in range(1, x + 1):
                    gt = i * gt
                return gt
        print(so(x))
main()