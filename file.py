#chương trình cho phép nhập vào một file
# và ghi ra file sau đó tính xem từ nào xuất
# hiện nhiều nhất trong file, em vẫn đang
# triển khai thực thi trong một file cụ thể như file word

def how_many_time():
    file = input('nhap file: ')
    nhap =  open(file,'w')
    store = dict()
    emp = list()
    filter = list()
    largest = 0
    while True:
        data = input('nhap vao day: ')
        if data == 'done':
            break
        data += '\n'
        nhap.write(data)
        line = data.strip()
        line = data.strip('\n')
        word = line.split()
        for i in word:
            emp.append(i)
    for i in emp:
        if emp.count(i) > largest:
            largest = emp.count(i)
            occur_max = i
        if i not in filter:
            filter.append(i)
            print('\'{}\' xuat hien {} lan.'.format(i,emp.count(i)))
    print('tu xuat hien nhieu nhat la: {}'.format(occur_max))
    nhap= open(file,'r')
    nhap.close()
how_many_time()


#nhap vao mot day va cho ra snt trong day
emp = list()
round = int(input('ban muon nhap bao nhieu so '))
for i in range(1,round +1 ):
    number = int(input('nhap so vao day: '))
    emp.append(number)


choice = input('nếu muốn in ra số nguyên trong dãy thì hãy bấm: \'snt\' \ncòn nếu muốn in ra số gần nhất với \ngiá trị trung bình nhất của dãy thì hãy bấm \'ave\'')
def task_snt():
    prime = list()
    def snt(n):
        for i in range(2,n):
            if n % i == 0:
                return False
        if n <= 1:
            return False
        return True

    for n in emp:
        if snt(n):
            prime.append(str(n))
    print('cac so nguyen to la: ',' '.join(prime))

#in ra gia tri gan nhat voi gia tri trung binh cua day 
def ave():
    empty = list()
    ave = sum(emp) / len(emp)
    for i in emp:
        close = i - ave
        if close < 0 :
            close = close * -1
        empty.append(close)
    print ('so gan nhat voi gia tri trung binh la:', emp[empty.index(min(empty))])
if choice == 'snt':
    task_snt()
elif choice == 'ave':
    ave()












