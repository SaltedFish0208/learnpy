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
    tofidstr = "null"
    if tofid == 0:
        tofidstr = "1"
    elif tofid == 1:
        tofidstr = "0"
    elif tofid == 2:
        tofidstr = "X"
    elif tofid == 3:
        tofidstr = "9"
    elif tofid == 4:
        tofidstr = "8"
    elif tofid == 5:
        tofidstr = "7"
    elif tofid == 7:
        tofidstr = "5"
    elif tofid == 8:
        tofidstr = "4"
    elif tofid == 9:
        tofidstr = "3"
    elif tofid == 10:
        tofidstr = "2"
    if tofidstr == str(r):
        print("身份证号是正确的！")
    else:
        print("身份证号错误！")
else:
    print("您的身份证号码位数有误，请核对后再输入")
