#Program Input data mahasiswa menggunakan list dan dictonary

#Input jumlah mahasiswa 
jumlah = int (input("Masukkan jumlah mahasiswa :"))

#List untuk menampung data semua mahasiswa
data_mahasiswa =[]

#Loop untuk input data tiap mahasiswa
for i in range(jumlah):
    print(f"\nMahasiswa {i+1}")
    nama = input("Nama  :")
    umur = input("Umur  :")
    alamat = input("Alamat :")

    #Simpan data dalam dictionary
    mahasiswa = {
        "Nama": nama,
        "Umur": umur,
        "Alamat": alamat
    }
    #Tambahkan ke list utama
    data_mahasiswa.append(mahasiswa)

#Menampilkan data mahasiswa
print("\n=== Data mahasiswa===")
for i, mhs in enumerate(data_mahasiswa, start=1):
    print(f"\nMahasiswa {i}")
    print(f"Nama     :{mhs['Nama']}")
    print(f"Umur     :{mhs['Umur']}")
    print(f"Alamat   :{mhs['Alamat']}")

