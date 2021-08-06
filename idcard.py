def idcheck(change):
    if {change} == 0:
        {change} = "1"
    elif {change} == 1:
        {change} = "0"
    elif {change} == 2:
        {change} = "X"
    elif {change} == 3:
        {change} = "9"
    elif {change} == 4:
        {change} = "8"
    elif {change} == 5:
        {change} = "7"
    elif {change} == 7:
        {change} = "5"
    elif {change} == 8:
        {change} = "4"
    elif {change} == 9:
        {change} = "3"
    elif {change} == 10:
        {change} = "2"


idnumber = input("输入身份证号码\n")
tim = str(len(idnumber))
if tim == "18":
    soloim = list(map(str,idnumber))
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r = soloim
    ax = int(a) * 7
    bx = int(b) * 9
    cx = int(c) * 10
    dx = int(d) * 5
    ex = int(e) * 8
    fx = int(f) * 4
    gx = int(g) * 2
    hx = int(h)
    ix = int(i) * 6
    jx = int(j) * 3
    kx = int(k) * 7
    lx = int(l) * 9
    mx = int(m) * 10
    nx = int(n) * 5
    ox = int(o) * 8
    px = int(p) * 4
    qx = int(q) * 2
    plusid = ax + bx + cx + dx + ex + fx + gx + hx + ix + jx + kx + lx + mx + nx + ox + px + qx
    tofid = plusid % 11
    checkstr = idcheck(tofid)
    if checkstr == str(r):
        print("身份证号是正确的！")
    else:
        print("身份证号错误！")
else:
    print("您的身份证号码位数有误，请核对后再输入")
