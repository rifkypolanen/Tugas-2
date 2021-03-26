kontak = []
telp = []
print('Selamat datang!')
menu = True 

while menu:
    menu = int(input('--- Menu --- \n 1. Daftar Kontak \n 2. Tambah Kontak \n 3. Keluar \n Pilih menu :'))
    if menu == 1:
        for x in range(loop):
            print(kontak[x])
            print(telp[x])
    elif menu == 2:
        kontak.append(input('Nama :'))
        telp.append(input('No Telpon :'))
        print('Kontak berhasil ditambahkan!')
        loop = len(kontak)
    elif menu == 3:
        menu = False
        print('Program selesai, sampai jumpa!')
    else:
        print('Menu tidak tersedia')