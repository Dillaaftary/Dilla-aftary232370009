# Rekam Data Mahasiswa 

import sys
import os

class Mahasiswa:
    def __init__(self, nim=0, nama=""):
        self.nim = nim
        self.nama = nama

dataSiswa = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        clear()
        print("Menu Aplikasi Data Siswa LinkedList Python")
        print("-------------------------------------------")
        print("1. Input Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Author")
        print("6. Keluar Aplikasi")
        try:
            pilih = int(input("Masukkan pilihan anda : "))
        except ValueError:
            input("Input tidak valid. Tekan Enter untuk kembali...")
            continue

        if pilih == 1:
            input_data()
        elif pilih == 2:
            tampil()
            input("Tekan Enter untuk kembali ke menu utama...")
        elif pilih == 3:
            update_data()
        elif pilih == 4:
            hapus_data()
        elif pilih == 5:
            author()
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif pilih == 6:
            print("Keluar aplikasi...")
            sys.exit()
        else:
            input("Pilihan tidak tersedia. Tekan Enter untuk kembali...")

def tampil():
    clear()
    print("DATA MAHASISWA")
    print("---------------")
    if not dataSiswa:
        print("Belum ada data mahasiswa.")
        return
    for data in dataSiswa:
        print("NIM  : " + str(data.nim))
        print("Nama : " + str(data.nama))
        print("----------------------")

def author():
    clear()
    print("Author : alvin meko | 672010193")
    print("UKSW 2015")

def input_data():
    ulang = 'Y'
    while ulang.upper() == 'Y':
        clear()
        siswaBaru = Mahasiswa()
        print("INPUT DATA MAHASISWA")
        try:
            siswaBaru.nim = int(input("masukkan nim : "))
        except ValueError:
            input("NIM harus berupa angka. Tekan Enter untuk ulang...")
            continue
        siswaBaru.nama = input("masukkan nama siswa : ")
        dataSiswa.append(siswaBaru)
        ulang = input("Apakah Anda Ingin Mengulang (Y/T)? ")

def update_data():
    clear()
    if not dataSiswa:
        input("Belum ada data. Tekan Enter untuk kembali...")
        return
    tampil()
    try:
        id_edit = int(input("Input NIM yang akan di update: "))
    except ValueError:
        input("NIM harus berupa angka. Tekan Enter untuk kembali...")
        return

    index_update = -1
    for a in range(0, len(dataSiswa)):
        if id_edit == dataSiswa[a].nim:
            index_update = a
            break

    if index_update > -1:
        print("INPUT DATA YANG DI UPDATE")
        try:
            new_nim = int(input("masukkan nim baru : "))
        except ValueError:
            input("NIM harus berupa angka. Tekan Enter untuk kembali...")
            return
        new_nama = input("masukkan nama siswa baru : ")
        dataSiswa[index_update].nim = new_nim
        dataSiswa[index_update].nama = new_nama
        print("Berhasil update data siswa.")
    else:
        print("NIM tidak ditemukan.")
    input("Tekan Enter untuk kembali...")

def hapus_data():
    clear()
    if not dataSiswa:
        input("Belum ada data. Tekan Enter untuk kembali...")
        return
    tampil()
    try:
        id_hapus = int(input("Input NIM yang akan di hapus : "))
    except ValueError:
        input("NIM harus berupa angka. Tekan Enter untuk kembali...")
        return

    index_delete = -1
    for a in range(0, len(dataSiswa)):
        if id_hapus == dataSiswa[a].nim:
            index_delete = a
            break

    if index_delete > -1:
        del dataSiswa[index_delete]
        print("Data telah dihapus.")
    else:
        print("NIM tidak ditemukan.")
    input("Tekan Enter untuk kembali...")

if __name__ == "__main__":
    menu()