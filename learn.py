#homework p57 exam 4-10
#a = ["pizza","apple","banana","pineapple","burger","hotdog"]
#for b in a[0:3]:
#    print("The first three items in the list are " + b)

idnumber = input("输入身份证号码\n")
tim = str(len(idnumber))
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
print(plusid)