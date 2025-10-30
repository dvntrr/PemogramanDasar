my_list = ["hello", [1, 2, 3, 4], "Python"]
print(my_list[1][3])

#.append tambah satu data
#.extend tambah banyak data
#.remove hapus by value
#.pop hapus by index
#.clear mengosongkan list

list = [1, "Rock", 2.5]
list.append(2)
list.extend([3, 4, "Paper"])
list[0] = -1
list.remove(2.5)
list.insert(1,0)
print(list)