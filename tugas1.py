# ===================================================
# Program: tugas1.py
# Deskripsi:
# Menampilkan pola segitiga bintang terbalik lalu naik
# dengan posisi tengah yang rapi di terminal
# ===================================================

# Input dari pengguna
n = int(input("Masukkan angka : "))

# Segitiga terbalik (turun)
for i in range(n, 0, -1):
    # Spasi kiri untuk meratakan ke tengah
    for j in range(n - i):
        print(" ", end=" ")
    # Bintang
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# Segitiga normal (naik)
for i in range(2, n + 1):
    # Spasi kiri untuk meratakan ke tengah
    for j in range(n - i):
        print(" ", end=" ")
    # Bintang
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()