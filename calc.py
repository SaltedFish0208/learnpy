import sympy
which = input("你想计算普通的加减乘除计算还是方程？\n[1.进行普通的加减乘除运算]\n[2.解方程]\n输入序号\n")
if which == "1":
    whichin1 = input("你想进行加减乘除哪项运算\n[1.加/减]\n[2.乘]\n[3.除]\n")
    #加减运算
    if whichin1 == "1":
        plustotal = 0
        pluslist = []
        plusdatas = input("输入需要计算的数字\n每个数字用一个空格隔开\n减数用负数代替\n")
        pluslist = plusdatas.split(" ")
        print("你输入的值为" + str(pluslist))
        for one in range(0, len(pluslist)):
            plustotal = plustotal + int(pluslist[one])
        print("和为: ", plustotal)
    #乘法运算
    elif whichin1 == "2":
        timestotal = 1
        timeslist = []
        timesdatas = input("输入需要计算的数字\n每个数字用一个空格隔开\n")
        timeslist = timesdatas.split(" ")
        print("你输入的值为" + str(timeslist))
        for once in range(1, len(timeslist)):
            timestotal = timestotal * int(timeslist[once])
        print("积为: ", timestotal)
    #除法运算
    elif whichin1 == "3":
        bediv = input("输入被除数")
        div = input("输入除数")
        print("你输入的被除数是" + str(bediv) + ";" + "你输入的除数是" + str(div))
        divanswer = int(bediv) / int(div)
        print("商是" + str(divanswer))