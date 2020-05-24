def main():
    A = float(input())
    B = float(input())
    
    MEDIA = (A*3.5/11)+(B*7.5/11)
    
    if MEDIA > 10:
        MEDIA = 10
    
    print("MEDIA = %.5f" % MEDIA)
    
if __name__ == "__main__" : main()