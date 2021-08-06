year = str(input("年份\n"))
ycheck = list(year)

if ycheck[2] == '0':
    judge1 = 0
else:
    judge1 = 1

if ycheck[3] == '0':
    judge2 = 0
else:
    judge2 = 1



if judge1 + judge2 >= 1 :
    remainder = int(year) % 4
    if remainder == 0:
        remainder2 = int(year) % 100
        if remainder2 != 0:
            print("是闰年")
        else:
            print("不是闰年")
else:
    remainder3 = int(year) % 400
    if remainder3 == 0:
        print("是闰年")
    else:
        print("不是闰年")