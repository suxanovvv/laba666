while True: 
    while True: 
        try: 
            t = int(input('Введіть хвилину: ')) 
            break 
        except ValueError: 
            print('Введіть число!') 
    if (t % 6) < 3: 
        print("ЗЕЛЕНИЙ") 
    elif (t % 6) == 3: 
        print("ЖОВТИЙ") 
    else: 
        print("ЧЕРВОНИЙ") 
 
    yeah = input("Для повторення операції введіть що-небудь, нічого - завершення операції") 
    if len(yeah) >= 1: 
        continue 
    break
