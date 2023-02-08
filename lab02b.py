def q1():
    while True:
        so  = int(input('enter: '))
        if so <= 5:
            print('plese re-enter')
            continue
        count = 0
        for i in range(1,so+1):
            count += i
        print('S1 =' ,count)
        count = 1
        for i in range(1,so + 1):
            count = count * i
        print('S2=',count)
        count = 0
        for i in range(1,so +1):
            phan_so = 1 / i
            count += phan_so
        print('S3 = {}'.format(count))
        break
    while True:
        so = int(input('enter: '))
        if all([so <= 5, so<=1]):
            print('plese re-enter')
            continue


        def is_prime(so):
            if so <= 1:
                return False
            for n in range(2, so):
                if so % i == 0:
                    return False
            return True

        if is_prime(so):
            print(so, "is a prime number")
        else:
            print(so, "is not a prime number")
        break



q1()
def q2():
    def gcd(m, n):
        while n != 0:
            m, n = n, m % n
        return m

    def lcm(m, n):

        return m * n // gcd(m, n)

    def common_prime_dividers(m, n):

        common_primes = []
        for i in range(2, min(m, n) + 1):
            if m % i == 0 and n % i == 0:
                m //= i
                n //= i
                common_primes.append(i)
        return common_primes

    def main():
        m = int(input("Enter first integer: "))
        n = int(input("Enter second integer: "))

        print("Common prime dividers:", common_prime_dividers(m, n))
        print("GCD:", gcd(m, n))
        print("LCM:", lcm(m, n))

    if __name__ == "__main__":
        main()


q2()
def q3():
    def check_input(n):

        try:
            int(n)
            return True
        except ValueError:
            return False

    def binary_format(n):

        return bin(n).split('b')[1]

    def sum_of_digits(n):

        return sum([int(digit) for digit in str(n)])

    def reverse_number(n):

        return int(str(n)[::-1])

    def main():
        n = input("Enter an integer number: ")
        while not check_input(n):
            n = input("Invalid input. Enter an integer number: ")
        n = int(n)

        print("Binary format:", binary_format(n))

        n = int(input("Enter another integer number: "))
        print("Sum of digits:", sum_of_digits(n))

        print("Reverse number:", reverse_number(n))

    if __name__ == "__main__":
        main()
q3()
def q4():
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def palindrome_numbers(m, n):
        for i in range(m, n + 1):
            if is_palindrome(i):
                print(i)

    m = int(input("Enter the first number: "))
    n = int(input("Enter the second number: "))
    if m < n:
        palindrome_numbers(m, n)
    else:
        print("Invalid interval, second number must be greater than first number")
q4()