#super() tahu objek yang sedang dibuat karena self sudah otomatis 
#dibawa, sedangkan Akses.__init__ harus diberi self karena dipanggil lewat nama class, dan super() memanggil 
#constructor sesuai urutan pewarisan (MRO), bukan sembarang class.

#super().__init__() dipakai untuk memanggil constructor class induk pertama secara otomatis tanpa menulis self
#Jika ada lebih dari satu class induk, constructor class lain harus dipanggil manual
#Pemanggilan manual constructor wajib memakai self agar atribut masuk ke objek yang sedang dibuat
#Semua constructor yang dipanggil (super maupun manual) mengisi satu objek yang sama, bukan membuat objek baru

class Karyawan:
    def __init__(self, nama, gaji):   
        self.nama = nama              
        self.gaji = gaji              
    def tampilkan_info(self):
        print(f"nama: {self.nama} | gaji: {self.gaji}")  

class Akses:
    def __init__(self, level):        
        self.level = level            

    def cek_akses(self):
        print(f"level : {self.level}")  
        print()


class Manager(Karyawan, Akses):       
    def __init__(self, nama, gaji, level):
        super().__init__(nama, gaji)  
        Akses.__init__(self, level)   

    def tambahgaji(self, jumlah):
        self.gaji += jumlah           
        print("jumlah berhasil ditambahkan")
        print(f"jumlah yang ditambahkan {jumlah}")
        print(f"Gaji {self.nama} sekarang {self.gaji}")
        print()

    def tampilkan_lengkap(self):
        self.tampilkan_info()         
        self.cek_akses()              


def main():
    
    manager = Manager("hartono", 1000, "karyawan")
    manager2 = Manager("Budi", 1000, "karyawan")
    manager3 = Manager("tino", 500, "staff")

    
    daftarkaryawan = {
        1: manager,
        2: manager2,
        3: manager3
    }

    while True:  
        print("1.lihat semua karyawan")
        print("2.tambah bonus karyawan ")
        print("3.cek akses karyawan")
        print("4.keluar")

        pilihan = input("pilih: ")    

        if not pilihan.isdigit():     
            print("Masukkan pilihan di atas")
            continue

        pilihan = int(pilihan)       

        if pilihan == 1:
            for k, v in daftarkaryawan.items():  
                print(f"no urut: {k} | nama karyawan {v.nama}")
            print()
            continue

        elif pilihan == 2:
            while True:
                for k, v in daftarkaryawan.items():
                    print(f"no urut: {k} | nama karyawan {v.nama}")

                pilihkrywn = input("masukkan no karywan yang diberi bonus(q to quit): ")

                if pilihkrywn.lower() == "q":
                    break
                elif not pilihkrywn.isdigit():
                    print("masukkan no yang benar!")
                    continue

                pilihkrywn = int(pilihkrywn)
                karyawandibribonus = daftarkaryawan.get(pilihkrywn)

                if karyawandibribonus is not None:
                    while True:
                        jumlhbonus = input(f"masukkan jumlah bonus untuk {karyawandibribonus.nama} (q to quit): ")

                        if jumlhbonus.lower() == "q":
                            break
                        elif not jumlhbonus.isdigit():
                            print("Jumlah harus digit!")
                            continue

                        jumlhbonus = int(jumlhbonus)

                        if jumlhbonus <= 0:
                            print("jumlh yng diberikan harus lebih besar dari 0")
                            continue
                        
                        karyawandibribonus.tambahgaji(jumlhbonus)  
                        break
                else:
                    print("tidak ada karyawan dengan no itu")

        elif pilihan == 3:
            while True:
                for k, v in daftarkaryawan.items():
                    print(f"no urut: {k} | nama karyawan {v.nama}")

                pilihkrywn = input("masukkan no karywan (q to quit): ")

                if pilihkrywn.lower() == "q":
                    break
                elif not pilihkrywn.isdigit():
                    print("Dilarang memasukkan selain angka")
                    continue

                pilihkrywn = int(pilihkrywn)
                karyawandiakses = daftarkaryawan.get(pilihkrywn)

                if karyawandiakses is not None:
                    karyawandiakses.tampilkan_lengkap()  
                else:
                    print("no karyawan tidak ada")

        elif pilihan == 4:
            break  
        else:
            print("Masukkan pilihan yang benar")


if __name__ == "__main__":
    main()  