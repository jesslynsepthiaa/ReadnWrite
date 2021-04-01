angka = int(input("Masukkan angka hoki Rocky: "))

cur=1

f = open("angka.txt", "w")
for num in range(2, angka+1):
    prime = True
    for i in range(2,num):
        if (num%i == 0):
            prime= False
    if prime:
        f.write(str(num)+" ekor")
        f.write("\t")

f.close()       
