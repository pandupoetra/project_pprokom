# data_kalori digunakan untuk menyimpan nilai kalori dari amsing-masing makanan 
data_kalori = {
    "Nasi Putih": 100,
    "Ayam Goreng": 340,
    "Sayur asam": 230,
    "Mangga": 140,
    "Es Teh": 140
}

#menyimpan nilai semua kalori pada makanan yang diplih
total_kalori = 0
i = 0
#menyimpan menu makanan yang kita pilih
pilihan_menu=[]

while i <= 5:
    print("\nMenu kategori makanan:")
    print("1. Makanan Pokok")
    print("2. Lauk")
    print("3. Sayur")
    print("4. Buah")
    print("5. Minuman")
    print("6. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5/6): ")

    if pilihan == '6':
        break
    if pilihan == '1':
        print("\n---Daftar Pilihan Makanan Pokok---")
        menu_mapok = {
            1: "Nasi Putih",
            2: "Ubi Rebus",
            3: "Singkong Rebus",
            4: "Ketan Putih",
            5: "Jagung Rebus",
            6: "keluar"
        }
        for kunci, nilai in menu_mapok.items():
            print(f"{kunci}. {nilai}")
        mapok_pilihan = int(input("Pilih menu (1/2/3/4/5): "))
        if mapok_pilihan in menu_mapok:
            pilihan_menu.append(menu_mapok[mapok_pilihan])
            total_kalori += data_kalori.get(menu_mapok[mapok_pilihan], 0)
            print(f"{menu_mapok[mapok_pilihan]} telah ditambahkan ke pilihan Anda.")
        else:
            print("Pilihan tidak valid. Silakan pilih nomor yang tersedia.")
    if pilihan == '2':
        print("\n---Daftar Pilihan Lauk Makan---")
        menu_lauk = {
            1: "Ayam Goreng",
            2: "Tahu Bacem",
            3: "Tempe Bacem",
            4: "Telur Mata Sapi",
            5: "Dendeng Balado",
            6: "keluar"
        }
        for kunci, nilai in menu_lauk.items():
            print(f"{kunci}. {nilai}")
        lauk_pilihan = int(input("Pilih menu (1/2/3/4/5): "))
        if lauk_pilihan in menu_lauk:
            pilihan_menu.append(menu_lauk[lauk_pilihan])
            total_kalori += data_kalori.get(menu_lauk[lauk_pilihan], 0)
            print(f"{menu_lauk[lauk_pilihan]} telah ditambahkan ke pilihan Anda.")
        else:
            print("Pilihan tidak valid. Silakan pilih nomor yang tersedia.")
    if pilihan == '3':
        print("\n---Daftar Pilihan sayur---")
        menu_sayur = {
            1: "Sayur asam",
            2: "Sop bayam",
            3: "Sayur lodeh",
            4: "Cah jagung putren",
            5: "Cah labu siam",
            6: "keluar"
        }
        for kunci, nilai in menu_sayur.items():
            print(f"{kunci}. {nilai}")
        sayur_pilihan = int(input("Pilih menu (1/2/3/4/5): "))
        if sayur_pilihan in menu_sayur:
            pilihan_menu.append(menu_sayur[sayur_pilihan])
            total_kalori += data_kalori.get(menu_sayur[sayur_pilihan], 0)
            print(f"{menu_sayur[sayur_pilihan]} telah ditambahkan ke pilihan Anda.")
        else:
            print("Pilihan tidak valid. Silakan pilih nomor yang tersedia.")
    if pilihan == '4':
        print("\n---Daftar Pilihan buah---")
        menu_buah = {
            1: "Mangga",
            2: "Pisang",
            3: "Apel",
            4: "Jeruk",
            5: "Anggur",
            6: "keluar"
        }
        for kunci, nilai in menu_buah.items():
            print(f"{kunci}. {nilai}")
        buah_pilihan = int(input("Pilih menu (1/2/3/4/5): "))
        if buah_pilihan in menu_buah:
            pilihan_menu.append(menu_buah[buah_pilihan])
            total_kalori += data_kalori.get(menu_buah[buah_pilihan], 0)
            print(f"{menu_buah[buah_pilihan]} telah ditambahkan ke pilihan Anda.")
        else:
            print("Pilihan tidak valid. Silakan pilih nomor yang tersedia.")
    if pilihan == '5':
        print("\n---Daftar Pilihan Minuman---")
        menu_minuman = {
            1: "Es Teh",
            2: "Es cendol",
            3: "Es kelapa muda",
            4: "Jus melon",
            5: "Air Putih",
            6: "keluar"
        }
        for kunci, nilai in menu_minuman.items():
            print(f"{kunci}. {nilai}")
        minuman_pilihan = int(input("Pilih menu (1/2/3/4/5): "))
        if minuman_pilihan in menu_minuman:
            pilihan_menu.append(menu_minuman[minuman_pilihan])
            total_kalori += data_kalori.get(menu_minuman[minuman_pilihan], 0)
            print(f"{menu_minuman[minuman_pilihan]} telah ditambahkan ke pilihan Anda.")
        else:
            print("Pilihan tidak valid. Silakan pilih nomor yang tersedia.")
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
    i += 1

print("\nPilihan Menu Anda:")
for menu in pilihan_menu:
    kalori = data_kalori.get(menu, "Tidak diketahui")  # Mengambil kalori dari dictionary
    print(f"{menu} = {kalori} kalori")

print(f"Total kalori dari semua makanan tadi adalah = {total_kalori}")
