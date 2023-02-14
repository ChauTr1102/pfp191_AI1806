def q1():
    original = input('enter word that you want to check whether one string is an anagram of another string ' )
    check = input('enter word that you consider to be the original string ' )
    origin = ''
    check1 = ''
    for i in original:
        if i.isalpha():
            origin += i

    for i in check:
        if i.isalpha():
            check1 += i
    def thu(check1):
        for i in check1:
            if i not in origin:
                return False
                break
        return True
    if thu(check1) :
        print(original,'is an anagram letter of',check)
    else:
        print(original,'is not an anagram letter of',check)
q1()
def q2():
    def hex_to_decimal(string):
        try:
            return int(string, 16)
        except ValueError:
            return "Error: Not a valid hexadecimal string."

    input_string = input("Enter a string: ")
    result = hex_to_decimal(input_string)
    print(result)
q2()