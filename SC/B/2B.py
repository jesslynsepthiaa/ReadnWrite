t = int(input("Masukkan tinggi diamond:"))

doc = open("diamond.txt", "w")

for i in range(1, t+1):
  i = i - (t//2 +1)
  if i < 0:
    i = -i
  doc.write(" " * i + "*" * (t - i*2) + " "*i + "\n")

doc.close()
