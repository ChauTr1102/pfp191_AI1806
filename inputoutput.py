
# đề bài:
#input = 3 5 1 5 3 9
#output 3 5 1 9
# tìm số lón nhất trong các số đã cho


def main():
    largest =  None
    emp = list()
    while True:

        nhap = input('nhap so vao day: ')

        if nhap == 'xong':
            break

        if nhap in emp:
            continue
        else:
            emp.append(nhap)
            sorted(emp)

    for i in emp:
        print(i, end=' ')

        if largest is None or i > largest :
            largest = i
    print('so lon nhat la:',largest)

main()


