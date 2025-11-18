# Program: verifikasi_data.py
# Deskripsi: tugas3.py

data = input("Masukkan Umur Kamu: ")

if data.isdigit():
    print("Data ini adalah angka integer. Angka =", int(data))
elif data.replace(".", "", 1).isdigit():
    print("Data ini adalah data float. Angka =", float(data))
else:
    print("Data yang anda inputkan adalah tipe string", type(data).__name__)