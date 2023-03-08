def q1():
    example_list_1 = [1,2,3]
    example_list_2 = [2,4,6]
    example_list_3 = [1.0 ,'chelsea',3]
    example_list_4 = []


    list1 = ['M','na','i','ke']
    list2 = ['y','me','s','lly']
    print(list1 + list2)

def q2():
    numbers= [1,2,3,4,5,6,7]
    print(list(n **2 for n in numbers))
    list1 = ['hello','take']
    list2 = ['dear','sir']
    result = []
    for i in list1:
        for k in list2:
            result.append(f'{i} {k}')
    print(result)

def q3():
    dict_1 = {'Ten': 10,'Twenty':20,'Thirsty': 30}
    dict_2 = {'Thirsty': 30,'Fourty':40,'Fifty':50}
    dict_1.update(dict_2)
    print(dict_1)
    sampleDict = {
        'class': {
            'student':{
                'name':'Mike',
                'marks':{
                    'physics':70,
                    'history':80
                }
            }
        }
    }
    print(sampleDict['class']['student']['marks']['history'])
    new = dict()
    employess = ['Kelly','Emma']
    defaults = {'designation' : 'Developer','salary': 8000}
    for name in employess:
        new[name] =  defaults
    print(new)

def q4():
    tuple1 = ('orange',[10,20,30],(5,15,25))
    print(tuple1[1][1])

    tuple_1 = (10,20,30,40)
    for i in tuple_1:
        print(i)
    tuple_3 = (11,22)
    tuple_4 = (99,88)
    tuple_3,tuple_4 = tuple_4 ,tuple_3
    print(tuple_3)
    print(tuple_4)

q4()