
#function with 3 arguments
def main():
    word = input('enter a string: ')
    print('enter two number: ',end=" ")
    st1= input()
    st2 = input()
    print(word.replace(st1,st2))

    string = input('enter a string: ')
    for i in string:
        if all([i != ' ' , string.count(i) > 1]):
            print('{} - {} times'.format(i,string.count(i)))
        elif all([string.count(i) == 1 , i != ' ']):
            print('{} - {} time'.format(i, string.count(i)))
main()
