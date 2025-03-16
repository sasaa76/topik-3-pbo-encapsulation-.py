# topik-3-pbo-encapsulation-.py
Tugas Topik 3
Nama : Amalia Sajidah
NIM : A710240042

class Komputer:
    def _init_(self, merek, tipe):
        self.merek = merek
        self.tipe = tipe
    
    def nyalakan(self):
        print(f"{self.merek} {self.tipe} sekarang menyala")
    
    def matikan(self):
        print(f"{self.merek} {self.tipe} sekarang mati")

komputer1 = Komputer("Lenovo", "ThinkPad")
komputer2 = Komputer("Dell", "XPS")

komputer1.nyalakan()
komputer1.matikan()

komputer2.nyalakan()
komputer2.matikan()

Berdasarkan hasil program pada tugas class dan object diatas 

Buatlah :

1. Ubah 2 properties menjadi private

2. Buat method getter dan setter

3. Buat objek baru dan akses variabel private tersebut menggunakan method getter dan setter

4. Kumpulkan link github/replit
