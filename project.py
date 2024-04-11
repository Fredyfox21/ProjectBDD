from pyeda.inter import *



def RR(i, j):
    f=expr(Or(((i + 3) % 32 == j % 32),((i + 8) % 32 == j % 32)))

    if(f):
        return True
    else:
        return False

def Even(j):

    if(j[4]==0):
        return True
    
    return False

def Prime(node2):
    array=[3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    for i in array:
        y=int2exprs(i,6)
        if(node2==y):
            return True

    return False

def RR2(num1,num2):

    for i in range(32):

        rr2=RR(num1,i)+RR(i,num2)
        if(rr2):
            return True
        
    return False

#========================================
# New Code but wont have enough time
#========================================
X=exprvars('x',5)
Y=exprvars('y',5)




r= expr(Or(And(~X[0],~X[1],~X[2],~X[3],~X[4],Y[0],Y[1],~Y[2],~Y[3],~Y[4]), And(X[0],~X[1],~X[2],~X[3],~X[4],~Y[0],~Y[1],Y[2],~Y[3],~Y[4])))

print(int2exprs(27,6))




#========================================

num =int(input("Input 1st node for RR: "))
num2=int(input("Input 2st node for RR: "))
if(RR(num,num2)):
    print("RR(",num,",",num2,") is True")
else:
    print("RR(",num,",",num2,") is False")

if(Even(int2exprs(num2,5))):
    print("EVEN(",num2,") is True")
else:
    print("EVEN(",num2,") is False")

if(Prime(int2exprs(num,6))):
    print("Prime(",num,") is True")
else:
    print("Prime(",num,") is False")

if(RR2(num,num2)):
    print("RR2(",num,",",num2,") is True")
else:
    print("RR2(",num,",",num2,") is False")


