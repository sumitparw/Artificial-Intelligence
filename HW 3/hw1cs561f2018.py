import numpy as np

def maxim_grid(grid1):
    m = grd1[0]
    if m > 0:
      for y in range(0, int(n) * int(n) - 1):
          if m < grd1[y + 1]:
            #print "hi",y
            m = grd1[y + 1]
            i = y+1
          else:
            continue
      print grd1[i]
      conflicts(i, grd1)
      print grd1
      return m
    else:
      break
def conflicts(i, grd1):
    q = i / int(n)
    r = i % int(n)
    grd1[i] = -1
    c = 1
    d = 1
    e = 1
    j = 1
    for y in range(int(n) * int(n)):
        q1 = y / int(n)
        r1 = y % int(n)
        if q1 == q and r1 != r:
            grd1[y] = -2
        elif q1 != q and r1 == r:
            grd1[y] = -2
        elif q1 == q-c and r1 == r-c:
            grd1[y] = -2
            c += 1
        elif q1 == q-d and r1 == r+d:
            grd1[y] = -2
            d += 1
        elif q1 == q+e and r1 == r-e:
            grd1[y] = -2
            e += 1
        elif q1 == q+j and r1 == r+j:
            grd1[y] = -2
            j += 1

f = open("input4.txt", "r")
f1=open("output.txt", "w")
n = f.readline()
p = f.readline()
s = f.readline()

grd = np.zeros((int(n), int(n)))
grd1 = np.zeros(int(n)*int(n))
maximize = 0

for x in range(int(s)*12):
    a = f.readline()
    arr = a.split(",")
    grd[int(arr[0]), int(arr[1])] += 1
#print grd
for x in range(int(n)):
    for y in range(int(n)):
        grd1[x*int(n)+y] = grd[x, y]
#print grd1
for x in range(int(p)):
  ma = maxim_grid(grd1)
  maximize = maximize + ma
f1.write(str(int(maximize)))

f.close()
f1.close()