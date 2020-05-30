
def main():
    n = int(input())
    i = 1
    while i != 7:
        if (n+1) % 2 != 0:
            print(n+1)
            i += 1
        n += 1

if __name__ == "__main__": main()