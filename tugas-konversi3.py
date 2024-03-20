bilangan = input("Masukkan bilangan yang ingin dikonversi (dalam bentuk biner, heksadesimal, atau oktal):\t")

desimal = None
if bilangan.startswith('0b'):
    desimal = int(bilangan, 2)  # Mengonversi dari biner ke desimal
elif bilangan.startswith('0x'):
    desimal = int(bilangan, 16)  # Mengonversi dari heksadesimal ke desimal
elif bilangan.startswith('0o'):
    desimal = int(bilangan, 8)   # Mengonversi dari oktal ke desimal
else:
    desimal = int(bilangan)      # Bilangan desimal

print("Hasil konversi ke desimal:", desimal)
