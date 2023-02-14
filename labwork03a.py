def q1():
    for i in range(5):
        for k in range(1,i+2):
            print(k,end=' ')
        print()



    number = int(input('Enter number '))
    run = 0
    for i in range(1,number+1):
        run += i
    print('Sum is', run)
q1()
def q2():
    list1 = [1,75,150,145,34,8,533,423,12,324]
    for i in list1:

        if i > 150:
            continue
        if i > 500:
            break
        if i % 5 == 0:
            print(i)
    number = input('enter number: ')
    zork = 0
    for i in number:
        zork += 1
    print('there are total {} digits in number {}'.format(zork,number))
    list1 = [10,20,30,40,50]
    for i in list1[::-1]:
        print(i)
q2()
#1
def q3():
    while True:
        letter = input('enter letter here: ')
        print('type \'done\' to quit')
        if letter == 'done':
            break
        if len(letter) %2 == 0:
            half = int(len(letter) /2)
            four_chars = letter[half-2:half+2]
        if len(letter) %2!=0:
            half = int((len(letter) -1) /2)
            four_chars = letter[half-1:half+3]
        print('Original string is',letter)
        print('Middle four chars is',four_chars)
    #2
    s1 = 'Ault'
    s2 =  'Kelly'
    half = int(len(s1)/2)
    new = s1[:half] + s2 + s1[half::]
    print(new)
#3
    s1 = 'America'
    s2 = 'Japan'
    def half(n):
        return int((len(n) -1) /2 )

    new = s1[0] + s2[0] +s1[half(s1)] +s2[half(s2)] + s1[-1] +s2[-1]
    print(new)
#4
    str1 = 'PyNaTive'
    lower = ''
    upper = ''
    for i in str1:
        if str1.islower():

            lower +=i
        else:
            upper += i
    new = lower + upper
    print(new)
    string = 'fsdj23443sf^%^@#$@&^&sdlkfsdjl'
    char = 0
    digit = 0
    sym = 0
    for i in string:
        if i.isalpha():
            char += 1
        elif i.isdigit():
            digit += 1
        else:
            sym += 1
    print('total counts of chars, digits and symbols\nChars = {} ,Digit = {}, symbol = {}'.format(char,digit,sym))
q3()
def q4():
    #1
    str1 = 'i am 25 years old and 10 months'
    num = list()
    for i in  str1:
        if i.isdigit():
            num.append(i)
    print(''.join(num))
    #2
    str2 = '/*jon is @developer & Musiction'
    new = list()
    word = str2.split()
    for i in word:
        i = i.strip('!@#$/%^&*()_+')
        new.append(i)
    print(' '.join(new))
    #3
    str = ['Emma','jon','','Kelly','None','Eric','']
    print('original: ',str)
    for i in str:
        if i =='':
            str.remove(i)
    print('after removing empty string: ',str)
    #4
    str1 = 'Emma-is-a-data-scientist'
    new = str1.split('-')
    print(' '.join(new))
q4