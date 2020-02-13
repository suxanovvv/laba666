days = range (1, 32)
mounths = range (1, 13)
years = range (1901, 2020)
while True:
    while True:
        try:
            d, m, y = int(input('Day: ')), \
                      int(input('month:')), \
                      int(input('year:'))
            break
        except ValueError:
            print('Enter correct number')
    if d in days and m in mounths and y in years:
      if y%4==0:
        while 1<m<12:
           m= int(input("input m!:"))
        if m == 2:
         index = 1
        elif m == 4 or m == 6 or m == 9 or m == 11:
         index = 2
        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
         index = 3
    
        while d < 1 or (d > 29 and index == 1) or (d > 30 and index == 2) or (d > 31 and index == 3):
         d = int(input("input d!:"))

        if (d == 29 and index == 1) or (d == 30 and index == 2) or (d == 31 and index == 3):
         nekst = 1
        else:
         t =d+1
        if (d==1 and index==1) or (d==1 and index==2):
         previous=31
        elif (m==3 and d==1):
         previous=29
        elif (m==5 and d==1) or (m==7 and d==1) or (m==10 and d==1) or (m==12 and d==1):
         previous==30
        else:
         previous=d-1
        
        print(nekst, ".", previous)
 
      else:
         while m < 1 or m > 12:
            m= int(input("input m!:"))
         if m == 2:
          index = 1
         elif m == 4 or m == 6 or m == 9 or m == 11:
           index = 2
         elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
           index = 3
    
         while d < 1 or (d > 28 and index == 1) or (d > 30 and index == 2) or (d > 31 and index == 3):
           d = int(input("input d!:"))

         if (d == 28 and index == 1) or (d == 30 and index == 2) or (d == 31 and index == 3):
          nekst = 1
         else:
          nekst =d+1
         if (d==1 and index==1) or (d==1 and index==2):
          previous=31
         elif (m==3 and d==1):
          previous=28
         elif (m==5 and d==1) or (m==7 and d==1) or (m==10 and d==1) or (m==12 and d==1):
          previous==30
         else:
          previous=d-1
        
         print(nekst, ".", previous)
    result = input('Хочете запустити заново? Якщо так - 1, ні - інше: ')
    if result == '1':
        continue
    else:
        break

