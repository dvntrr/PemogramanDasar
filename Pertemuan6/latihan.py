list_nim = []
list_uts = []
list_uas = []
list_total = []

ulang = int(input("Masukkan Banyak Data : "))
for i in range(ulang) :
    print(f"Data Ke-{i+1}")
    list_nim.append(input("Masukkan Nim Anda : "))
    list_uts.append(int(input("Masukkan Nilai UTS Anda : ")))
    list_uas.append(int(input("Masukkan Nilai UAS Anda : ")))

for i in range(ulang) :
    list_total.append((list_uas[i] + list_uts[i]) / 2)

print("=============================================================")
print("  Nim        Nilai Uts        Nilai UAS                 Total")
print("=============================================================")
for i in range(ulang):
    print("%s \t %i \t\t %i \t\t\t %i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))
    print("=============================================================")