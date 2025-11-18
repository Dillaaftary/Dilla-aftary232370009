#Program untuk menampilkan bilangan prima yang lebih kecil dari 30 
#fungsi untuk mengecek apakah sebuah bilangan adalah bilangan prima
def is_prima(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
#Menampilkan bilangan prima yang lebih kecil dari 30
print("Bilangan prima yang lebih kecil dari 30 adalah:")

for angka in range(2,30):
    if is_prima(angka):
        print(angka, end=" ")
