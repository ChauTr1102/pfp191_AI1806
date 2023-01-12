def main():
    while True:
        h = input('enter hour')
        r = input('enter rate')
        try:
            hs = int(h)
            hr = int(r)
        except:
            print('error')
            continue
        pay = hs * hr
        if hs <= 40:
            print('pay:',pay)
            break
        else:
            print('pay:',pay + (40 - hs ) * 1.5 * hr )
            break
main()