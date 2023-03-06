def q1():
    with open('story.txt','r') as file:
        for line in file:
            print(line,end='')
        file.seek(0)
        count= 0
        for sentence in file:
            if sentence.startswith('T'):
                continue
            else:
                count+= 1
        print(f'lines not starting with \'T\': {count}')
q1()
def q2():
    with open('story.txt','r') as file:#1
        count = list()
        for sentence in file:
            for word in sentence.split():
                count.append(word)
        print(f'total word are {len(set(count))}')

        #2
        file.seek(0)
        for sentence in file:
            for word in sentence.split():
                if len(word) <4:
                    print(word,end=' ')
q2()

def q3():
    store = []
    with open('story.txt' , 'r') as file:
        dem = 0
        print()
        for sentence in file:
            for word in sentence.split():
                store.append(word)
                if word.upper():
                    dem += 1
        print(dem)
        count = 0
        for word in store:
            if any([word == 'this',word == 'these']):
                count += 1
        print(f'there are {count} \'this\' and \'these\' word')
q3()
def q4():
    def hash_display():
        begin = ''
        with open('story.txt','r') as file:
            for word in file.readlines():
                for char in word:
                    if char == '':
                        continue
                    else:
                        begin += char +'#'
        print(begin)
    with open('wolrd.txt','r') as file:
        begin =''
        for word in file.readlines():
            for char in word:
                if char == 'J':
                    begin += 'I'
                else:
                    begin += char
        print(begin)
q4()


