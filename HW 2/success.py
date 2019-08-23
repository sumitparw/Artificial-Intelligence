import numpy as np
from datetime import datetime
t1 = datetime.now()
class lhsa:
    def __init__(self, id):
        self.id = id
        return


class spla:
    def __init__(self, id):
        self.id = id


class applicants:
    def __init__(self, id, gender, age, pet, mn, car, dl, days, eval):
        self.id = id
        self.gender = gender
        self.age = age
        self.pet = pet
        self.mn = mn
        self.car = car
        self.dl = dl
        self.days = days
        self.eval = eval


def rem1(arr, arra, l, a, max):
    arr1 = list(arra)
    day = []
    for lapplicants in arr:
        for applicants in arr1:
            if int(lapplicants.id) == int(applicants.id):
                day = applicants.days
                max = decrement(day, max)
                arra.remove(applicants)
            else:
                continue
    return arra, max


def fbucket(arra):
    blhsa = []
    for applicants in arra:
        if int(applicants.age) > 017 and applicants.gender == 'F' and applicants.pet == 'N':
            blhsa.append(applicants)
            #print applicants.id
        else:
            continue

    bspla = []
    for applicants in arra:
        if applicants.car == 'Y' and applicants.dl == 'Y' and applicants.mn == 'N':
            bspla.append(applicants)
        else:
            continue
    bint = []
    for applicants in arra:
        if applicants.car == 'Y' and applicants.dl == 'Y' and applicants.mn == 'N' and int(applicants.age) > 017 and applicants.gender == 'F' and applicants.pet == 'N':
            bint.append(applicants)
        else:
            continue
    return bspla, blhsa, bint


def conversion(arr):
    days = []
    days = list(arr)
    days = map(int, days)
    return days

def decrement(days, max):
    for x in range(7):
        max[x] = max[x] - days[x]
    return max

def increment(days, max):
    for x in range(7):
        max[x] = max[x] + days[x]
    return max
def checkIfValid(applicantDays,givenDays):
    for i in range(len(applicantDays)):
        if givenDays[i]-applicantDays[i]<0:
            return False
    return True
def formula(bspla, blhsa, maxp, maxb):
    sp = len(bspla)
    lh = len(blhsa)
    if sp == 0:
        return 0, 0, 0
    funcMaxSpla=0
    funcMaxLahsa=0
    funcId=''
    isCommon_lhsa = False
    for splaApplicant in bspla:
        if(datetime.now() - t1).seconds > 170:
          break
        index1 = bspla.index(splaApplicant)
        index2 = 0
        id = splaApplicant.id
        if checkIfValid(splaApplicant.days, maxp):
            maxp = decrement(splaApplicant.days, maxp)
        else:
            continue
        bspla.remove(splaApplicant)
        if splaApplicant in blhsa:
            index2 = blhsa.index(splaApplicant)
            blhsa.remove(splaApplicant)
            isCommon_lhsa = True
        max1, max2, id = play(bspla, blhsa, True, maxb, maxp,False)
        bspla.insert(index1, splaApplicant)
        if isCommon_lhsa:
           blhsa.insert(index2, splaApplicant)
        isCommon_lhsa = False
        maxp = increment(splaApplicant.days, maxp)
        #print max1, max2
        if max1+splaApplicant.eval > funcMaxSpla:
            funcMaxSpla = max1+splaApplicant.eval
            funcMaxLahsa = max2
            funcId = splaApplicant.id
    return funcId, funcMaxSpla, funcMaxLahsa

