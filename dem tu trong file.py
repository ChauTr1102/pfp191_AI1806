def how_many_time():
    file = input('nhap file: ')
    nhap =  open(file)
    emp = list()
    filter = list()
    largest = 0
    for line in nhap:
        line = line.strip('\n')
        line = line.strip()
        word = line.split()
        for i in word:
            i = i.strip('.,:()')
            if i.isdigit():
                continue
            emp.append(i)
    print('{:_>45}'.format(''))
    print('|{:^18}{:>23}  |'.format('Từ', 'lần xuất hiện'))
    for i in emp:
        if emp.count(i) > largest:
            largest = emp.count(i)
            occur_max = i
        if i not in filter:
            filter.append(i)
            print('{}{:^19}  {:12}{:>11} '.format('|',i,emp.count(i),'|'))
    print('{:->45}'.format(''))
    print('tu xuat hien nhieu nhat la: \'{}\' voi {} lan xuat hien'.format(occur_max,largest))
    nhap= open(file,'r')
    nhap.close()
how_many_time()



