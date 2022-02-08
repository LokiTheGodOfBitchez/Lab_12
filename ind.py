x = input("Write x: ")
n = input("Write n: ")


def rec(x, n):
    if n == 0:
        print(1)
        return
    elif n < 0:

        rec(n - 1)


if __name__ == '__main__':
    num = int(input('Enter the number: '))
    rec(num)
