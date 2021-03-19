list = ['alvin', 'memed', 'ryan', 'yeario', 'attar', 'adhi', 'rakha', 'alqodriano', 'sony', 'bagus' ]
print(list)
print("isi list indeks nomor 3,5,9: ", list[3], list[5], list[9])

#mengganti nama list indeks nomor 4,6,7
list[4], list[6], list[7] = "nadiya", "udin", "tito"
print("nama yang baru pada indeks 4,6,7", list)

#menambah 2 nama teman
list.append('hasan')
list.append('aji')
print(list)

#menampilkan nama semua teman dengan perulangan
print(list)

#menampilkan panjang nama list
print(len(list))