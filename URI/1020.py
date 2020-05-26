def main():
    age_days = int(input())
    make_age(age_days)

def make_age(days):
    
    years = int(days/365) 
    months = int((days%365)/30)
    days = int(days-(years*365)-(months*30))

    print("%i ano(s)" % years)
    print("%i mes(es)" % months)
    print("%i dia(s)" % days)

    
if __name__ == "__main__": main()