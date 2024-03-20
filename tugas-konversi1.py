bilangan=int(input("masukan bilangan yang ingin dikonversi :\t"))

konversi1=bin(bilangan)[2:]
print("Bilangan Biner \t\t: ", konversi1.zfill(8))