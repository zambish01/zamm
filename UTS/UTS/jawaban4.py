print("==============")
print("Nama Provinsi")
print("==============")

listKota = [
  'Kalimantan', 'Sumatra', 'Sulawesi'
]

for kota in listKota:
  
  listTempat = [
    'West', 'North', 'South'
  ]

  while listTempat:
    print(kota, listTempat.pop(0))