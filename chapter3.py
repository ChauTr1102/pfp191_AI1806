# đề bài: kiểm tra xem số có bao nhiêu chữ số, đổi ra đơn vị tiền việt nam

def main():
    while True:
        name = input('nhap ten cua ban vao day: ')
        def git(name):
            if name == name:
                print('hello',name,'have a good day',name)
        git(name)
        break

    while True:
        nhap = input('nhap so vao day: ')
        if nhap.startswith('0'):
            print('so khong thoa man')
            continue
        if nhap == 'xong':
            quit()
        try:
            so = int(nhap)

        except:
            print('loi, nhap lai so ')
            continue
        x = int(nhap)
        a = x * 23.3
        print(str(a) + 'k','usd')
           # print('so co',len(nhap),'chu so')
        if so < 10 and so >= 0:
            print('so co mot chu so ')
        elif so >= 100 and so <1000:
            print('so co ba chu so')
        elif so >= 10 and so <= 100:
            print('so co hai chu so')
        else:
            print('so lon hon ba chu so ')
            print('so co', len(nhap), 'chu so')
        continue
main()