def play(bspla, blhsa, isspla, maxb, maxp, isSkip):
    sp = len(bspla)
    lh = len(blhsa)
    if (datetime.now() - t1).seconds > 170:
        return 0,0,''
    canChoose = False
    funcMaxSpla = 0
    funcMaxLahsa = 0
    funcId=''

    if isspla:
        isCommon_spla = False
        for lhsaApplicants in blhsa:
            if(datetime.now() - t1).seconds > 170:
              break
            index1 = blhsa.index(lhsaApplicants)
            index2 = 0
            if checkIfValid(lhsaApplicants.days, maxb):
                maxb = decrement(lhsaApplicants.days, maxb)
            else:
                continue
            #print "lhsa", lhsaApplicants.id
            blhsa.remove(lhsaApplicants)
            if lhsaApplicants in bspla:
                bspla.remove(lhsaApplicants)
                isCommon_spla = True
            canChoose = True
            max1, max2, id = play(bspla, blhsa, False, maxb, maxp, False)
            blhsa.insert(index1, lhsaApplicants)
            if isCommon_spla:
                bspla.insert(index2, lhsaApplicants)
            isCommon_spla = False
            maxb = increment(lhsaApplicants.days, maxb)
            if funcMaxLahsa < max2+lhsaApplicants.eval:
                funcMaxLahsa = max2+lhsaApplicants.eval
                funcMaxSpla = max1
                funcId = lhsaApplicants.id
        if not canChoose and not isSkip:
            m1,m2,id= play(bspla, blhsa, False, maxb, maxp, True)
            #print m1,m2,id
            return m1,m2,id
        if isSkip and not canChoose:
            return 0, 0, ''
        return funcMaxSpla, funcMaxLahsa, funcId

    else:
        isCommon_lhsa = False
        for splaApplicant in bspla:
            if (datetime.now() - t1).seconds > 170:
               break
            index1 = bspla.index(splaApplicant)
            index2 = 0
            if checkIfValid(splaApplicant.days, maxp):
                maxp = decrement(splaApplicant.days, maxp)
            else:
                continue
            #print "spla", splaApplicant.id
            bspla.remove(splaApplicant)
            canChoose=True
            if splaApplicant in blhsa:
                blhsa.remove(splaApplicant)
                isCommon_lhsa = True
            max1, max2, id = play(bspla, blhsa, True, maxb, maxp,False)
            bspla.insert(index1, splaApplicant)
            if isCommon_lhsa:
                blhsa.insert(index2, splaApplicant)
            isCommon_lhsa = False
            maxp = increment(splaApplicant.days, maxp)
            if max1+splaApplicant.eval > funcMaxSpla:
                funcMaxSpla = max1+splaApplicant.eval
                funcMaxLahsa = max2
                funcId = splaApplicant.id
        if not canChoose and not isSkip:
            m1,m2,id= play(bspla, blhsa, True, maxb, maxp, True)
            #print m1, m2, id
            return m1, m2, id
        if not canChoose and isSkip:
            return 0, 0, ''
        return funcMaxSpla, funcMaxLahsa, funcId

def opt(bint, maxp, maxb):
    sp = len(bint)
    if sp == 0:
        return 0,0,0
    funcMaxSpla=0
    funcMaxLahsa=0
    funcId=''
    for splaApplicant in bint:
        if (datetime.now() - t1).seconds > 170:
            break
        index1 = bint.index(splaApplicant)
        index2 = 0
        id = splaApplicant.id
        if checkIfValid(splaApplicant.days, maxp):
            maxp = decrement(splaApplicant.days, maxp)
        else:
            continue
        #print "formula"
        #print splaApplicant.id
        bint.remove(splaApplicant)
        max1, max2, id = player(bint, True, maxb, maxp,False)
        bspla.insert(index1, splaApplicant)
        maxp = increment(splaApplicant.days, maxp)
        #print max1, max2
        if max1+splaApplicant.eval > funcMaxSpla:
            funcMaxSpla = max1+splaApplicant.eval
            funcMaxLahsa = max2
            funcId = splaApplicant.id
        #end_time = time.clock()
        #diff = end_time - start_time
        #print "formula diff =", diff
        #if diff > 150:
            #funcId= 0
            #return funcId
    return funcId, funcMaxSpla, funcMaxLahsa

def player(bint, isspla, maxb, maxp, isSkip):
    if (datetime.now() - t1).seconds > 170:
        return 0,0,''
    sp = len(bint)
    canChoose = False
    funcMaxSpla = 0
    funcMaxLahsa = 0
    funcId=''

    if isspla:
        isCommon_spla = False
        for lhsaApplicants in bint:
            if (datetime.now() - t1).seconds > 170:
                break
            index1 = bint.index(lhsaApplicants)
            index2 = 0
            if checkIfValid(lhsaApplicants.days, maxb):
                maxb = decrement(lhsaApplicants.days, maxb)
            else:
                continue
            #print "lhsa", lhsaApplicants.id
            bint.remove(lhsaApplicants)
            canChoose = True
            max1, max2, id = player(bint, False, maxb, maxp, False)
            bint.insert(index1, lhsaApplicants)
            maxb = increment(lhsaApplicants.days, maxb)
            if funcMaxLahsa < max2+lhsaApplicants.eval:
                funcMaxLahsa = max2+lhsaApplicants.eval
                funcMaxSpla = max1
                funcId = lhsaApplicants.id
        if not canChoose and not isSkip:
            m1,m2,id= player(bint, False, maxb, maxp, True)
            #print m1,m2,id
            return m1,m2,id
        if isSkip and not canChoose:
            return 0, 0, ''
        return funcMaxSpla, funcMaxLahsa, funcId

    else:
        isCommon_lhsa = False
        for splaApplicant in bint:
            if (datetime.now() - t1).seconds > 170:
                break
            index1 = bint.index(splaApplicant)
            index2 = 0
            if checkIfValid(splaApplicant.days, maxp):
                maxp = decrement(splaApplicant.days, maxp)
            else:
                continue
            #print "spla", splaApplicant.id
            bint.remove(splaApplicant)
            canChoose=True
            max1, max2, id = player(bint, True, maxb, maxp,False)
            bint.insert(index1, splaApplicant)
            maxp = increment(splaApplicant.days, maxp)
            if max1+splaApplicant.eval > funcMaxSpla:
                funcMaxSpla = max1+splaApplicant.eval
                funcMaxLahsa = max2
                funcId = splaApplicant.id
        if not canChoose and not isSkip:
            m1,m2,id= player(bint, True, maxb, maxp, True)
            #print m1, m2, id
            return m1, m2, id
        if not canChoose and isSkip:
            return 0, 0, ''
        return funcMaxSpla, funcMaxLahsa, funcId

