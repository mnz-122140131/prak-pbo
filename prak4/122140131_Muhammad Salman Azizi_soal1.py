class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.makan = False

    def bersuara(self):
        if not self.makan:
            self.makan = True
        else:
            print(f"{self.__class__.__name__} {self.nama} sedang makan: tulang")
            self.makan = False

class Kucing(Hewan):
    def bersuara(self):
        if not self.makan:
            print(f"Kucing {self.nama} bersuara: Meong!")
        super().bersuara()

class Anjing(Hewan):
    def bersuara(self):
        if not self.makan:
            print(f"Anjing {self.nama} bersuara: Guk Guk!")
        super().bersuara()

hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama)
print(hewan2.nama)

hewan1.bersuara()
hewan1.bersuara()
hewan2.bersuara()
hewan2.bersuara()
