
def main():
    money = float(input())
    print("NOTAS:")
    coin_money = (decompoem_notas(money))
    print("MOEDAS:")
    decompoem_moedas(coin_money,0)
    
# notas 100, 50, 20, 10, 5, 2
def decompoem_notas(x, index = 0):
    cedulas = [100, 50, 20, 10, 5, 2]

    resto = x % cedulas[index]
    qtd = int( x / cedulas[index])

    if index == 5:
        print(str(qtd) + " nota(s) de R$ %.2f" % cedulas[index])
        return int(resto * 100) 
    else:
        print(str(qtd) + " nota(s) de R$ %.2f" % cedulas[index])
        return decompoem_notas(resto, index+1)

#moedas 1, 0.50, 0.25, 0.10, 0.05, 0.01
def decompoem_moedas(x, index = 0):
    cedulas_print = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    cedulas = [100, 50, 25, 10, 5, 1]
    resto = x % cedulas[index]
    
    qtd = int( x / cedulas[index])
        
    if index == 5:
        return print(str(qtd) + " moeda(s) de R$ %.2f" % cedulas_print[index])
    else:
        print(str(qtd) + " moeda(s) de R$ %.2f" % cedulas_print[index])
        return decompoem_moedas(resto, index+1)


if __name__ == "__main__": main()