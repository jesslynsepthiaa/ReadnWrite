


print("=========SELAMAT DATANG DI SMA BELAJAR GIAT!==============")
flag = True


while (flag):
    print("1. Tambah data")
    print("2. Lihat Data Mahasiswa")
    print("3. Exit")
    ip = int(input("Masukkan nomor menu yang diinginkan : "))
    
    if ip ==1 :
        doc=open('maha.txt','a')
        print("====MENU TAMBAH DATA====")
        kls = input("Masukkan Kelas : ")
        jlhmaha = int(input("Masukkan jumlah Mahasiswa : "))
        for i in range(jlhmaha):
            m = input("Masukkan Nama Mahasiswa : ")
            n = int(input("Masukkan Nilai Mahasiswa : "))
            doc.write(kls+","+m+","+str(n))
            doc.write("\n") 
        print("Berhasil dimasukkan\n")
        doc.close()
        
    elif ip ==2 :
        print("====Lihat Data Mahasiswa====")
        wr=open('maha.txt','r')
        liste = wr.readlines()
        for i in liste:
            kata = i
            k,name,nile = kata.split(",",3)
            print("Kelas \t Nama\t \t Nilai")
            print(k+" \t"+name+"\t \t"+nile)
        wr.close()
    elif ip ==3 :
        print("Berhasil Logout")
        flag =False
    else:
        print("Invalid Input")

    
    
