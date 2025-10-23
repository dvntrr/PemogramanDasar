ulang = int(input("Ada Berapa Orang?"))

for i in range(ulang) :
    print(f"Data Ke {i+1}")
    nim = input("Masukkan NIM Anda  : ")
    uts = int(input("Masukkan Nilai UTS : "))
    uas = int(input("Masukkan Nilai UAS : "))
    print(f"NIM anda adalah {nim}, Nilai UTS anda adalah {uts}, Nilai UAS anda adalah {uas}")