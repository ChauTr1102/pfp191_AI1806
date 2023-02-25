


def cau1():
    print('{:->26}{}{:->29}'.format('', 'Cau 1', ''))
    word = input('Input string: ')
    store = [i for i in word]
    for i in set(store):
        print('{:3}{:>10}'.format(f'\'{i}\'',word.count(i)))
# cau1()

def cau2():
    print('{:->26}{}{:->29}'.format('', 'Cau 2', ''))
    word = input('Input string: ')
    empty = ''
    for i in word:
        if i.upper() == i:
            i = i.lower()
        else:
            i = i.upper()
        empty += i
    print('Result:\n',empty,sep='')
# cau2()


def cau3():
    print('{:->26}{}{:->29}'.format('', 'Cau 3', ''))
    word = input('Input string: ')
    chu = word.split()
    hoa_chu_dau = list(map(lambda x: x[0].upper() + x[1::].lower(),chu))
    print('Result:\n',' '.join(hoa_chu_dau),sep='')
# cau3()


def cau4():
    print('{:->26}{}{:->29}'.format('', 'Cau 4', ''))
    word = input('Input string: ')
    empty = ''
    for i in word:
        if i.isalpha() != True:
            empty += ' '
            continue
        empty += i
    print('Result:\n',empty,sep='')
# cau4()


def cau5():
    print('{:->26}{}{:->29}'.format('', 'Cau 5', ''))
    word = input('Input string: ').split()
    empty = ''
    for i in word:
        if len(i) >= 4:
            empty += (len(i) *'#' +' ')
            continue
        empty += i +' '
    print('Result\n',empty,sep='')
# cau5()


def cau6():
    print('{:->26}{}{:->29}'.format('', 'Cau 6', ''))
    sentence = input('Input string: ')
    emp = ''
    j = 0
    while j < len(sentence):
        if sentence[j] == sentence[j-1]:
            emp += ''
        else:
            emp += sentence[j]
        j += 1
    print('Result\n',emp,sep='')
# cau6()


def cau7():
    print('{:->26}{}{:->29}'.format('', 'Cau 7', ''))
    sentence = input('Input string: ')
    emp = ''
    for i in sentence:
        if i == '':
            continue
        elif i not in ['u','e','o','a','i']:
            emp += '-'+i+'-'
        emp += i
    print('Result\n',emp,sep='')
# cau7()


def cau8():
    print('{:->26}{}{:->29}'.format('', 'Cau 8', ''))
    sentence = input('Input string: ')
    word = list(n for n in sentence)
    name = sentence[:word.index('@')]
    print('Result\n',name,sep='')
def cau9():
    print('{:->26}{}{:->29}'.format('', 'Cau 9', ''))
    sentence = input('Input string: ')
    sentence2 = input('Input string: ')
    j = 0
    count = 0
    while j <= len(sentence) -3:
        if sentence[j:j+3] == sentence2[j:j+3]:
            count += 1
        j += 1
    print('Result\n',count,sep='')


def cau10():
    print('{:->26}{}{:->29}'.format('', 'Cau 10', ''))
    sentence = input('Input string: ')
    sentence2 = input('Input string: ')
    j = 0
    count = 0
    while j < len(sentence) :
        if sentence[j] == sentence2[j]:
            count += 1
        j += 1
    print('Result\n',count/len(sentence) *10,sep='')



def uiux():
    print('{:->20}{}{:->20}'.format('','Student Information',''))
    data = {'Name':'your name','ID':'your class','Class':'your class'}
    for k,v in data.items():
        print('{:5}{:<15}{:^15}{}'.format('',k,':',v))
    print('{:->59}'.format(''))
    print()
    print('{:->26}{}{:->29}'.format('','MENU',''))
    word = ['a','b','c','d','e','f','g','h','i','j']
    base = dict()
    j = 6
    for i in range(1,len(word)+1):
        base[word[i-1]] = i
    for k,v in base.items():
        if k == 'f':
            break
        print('{:>15} Cau {:<15} {} Cau {}'.format('['+k+']',v,'['+word[j-1]+']',j))
        j += 1
    print('{:->26}{}{:->29}'.format('','EXIT',''))
    print('{:->59}'.format(''))



def rule():
    while True:
        choie = input('enter your opinion: ')
        if choie == 'a':
            cau1()
        elif choie == 'b':
            cau2()
        elif choie == 'c':
            cau3()
        elif choie == 'd':
            cau4()
        elif choie == 'e':
            cau5()
        elif choie == 'f':
            cau6()
        elif choie == 'g':
            cau7()
        elif choie == 'h':
            cau8()
        elif choie == 'i':
            cau9()
        elif choie == 'j':
            cau9()
uiux()
rule()

