
def main():
    n = int(input())
    i = 1

    while i <= n:
        if n % i == 0:
            print(i)
            i += 1
        else:
            i += 1


if __name__ == "__main__": main()