
doc=open("daftar.txt","r")
se = input("Masukkan nama barang yang ingin dicari : ")
skincare=doc.readlines()
c= 1
kuantitas=""
ket=""
harga=""
for i in skincare:
    kata=i
    k,n,ke,ha = kata.split(",",4)
    if se == n:
        c=1
        kuantitas = k
        ket = ke
        harga =ha
        flag=False
        break

    else:
        c=0
        continue

            
if c== 1:
    print("Barang ditemukan dengan kuantitas "+kuantitas+"\nKet :"+ ket+"\nharga :"+harga)
else:
    print("Barang tidak ditemukan silahkan mencari lagi ")
            
