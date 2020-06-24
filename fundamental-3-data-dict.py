kamus = {'anak' : 'son', 'istri' : 'wife', 'ayah' : 'father', 'ibu' : 'mother'}

print(kamus)
print(kamus['ayah'])
print(kamus['ibu'])

print('\nData ini di kirimkan dari server gojek')
data_dari_server_gojek = {
    'tanggal' : '2020-05-24',
    'driver_list' : [
        {'nama' : 'Eko', 'jarak' : 10},
        {'nama' : 'Dwi', 'jarak' : 100},
        {'nama' : 'Tri', 'jarak' : 1000},
        {'nama' : 'Catur', 'jarak' : 10000}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver di sekitar sini #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver di sekitar sini #3 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat dari anda {data_dari_server_gojek['driver_list'][0]['jarak']} meter ")
