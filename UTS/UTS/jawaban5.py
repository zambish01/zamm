pilihan="y"
while pilihan=="y":        
    print("""
        ==============================
        1. Cappucino : Rp 5.000
        2. Teh       : Rp 3.000
        Exit
        ==============================
        """)

    pesan=str(input("Pilih Menu :"))
    jumlahpesan=int(input("Masukan Jumlah Pesan :"))
    if pesan == "1":
        listnama= "Cappucino"
        harga=(5000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "2":
        listnama= "Teh"
        harga = (3000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
    
    Nama = str(input("Masukan Nama :" ))
    NIM  = str(input("Masukan NIM  :" ))
    print("--------------------------")
    print("NiM  : " + NIM)
    print("Nama : " + Nama)
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")