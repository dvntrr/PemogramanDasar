print("GEROBAK FRIED CHICKEN")
print("--------------------------")
print("D    Dada    Rp.2500")
print("P    Paha    Rp.2000")
print("S    Sayap   Rp.1500")
print("--------------------------")

bjenis = int(input("Banyak Jenis : "))
for i in range(bjenis):
    print(f"Jenis Ke-{i+1}")
    kode = input("Kode Potong [D/P/S] : ").upper()
    bpotong = int(input("Banyak Potong : "))
    if kode == "D" :
        harga = 2500
        jenis = "Dada"
    elif kode == "P" :
        harga = 2000
        jenis = "Paha"
    elif kode == "S" :
        harga = 1500
        jenis = "Sayap"
    else :
        print("Kode Tidak Valid")
        continue
        
    jumlah = harga*bpotong
    total1 += jumlah
print("\nGEROBAK FRIED CHICKEN")
print("---------------------------------------------------------")
for i2 in range(i):
    print(f"{i2+1:<4} {jenis:<7} Rp.{harga:<7} {bpotong:<6} Rp.{jumlah}")
    print("---------------------------------------------------------")

pajak = jumlah*0.10
total2 = jumlah+pajak

print(f"                                  Jumlah Bayar Rp.{total1}")
print(f"                                  Pajak 10%    Rp.{pajak}")
print(f"                                  Total Bayar  Rp.{total2}")