doc = open('encrypt.txt','r')

baca= doc.readlines()
strings = [str(integer) for integer in baca]
a_string = "".join(strings)
nu = int(a_string)
ang,i,n=0,0,0
while(nu !=0):
    dec= nu %10
    ang = ang+dec*pow(2,i)
    nu = nu//10
    i+=1
print("Passcodenya adalah "+str(ang))
    
