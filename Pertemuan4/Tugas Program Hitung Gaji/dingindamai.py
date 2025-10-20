print("PROGRAM HITUNG GAJI KARYAWAN")
nama = input("  Masukkan Nama Karyawan             : ").capitalize()
golongan = input("  Masukkan Golongan Jabatan (1/2/3)  : ")
pendidikan = input("  Masukkan Pendidikan (SMA/D1/D3/S1) : ").upper()
jk = int(input("  Masukkan Jumlah Jam Kerja          : "))
gaji = 300000

if golongan == "1" :
    tj = 0.05*gaji
elif golongan == "2" :
    tj = 0.10*gaji
elif golongan == "3" :
    tj = 0.15*gaji
else :
    tj = 0

if pendidikan == "SMA" :
    tp = 0.025*gaji
elif pendidikan == "D1" :
    tp = 0.05*gaji
elif pendidikan == "D3" :
    tp = 0.2*gaji
elif pendidikan == "S1" :
    tp = 0.3*gaji
else :
    tp = 0

if jk > 8 :
    lembur = (jk-8)*3500
else :
    lembur = 0
    
total = lembur+tp+tj+gaji

print("==========================================")
print(f"Karyawan Yang Bernama {(nama)}")
print(f"Gaji Yang Diterima")
print(f"    Gaji Pokok           Rp{int(gaji)}")
print(f"    Tunjangan Jabatan    Rp{int(tj)}")
print(f"    Tunjangan Pendidikan Rp{int(tp)}")
print(f"    Honor Lembur         Rp{int(lembur)}")
print(f"                         ________________+")
print(f"Total Gaji               Rp{int(total)}")