#NAMA   : Muhammad Salman Azizi
#NIM    : 122140131
#Kelas  : PBO RB

#NO.2
jari = float(input("jari-jari: "))
phi = 3.14

if jari < 0:
    print("jari-jari lingkaran tidak boleh negatif")
else:
    luas = phi * jari ** 2
    keliling = 2 * phi * jari
    print("luas: ",luas)
    print("keliling: ",keliling)