#Nama  : Muhammad Salman Azizi
#NIM   : 122140131
#Kelas : RB

class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((self.__nama, self.__stok, self.__harga))

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for barang in Dagangan.list_barang:
            if barang[0] == self.__nama:
                Dagangan.list_barang.remove(barang)
                print(f"\n{self.__nama} dihapus dari toko!")
                break

    @staticmethod
    def lihat_barang():
        print(f"Jumlah barang dagangan pada toko: {Dagangan.jumlah_barang} buah")
        print("="*50)
        for i, barang in enumerate(Dagangan.list_barang, 1):
            print(f"{i}. {barang[0]} seharga Rp {barang[2]} (stok: {barang[1]})")



# Main Program
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()

print("="*50)
del Dagangan1
print()

Dagangan.lihat_barang()
