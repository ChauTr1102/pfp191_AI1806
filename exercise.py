def main():
    def snt(n):
        if n <2:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        return True
    num = int(input('input here: '))
    n = 2
    i = 1
    while i <= num:
        if snt(n):
            print(n,end=' ')
            i += 1
        else:
            i = i
        n += 1
main()
def bai2():
    he_chu = list()
    he_4 = list()
    he_10 = list()
    n = input('enter your file: ')
    file = open(n,'r+')
    for line in file:
        line = line.strip()
        line = line.split()
        he_chu.append(line[0])
        he_10.append(line[2])
        he_4.append(line[1])
    x = float(input('nhap diem '))
    for i in he_10:
        compare = float(i)
        if x >= compare:
            print('diem he 4: ',he_4[he_10.index(i)],', diem he chu: ',he_chu[he_10.index(i)])
            break
    file.close()
bai2()