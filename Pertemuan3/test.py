gaji_pokok = 5000000
produk_terjual = int(input("Masukan Produk Yang Terjual : "))
harga = float(input("Masukan Harga Satuan Produk : "))
omset = produk_terjual*harga

if produk_terjual > 100 :
    bonus = 0.20*omset+gaji_pokok
else :
    bonus = 0.10*omset+gaji_pokok

print(f"Gaji Pokok : {gaji_pokok}")
print(f"Total Produk yang Terjual : {produk_terjual}")
print(f"Harga Satuan Produk : {int(harga)}")
print(f"Omset Penjualan : {int(omset)}")
print(f"Total gaji Setelah Bonus : {int(bonus)}")