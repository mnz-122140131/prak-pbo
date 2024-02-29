#NAMA   : Muhammad Salman Azizi
#NIM    : 122140131
#Kelas  : PBO RB

#NO.1
low = int(input("Batas bawah: "))
up = int(input("Batas atas: "))

if low < 0 or up < 0:
    print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah Nol")
else:
    odd = [odd for odd in range(low, up) if odd % 2 != 0]
    
    for odd_number in odd:
        print(odd_number)
    
    print("Total:", sum(odd))
