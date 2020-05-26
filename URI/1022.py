
def main():
    n = int(input())
    for i in range(n):
        N1, OP1, D1, OP2, N2, OP3, D2 = input().split()
        N1, D1, N2, D2 = int(N1), int(D1), int(N2), int(D2)
        a,b,c,d = operador(N1,D1,OP2,N2,D2)
        print("{}/{} = {}/{}".format(a,b,c,d))
   
    

def operador(N1,D1,OP2,N2,D2):

    if OP2 == "+":
        value1 = (N1*D2 + N2*D1)
        value2 = (D1*D2)
        value3, value4 = mdc(value1,value2)
            
    elif OP2 == "-":
        value1 = (N1*D2 - N2*D1)
        value2 = (D1*D2)
        value3, value4= mdc(value1,value2)
            
    elif OP2 == "*":
        value1 = (N1*N2)
        value2 = (D1*D2)
        value3, value4 = mdc(value1,value2)

    elif OP2 == "/":
        value1 = (N1*D2)
        value2 = (N2*D1)
        value3, value4 = mdc(value1,value2)

    else:
        pass 

    return value1,value2,value3,value4


def mdc(a, b):

    a_abs = abs(a)
    b_abs = abs(b)
    mdc = a_abs

    while a_abs % mdc != 0 or b_abs % mdc != 0: 
        mdc = mdc - 1

    return int(a/mdc),int(b/mdc)

if __name__ == "__main__": main()