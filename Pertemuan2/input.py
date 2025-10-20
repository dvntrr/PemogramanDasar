#input
nama_barang=input("Masukkan Nama barang : ")
jumlah_barang=int(input("Masukkan Jumlah Barang : "))
harga_barang=int(input("Masukkan Harga barang : "))

#proses
total=harga_barang*jumlah_barang

#output
print("================================================================")
print(f"Nama Barang : {nama_barang}")
print(f"Jumlah Barang yang Dibeli : {jumlah_barang}")
print(f"Harga Barang : {harga_barang}")
print(f"Total yang Harus Dibayar : {total}")