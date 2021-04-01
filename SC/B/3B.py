print("=========TUGAS!==============")
flag = True


while (flag):
    print("1. Tambah Data ")
    print("2. Lihat Data ")
    print("3. Exit")
    ip = int(input("Masukkan nomor menu yang diinginkan : "))
    
    if ip ==1 :
        doc=open('tugas.txt','a')
        print("====MENU TAMBAH DATA====")
        tel = int(input("Masukkan jumlah alamat telepon : "))
        for i in range(tel):
            m = input("Masukkan Nama  : ")
            n = input("Masukkan nomor telepon : ")
            doc.write(m+","+n)
            doc.write("\n") 
        print("Berhasil dimasukkan\n")
        doc.close()
        
    elif ip ==2 :
        print("====Lihat Data====")
        wr=open('tugas.txt','r')
        liste = wr.readlines()
        for i in liste:
            kata = i
            name,no = kata.split(",",2)
            print("Nama\t \t nomor telp")
            print(name+"\t \t"+no)
        wr.close()
    elif ip ==3 :
        print("Berhasil Logout")
        flag =False
    else:
        print("Invalid Input")

    
    
