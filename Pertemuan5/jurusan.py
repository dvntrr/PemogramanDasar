nis = input(str("Masukkan NIS anda : "))
nama = input(str("Masukkan Nama anda : "))
jurusan = input(str("Masukkan Jurusan Yang Diminati (SI/SIA) : ")).upper()

if jurusan == "SI" :
    prodi = "Sistem Informasi"
    harga = 2400000
elif jurusan == "SIA" :
    prodi = "Sistem Informasi Akuntansi"
    harga = 2800000
else :
    prodi = "Prodi Tidak Tersedia"
    harga = 0

print(f"NIS     : {nis}")
print(f"Nama    : {nama}")
print(f"Jurusan : {jurusan}-{prodi}")
print(f"Harga   : {harga}")