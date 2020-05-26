def main():
    time = int(input())
    make_time(time)

def make_time(time):
    
    hours = int(time/3600) 
    minutes = int((time%3600)/60)
    seconds = int(time-(hours*3600)-(minutes*60))


    print("{}:{}:{}".format(hours,minutes,seconds)) 

if __name__ == "__main__": main()