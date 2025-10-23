print("GEROBAK FRIED CHICKEN")
print("--------------------------")
print("D    Dada    Rp.2500")
print("P    Paha    Rp.2000")
print("S    Sayap   Rp.1500")
print("--------------------------")

list_bjenis = []
list_harga = []
list_beli =[]
list_jumlah = []

total1 = 0

bjenis = int(input("Banyak Jenis : "))
for i in range(bjenis):
    print(f"Jenis Ke-{i+1}")
    kode = input("Kode Potong [D/P/S] : ").upper()
    beli = int(input("Banyak Potong : "))
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
        
    jumlah = harga*beli
    total1 += jumlah

    list_bjenis.append(jenis)
    list_harga.append(harga)
    list_beli.append(beli)
    list_jumlah.append(jumlah)

print("\nGEROBAK FRIED CHICKEN")
print("---------------------------------------------------------")
print("No. Jenis Potong  Harga Satuan  Banyak Beli  Jumlah")
print("---------------------------------------------------------")
for i in range(len(list_bjenis)):
    if list_bjenis[i] == "Dada" or list_bjenis[i] == "Paha" :
        print(f"{i+1}       {list_bjenis[i]}         Rp.{list_harga[i]}         {list_beli[i]}       Rp.{list_jumlah[i]}")
    elif list_bjenis[i] == "Sayap" :
        print(f"{i+1}       {list_bjenis[i]}        Rp.{list_harga[i]}         {list_beli[i]}       Rp.{list_jumlah[i]}")
    print("---------------------------------------------------------")

pajak = total1*0.10
total2 = total1+pajak

print(f"                                Jumlah Bayar Rp.{int(total1)}")
print(f"                                Pajak 10%    Rp.{int(pajak)}")
print(f"                                Total Bayar  Rp.{int(total2)}")