gaji_pokok = int(input("Masukan Gaji : "))
jam = int(input("Masukan Jam Kerja Anda : "))

if jam > 200 :
    lembur = (jam-200)*20000
else :
    lembur = 0

print (lembur)