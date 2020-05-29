
def main():
    n = int(input())
    for i in range(n):
        texto =(input())
        texto2 = list(inverte_string(texto))
        print(encripita(texto2))
   

def inverte_string(texto):
    return (texto[::-1])


def encripita(texto):
    i = len(texto)
    half = int(i/2)
    n = 0
    new_texto = texto
    for n in range(i):
        if n < half:
            if (int(ord(texto[n])) >= 65 and int(ord(texto[n])) <= 90) or (int(ord(texto[n])) >= 97 and int(ord(texto[n]) <= 122)):
                # 3 casas para direita
                new_texto[n] = chr(ord(texto[n]) + 3)
            else:
                new_texto[n] =  texto[n]
        else:
            if (int(ord(texto[n])) >= 65 and int(ord(texto[n])) <= 90) or (int(ord(texto[n])) >= 97 and int(ord(texto[n]) <= 122)):
                # 3 casas para direita
                new_texto[n] = chr(ord(texto[n]) + 2)
            else:
                new_texto[n] =  chr(ord(texto[n]) -1)
    final_texto = ("").join(new_texto)
    return final_texto


if __name__ == "__main__": main()