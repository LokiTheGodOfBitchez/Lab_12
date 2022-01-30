def rec(n):
    if n == 0:
        print(n)
        return
    else:
        print(n)
        rec(n - 1)


if __name__ == '__main__':
    num = int(input('Enter the number: '))
    rec(num)
