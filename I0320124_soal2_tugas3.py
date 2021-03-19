# Nama, Hobi, Sosmed, Lagufav, Makananfav
dict = {'Name' : 'Ananda wahyu Nur Said',
        'hobby' : ['riding','volly', 'mendaki gunung', 'main game'],
        'sosialmedia' : {'IG' : 'nnd_wahyu', 'twitter' : 'nanda wahyu', 'facebook' : 'nanda wahyu'},
        'klubbolafavorit' : ['Persib', 'Manchester United', 'Real Madrid'],
        'gamekesukaan' : ['PUBG mobile', 'mobile legend', 'PES']}

# Mengubah salah satu hobi dan sosmed
dict['hobby'][0] = 'berenang'
dict['sosialmedia']['twitter'] = 'nanda wahyu'

# Menghapus 2 klub bola favorit
del dict['klubbolafavorit'][0]
del dict['klubbolafavorit'][1]

# Menambahkan 1 hobi
dict['hobby'].append('futsal')
print (*dict['hobby'], sep= ", ")