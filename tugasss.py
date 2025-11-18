# ===========================================
# PROGRAM HITUNG IP MENGGUNAKAN FUNGSI
# ===========================================

def konversi_bobot(nilai):
    """Mengubah nilai angka (0–100) menjadi bobot (0–4)."""
    if nilai >= 85:
        return 4
    elif nilai >= 75:
        return 3
    elif nilai >= 65:
        return 2
    elif nilai >= 55:
        return 1
    else:
        return 0


def hitung_ip(daftar_mk):
    """Menghitung IP berdasarkan list mata kuliah."""
    total_sks = 0
    total_bobot = 0

    for mk in daftar_mk:
        sks = mk["sks"]
        bobot = mk["bobot"]

        total_sks += sks
        total_bobot += bobot * sks

    return total_bobot / total_sks


# ===========================================
# INPUT
# ===========================================

print("====================================")
print("        PROGRAM HITUNG IP")
print("====================================")

nama = input("Nama : ")
npm = input("NPM  : ")

jumlah = int(input("\nJumlah mata kuliah : "))

daftar_mk = []

for i in range(jumlah):
    print(f"\n--- Mata Kuliah {i+1} ---")
    mk = input("Nama MK      : ")
    sks = int(input("SKS          : "))
    nilai = int(input("Nilai (0-100): "))

    bobot = konversi_bobot(nilai)

    daftar_mk.append({
        "nama": mk,
        "sks": sks,
        "nilai": nilai,
        "bobot": bobot
    })

# ===========================================
# OUTPUT
# ===========================================

ip = hitung_ip(daftar_mk)

print("\n====================================")
print("       KARTU HASIL STUDI (KHS)")
print("====================================")
print(f"Nama : {nama}")
print(f"NPM  : {npm}\n")

for mk in daftar_mk:
    print(f"{mk['nama']} : {mk['bobot']}")

print("\nIP Anda :", round(ip, 2))
print("====================================")
