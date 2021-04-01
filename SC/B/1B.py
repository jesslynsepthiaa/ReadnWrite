doc = open("passTina.txt","w")

passw = input("Masukkan password yang akan digenerate : ")
hasl = int(passw,16)
doc.write(str(hasl))



doc.close()
