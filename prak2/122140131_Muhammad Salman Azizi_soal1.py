class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.__angkatan = angkatan
        self.__isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def display_info(self):
        if self.__isMahasiswa:
            status = "Mahasiswa"
        else:
            status = "Bukan Mahasiswa"
        return f"NIM: {self.__nim}\nNama: {self.__nama}\nAngkatan: {self.__angkatan}\nStatus: {status}"

    def is_lulus(self):
        return "Lulus" if self.__angkatan <= 2022 else "Belum Lulus"

    def get_status_mahasiswa(self):
        return "Aktif" if self.__isMahasiswa else "Tidak Aktif"


mahasiswa1 = Mahasiswa("122140131", "Muhammad Salman Azizi", 2024)
print("Informasi Mahasiswa 1 sebelum perubahan:")
print(mahasiswa1.display_info())
print("Status Mahasiswa 1:", mahasiswa1.get_status_mahasiswa())
print("Apakah mahasiswa 1 lulus? ", mahasiswa1.is_lulus())

mahasiswa1.set_nama("Ronaldinho")
mahasiswa1.set_nim("122140141")

print("\nInformasi Mahasiswa 1 setelah perubahan:")
print(mahasiswa1.display_info())


mahasiswa2 = Mahasiswa("122140132", "Ambatukham", 2020, isMahasiswa=False)
print("\nInformasi Mahasiswa 2 sebelum perubahan:")
print(mahasiswa2.display_info())
print("Status Mahasiswa 2:", mahasiswa2.get_status_mahasiswa())
print("Apakah mahasiswa 2 lulus? ", mahasiswa2.is_lulus())

mahasiswa2.set_nama("David Bekam")
mahasiswa2.set_nim("122140122")

print("\nInformasi Mahasiswa 2 setelah perubahan:")
print(mahasiswa2.display_info())