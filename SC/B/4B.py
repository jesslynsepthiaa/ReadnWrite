
doc=open("daftarbuku.txt","r")
se = input("Masukkan nama buku yang ingin dicari : ")
bk=doc.readlines()
c= 1
nama=""
kode=""
thn=""
des=""
for i in bk:
    kata=i
    n,k,t,d = kata.split(",",4)
    if se == n:
        c=1
        nama = n
        kode = k
        thn =t
        des=d
        flag=False
        break

    else:
        c=0
        continue

            
if c == 1:
    print("BUKU ditemukan\nNama: "+nama+"\nKode :"+ kode+"\nTahun Rilis :"+thn+
          "\nDescripsi "+des)
else:
    print("Barang tidak ditemukan silahkan mencari lagi ")
            
