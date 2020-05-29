#[0,25], (25,50], (50,75], (75,100])

def main():
    valor = float(input())

    if valor < 0 or valor > 100:
        print("Fora de intervalo")
    elif valor >= 0 and valor <= 25:      
        print("Intervalo [0,25]")
    elif valor > 25 and valor <= 50:     
        print("Intervalo (25,50]")
    elif valor > 50 and valor <= 75:     
        print("Intervalo (50,75]")
    elif valor > 75 and valor <= 100:     
        print("Intervalo (75,100]") 
    else:
        pass

if __name__ == "__main__": main()