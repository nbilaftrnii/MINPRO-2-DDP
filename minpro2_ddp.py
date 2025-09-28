akun = {
    "admin": {"username": "blu", "password": "111"},
    "pasien": {"username": "emp", "password": "222"}
}

data_pasien = []

def login():
    while True:
        print("------------------------------")
        print("|                            |")
        print("| SISTEM PENDAFTARAN ANTRIAN |")
        print("|      PUSKESMAS MANTAP      |")
        print("|                            |")
        print("------------------------------")
        print()
        print("            LOGIN")
        print()
        print("1. Admin")
        print("2. Pasien")
        print("------------------------------")
        try:
            menu = int(input("Masuk sebagai: "))
            if menu == 1:
                if login_admin():
                    main_menu()
                    break
            elif menu == 2:
                if login_pasien():
                    pasien()
                    break
            else:
                print("Terjadi kesalahan, silahkan ulangi kembali!")
        except ValueError:
            print("Masukkan angka yang valid!")

def login_admin():
    while True:
        username = input("Masukkan username anda: ")
        password = input("Masukkan password anda: ")
        if username == akun["admin"]["username"] and password == akun["admin"]["password"]:
            print("Login Berhasil!")
            return True
        else:
            print("Username atau Password yang anda masukkan salah!")
            return False

def main_menu():
    while True:
        print("|=========================|")
        print("|                         |")
        print("|    welcome ceo mantap   |")
        print("|                         |")
        print("|=========================|")
        print("|Menu Layanan             |")
        print("| 1. Input data           |")
        print("| 2. Lihat data           |")
        print("| 3. Ubah data            |")
        print("| 4. Hapus data           |")
        print("| 5. Metode Pembayaran    |")
        print("| 6. Keluar               |")
        print("===========================")
        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1 :
                tambah_data_pasien()
            elif pilihan == 2 :
                lihat_data_pasien()
            elif pilihan == 3 :
                ubah_data()
            elif pilihan == 4 :
                delete_data()
            elif pilihan == 5 :
                metode_pembayaran()
                cetak_struk()
                break
            elif pilihan == 6 :
                keluar = input("Apakah anda ingin keluar? (y/n) ")
                if keluar == 'y' :
                    break
            else:
                print("Menu yang anda masukkan tidak tersedia!")
        except:
            print("Tolong masukkan angka!")

def tambah_data_pasien():
    print("|=========================|")
    print("|                         |")
    print("|    Input Data Pasien    |")
    print("|                         |")
    print("|=========================|")
    pasien = {}
    pasien["NIK"] = input("NIK                              : ")
    pasien["Nama"] = input("Nama                             : ")
    pasien["Tanggal Lahir"] = input("Tanggal Lahir (DD-MM-YYYY)       : ")
    pasien["Jenis Kelamin"] = input("Jenis Kelamin                    : ")
    pasien["Umur"] = input("Umur                             : ")
    pasien["Alamat"] = input("Alamat                           : ")
    pasien["No Hp"] = input("No Hp                            : ")
    pasien["Poli"] = input("Poli                             : ")

    pilihan = input("Masukkan keluhan penyakit pasien (isi/skip) : ").strip().lower()
    if pilihan == "isi":
        pasien["Keluhan"] = input("Tulis keluhan pasien: ")
    else:
        pasien["Keluhan"] = ""

    data_pasien.append(pasien)
    no_antrian = len(data_pasien)
    print(f"Keluhan Pasien berhasil ditambahkan. Nomor antrian anda adalah : {no_antrian}")

def lihat_data_pasien():
    if not data_pasien:
        print("Data tidak ditemukan, silakan ulangi!")
        return
    print("-------Daftar Antrian Pasien-------")
    for i, pasien in enumerate(data_pasien, start=1):
        print(f"{i}. Nama: {pasien.get('Nama','-')}, Poli: {pasien.get('Poli','-')}")
    print()

def ubah_data():
    print("|=========================|")
    print("|                         |")
    print("|   Update Data Pasien    |")
    print("|                         |")
    print("|=========================|")
    if not data_pasien:
        print("Tidak ada data pasien untuk diubah.")
        return
    lihat_data_pasien()
    try:
        no_antrian = int(input("Input nomor pasien yang ingin diupdate: "))
        idx = no_antrian - 1
        if 0 <= idx < len(data_pasien):
            pasien = data_pasien[idx]
            print("Kosongkan input jika tidak ingin mengubah field tersebut.")
            for key in list(pasien.keys()):
                baru = input(f"{key} ({pasien[key]}): ")
                if baru.strip():
                    pasien[key] = baru
            print("Data pasien berhasil diubah.\n")
        else:
            print("antrian tidak dapat ditemukan")
    except ValueError:
        print("Harap masukkan angka!")

def delete_data():
    print("|=========================|")
    print("|                         |")
    print("|   Delete Data Pasien    |")
    print("|                         |")
    print("|=========================|")
    if not data_pasien:
        print("Tidak ada data pasien untuk dihapus.")
        return
    lihat_data_pasien()
    try:
        no_antrian = int(input("Input nomor pasien yang ingin dihapus: "))
        idx = no_antrian - 1
        if 0 <= idx < len(data_pasien):
            data_pasien.pop(idx)
            print("Data pasien telah dihapus")
        else:
            print("Data pasien tidak dapat ditemukan")
    except ValueError:
        print("Harap masukkan angka!")

def metode_pembayaran():
    while True:
        print("-------Pilih Metode Pembayaran-------")
        print("[A] BPJS")
        print("[B] Umum")
        try: 
            pilihan = input("pilih option yang tertera (A/B): ").strip().lower()
            if pilihan == "a":
                print("Menggunakan BPJS")
                break
            elif pilihan == "b":
                print("Menggunakan Umum")
                break
            else:
                print("Menu yang anda masukkan tidak tersedia! Silahkan ulangi kembali!")
        except:
            print("Tolong masukkan angka!")

def cetak_struk():
    while True:
        no_antrian = len(data_pasien)
        print("======================================")
        print("         PUSKESMAS MANTAP")
        print("          KOTA SAMARINDA")
        print("======================================")
        print()
        print("         NOMOR ANTRIAN", no_antrian )
        print()
        print("   Terimakasih Atas Kunjungan Anda")
        print("        Semoga Lekas sembuh")
        print("   Senin, 15 September 2025")
        print("              07.15")
        break


def login_pasien():
    while True:
            username = input("Masukkan username anda: ")
            password = input("Masukkan password anda: ")
            if username == akun["pasien"]["username"] and password == akun["pasien"]["password"]:
                print("Login Berhasil!")
                return True
            else:
                print("Username atau Password yang anda masukkan salah!")
                return False

def pasien():
    while True:
        try:
            print("|=========================|")
            print("|                         |")
            print("|         welcome         |")
            print("|                         |")
            print("|=========================|")
            print("| 1. Lihat Data Pasien    |")
            print("| 2. Logout               |")
            print("|=========================|")
            pilihan = input("Pilih menu (1-2): ")
            if pilihan == "1":
                lihat_data_pasien()
            elif pilihan == "2":
                print("Anda telah Logout")
                return True
            else:
                print("Menu tidak tersedia")
        except:
            print("Terjadi error")

login()