def opt1(bspla, maxp):
    siz = len(bspla)
    if siz == 0:
        return 0,0,0
    funcMaxSpla=0
    funcMaxLahsa=0
    funcId=''
    for splaApplicant in bspla:
        if (datetime.now() - t1).seconds > 170:
            break
        index1 = bspla.index(splaApplicant)
        index2 = 0
        id = splaApplicant.id
        if checkIfValid(splaApplicant.days, maxp):
            maxp = decrement(splaApplicant.days, maxp)
        else:
            continue
        bspla.remove(splaApplicant)
        max1, id = player1(bspla, maxp, False)
        bspla.insert(index1, splaApplicant)
        maxp = increment(splaApplicant.days, maxp)
        #print max1, max2
        if max1+splaApplicant.eval > funcMaxSpla:
            funcMaxSpla = max1+splaApplicant.eval
            funcId = splaApplicant.id
    return funcMaxSpla,funcId

def player1(bspla, maxp, isSkip):
    if (datetime.now() - t1).seconds > 170:
        return 0,''
    siz = len(bspla)
    canChoose = False
    funcMaxSpla = 0
    funcId=''
    for splaApplicant in bspla:
        if (datetime.now() - t1).seconds > 170:
            break
        index1 = bspla.index(splaApplicant)
        index2 = 0
        if checkIfValid(splaApplicant.days, maxp):
            maxp = decrement(splaApplicant.days, maxp)
        else:
            continue
        #print "spla", splaApplicant.id
        bspla.remove(splaApplicant)
        canChoose=True
        max1, id = player1(bspla, maxp, False)
        bspla.insert(index1, splaApplicant)
        maxp = increment(splaApplicant.days, maxp)
        if max1+splaApplicant.eval > funcMaxSpla:
            funcMaxSpla = max1+splaApplicant.eval
            funcId = splaApplicant.id
    if not canChoose and not isSkip:
        m1, id = player1(bspla,maxp, True)
        #print m1, m2, id
        return m1, id
    if not canChoose and isSkip:
        return 0,''
    return funcMaxSpla, funcId

f = open("input.txt", "r")
b = int(f.readline())
p = int(f.readline())
l = f.readline()
l = int(l)
arrl = []
for x in range(l):
    l1 = lhsa(f.readline())
    arrl.append(l1)

s = f.readline()
s = int(s)
# print s
arrs = []
for x in range(s):
    s1 = spla(f.readline())
    arrs.append(s1)

a = f.readline()
a = int(a)
# print a
arra = []
for x in range(a):
    str = f.readline()
    id = str[0:5]
    # print id
    gender = str[5:6]
    # print gender
    age = str[6:9]
    # print age
    pet = str[9:10]
    # print pet
    mn = str[10:11]
    # print mn
    car = str[11:12]
    # print car
    dl = str[12:13]
    # print dl
    days = str[13:20]
    days = conversion(days)
    eval = sum(days)
    arra.append(applicants(id, gender, age, pet, mn, car, dl, days, eval))
    # print arra[x].gender
    str = ''

count = 0
for applicants in arra:
    if int(applicants.age) <= 17 and applicants.gender != 'F' and applicants.pet == 'Y' and applicants.car == 'N' and applicants.dl == 'N' and applicants.mn == 'Y':
        arra.remove(applicants)

arra = sorted(arra, key=lambda evaluate: evaluate.eval, reverse=True)
#print arra[0].id

maxp = [p, p, p, p, p, p, p]
maxb = [b, b, b, b, b, b, b]

arra, maxb = rem1(arrl, arra, l, a, maxb)
arra, maxp = rem1(arrs, arra, s, a, maxp)
#print arra[3].id
# print arra[2].id
# print maxb, maxp

bspla, blhsa, bint = fbucket(arra)
#print bint[0].id
if len(bint) == 0:
    funcMaxSpla, funcId = opt1(bspla, maxp)
    f1 = open("output.txt","w")
    f1.write(funcId)
else:
    funcid, funcmaxspla, funcmaxlahsa = opt(bint, maxp, maxb)
    funcid1, funcmaxspla1, funcmaxlahsa1 = formula(bspla, blhsa, maxp, maxb)
    if funcmaxspla > funcmaxspla1:
       f1 = open("output.txt", "w")
       f1.write(funcid)
    elif funcmaxspla == funcmaxspla1:
        if int(funcid)> int(funcid1):
            f1 = open("output.txt", "w")
            f1.write(funcid1)
        elif int(funcid)<= int(funcid1):
            f1 = open("output.txt", "w")
            f1.write(funcid)
    else:
        f1 = open("output.txt", "w")
        f1.write(funcid1)
print (datetime.now() - t1).seconds
f.close()
f1.close()
