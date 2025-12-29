#timer
def clock():
    t_sec = int(input("Enter time in seconds: "))
    hours = t_sec//3600
    minutes = (t_sec%3600)//60
    seconds = t_sec%60
    print(f"{hours}Hr:{minutes}Min:{seconds}Sec")
clock()
