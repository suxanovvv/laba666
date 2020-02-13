from enum import Enum 
 
class month(Enum): 
    January = 1 
    February = 2 
    March = 3 
    April = 4 
    May = 5 
    June = 6 
    July = 7 
    August = 8 
    September = 9 
    October = 10 
    November = 11 
    December = 12 
 
 
class season(Enum): 
    Winter = 1 
    Spring = 2 
    Summer = 3 
    Autumn = 4 
 
while True: 
    while True: 
        try: 
            s = int(input("month: ")) 
            break 
        except ValueError: 
            print('Введіть число!') 
    if s in range(1, 3) or s == 12: 
        print('Winter') 
    elif s in range(3, 6): 
        print("Spring") 
    elif s in range(6, 8): 
        print('Summer') 
    elif s in range(9, 12): 
        print('Autumn')
    else:
        print('Error')
 
    yeah = input("Для повторення операції введіть що-небудь, нічого - завершення операції") 
    if len(yeah) >= 1: 
        continue 
    break
