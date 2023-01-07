def main():
    while True:

        hs = input('Enter Hours: ')
        r = input('Enter Rate: ')
        try:
            a = float(hs)
            b = float(r)
        except:
            print('error, please reinput ')
        print('Pay:',a * b)
        continue
main()