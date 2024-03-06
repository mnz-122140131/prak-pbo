class Bus:
    def __init__(self, nomor_bus, kapasitas, rute):
        self.nomor_bus = nomor_bus
        self.kapasitas = kapasitas
        self.rute = rute
        self.penumpang = 0

    def __del__(self):
        print(f"Bus {self.nomor_bus} telah selesai beroperasi.")

    @property
    def available_seats(self):
        return self.kapasitas - self.penumpang

    def pick_up_passengers(self, jumlah_penumpang):
        if jumlah_penumpang <= self.available_seats:
            self.penumpang += jumlah_penumpang
            print(f"{jumlah_penumpang} penumpang telah naik ke Bus {self.nomor_bus}.")
        else:
            print("Bus penuh. Tidak dapat menampung lebih banyak penumpang.")

    def drop_off_passengers(self, jumlah_penumpang):
        if jumlah_penumpang <= self.penumpang:
            self.penumpang -= jumlah_penumpang
            print(f"{jumlah_penumpang} penumpang telah turun dari Bus {self.nomor_bus}.")
        else:
            print("Jumlah penumpang yang turun melebihi jumlah penumpang di dalam bus.")


def valid_route(func):
    def wrapper(self, *args, **kwargs):
        rute = kwargs.get("rute", "")
        if rute.lower() in ["a", "b", "c"]:
            func(self, *args, **kwargs)
        else:
            print("Rute tidak valid. Pilih rute A, B, atau C.")
    return wrapper

class BusOperator:
    @valid_route
    def set_bus_route(self, bus, rute):
        bus.rute = rute
        print(f"Bus {bus.nomor_bus} telah diatur untuk menjalankan rute {rute.upper()}.")

bus1 = Bus(nomor_bus="001", kapasitas=30, rute="A")

operator = BusOperator()

operator.set_bus_route(bus1, rute="D")  # Contoh rute yang tidak valid
operator.set_bus_route(bus1, rute="B")  # Contoh rute yang valid


bus1.pick_up_passengers(15)
bus1.drop_off_passengers(5)

# Hapus objek Bus (akan memanggil destructor)
del bus1
