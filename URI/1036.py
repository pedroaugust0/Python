def main():
    x = input().split()
    a, b, c, = x
    a = float(a)
    b = float(b)
    c = float(c)

    bhaskara(a,b,c)

def bhaskara(a,b,c):
    
    delta = (b*b) - (4*a*c)
    raiz_delta = delta ** (1/2)

    if a < 1 or delta < 0:
        return print("Impossivel calcular")
    else:
        raiz_1 = (-b + raiz_delta)/(2*a)
        raiz_2 = (-b - raiz_delta)/(2*a)
        print("R1 = %.5f" % raiz_1)
        print("R2 = %.5f" % raiz_2)
        
if __name__ == "__main__": main()