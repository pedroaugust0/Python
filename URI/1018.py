def main():
    money = int(input())
    print(money)
    decompoem(money)

# notas 100, 50, 20, 10, 5, 2 e 1
def decompoem(x, index = 0):
    cedulas = [100, 50, 20, 10, 5, 2, 1]

    resto = x % cedulas[index]
    qtd = int( x / cedulas[index])
    
    if index == 6:
        return print(str(qtd) + " nota(s) de R$ %i,00" % cedulas[index])
    else:
        print(str(qtd) + " nota(s) de R$ %i,00" % cedulas[index])
        return decompoem(resto, index+1)

    
if __name__ == "__main__": main()