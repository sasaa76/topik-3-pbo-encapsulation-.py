class Komputer:
    def __init__(self, merek, tipe):
        self.__merek = merek 
        self.__tipe = tipe   
    
    def get_merek(self):
        return self.__merek
    
    def get_tipe(self):
        return self.__tipe
    
    def set_merek(self, merek_baru):
        self.__merek = merek_baru
    
    def set_tipe(self, tipe_baru):
        self.__tipe = tipe_baru
    
    def nyalakan(self):
        print(f"{self.__merek} {self.__tipe} sekarang menyala")
    
    def matikan(self):
        print(f"{self.__merek} {self.__tipe} sekarang mati")


komputer1 = Komputer("Lenovo", "ThinkPad")
komputer2 = Komputer("Dell", "XPS")

komputer1.nyalakan()
komputer1.matikan()

komputer2.nyalakan()
komputer2.matikan()

komputer3 = Komputer("HP", "Pavilion")

print(f"Merek komputer 3: {komputer3.get_merek()}")
print(f"Tipe komputer 3: {komputer3.get_tipe()}")

komputer3.set_merek("Asus")
komputer3.set_tipe("ROG")

print(f"Merek komputer 3 setelah diubah: {komputer3.get_merek()}")
print(f"Tipe komputer 3 setelah diubah: {komputer3.get_tipe()}")

komputer3.nyalakan()
komputer3.matikan()
