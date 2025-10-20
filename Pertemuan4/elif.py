kode_baju = input("Masukan Kode Baju Yang Anda Mau Beli [SP/OW] : ")
ukuran = input("Masukan Ukuran Baju Anda [S/M] : ")

if kode_baju == "SP" or kode_baju ==  "sp":
    merk = "Supreme"
    if ukuran == "S" or ukuran ==  "s":
        harga = 400000
    elif ukuran == "M" or ukuran == "m":
        harga = 450000
    elif ukuran == "L" or ukuran == "l":
        harga = 500000
elif kode_baju == "OW" or kode_baju == "ow":
    merk = "OffWhite"
    if ukuran == "S" or ukuran == "s":
        harga = 300000
    elif ukuran == "M" or ukuran == "m":
        harga = 350000
    elif ukuran == "L" or ukuran == "l" :
        harga = 400000
else :
    merk = "Merk Tidak Ada"
    harga = 0

print("Merk Baju : ",merk)
print("Harga Baju : ",harga)