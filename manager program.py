class Karyawan:
    def __init__(self, namakaryawan, gaji):
        self.nama = namakaryawan #tetapkan nilai dari parameter namakaryawan menjadi isi yang permanen untuk atribut nama milik objek itu sendiri
        self.gaji = gaji #tetapkan nilai dari parameter gaji menjadi isi yang permanen untuk atribut gaji milik objek itu sendiri

    def tampilkanprofil(self): #metode untuk menampilkan profil
        print("data awal") 
        print(f"Nama: {self.nama} | gaji: {self.gaji:,}") #mencari data nama dan juga gaji milik objek itu sendiri lalu sisipkan bersama teks

class Manager(Karyawan): #manager mewrisi isi dari class karywan
    def tambahgaji(self, jumlah): #metode untuk menambah gaji karyawan
        self.gaji += jumlah #cari data gaji milik objek saat ini lalu tambahkan datanya dengan nilai dari parameter jumlah 
        print("--- MEMBERI BONUS ---")
        print(f"Bonus berhasil ditambahkan untuk {self.nama}!") 
        print()
        print("data akhir")
        print(f"Nama: {self.nama} | gaji: {self.gaji:,}")

karyawan1 = Manager("rusdi", 1000) #karyawan1 berisi hasil dari pemanggilan constructor milik class manager dengan argumen rusdi dan 1000
karyawan2 = Manager("pandu", 1500) #karyawan1 berisi hasil dari pemanggilan constructor milik class manager dengan argumen pandu dan 1500

daftarkaryawan = { 1 : karyawan1, #dictionary yang berisi value yang menunjuk ke objek karyawan1 untuk key 1
                   2 : karyawan2} #dictionary yang berisi value yang menunjuk ke objek karyawan2 untuk key 2

while True:
    print("pilih karyawan yang diberi bonus")
    print(f"1 {daftarkaryawan[1].nama}") #ambil isi dari kunci 1 yang ada di dalam daftarkaryawan lalu cari data nama milik objek yang sedang ditunjuk oleh isi
    print(f"2 {daftarkaryawan[2].nama}") #ambil isi dari kunci 2 yang ada di dalam daftarkaryawan lalu cari data nama milik objek yang sedang ditunjuk oleh isi
    pilihkaryawan = input("pilih (q to quit): ") #minta input dari user lalu masukkan input itu ke pilihankaryawan

    if pilihkaryawan.lower() == "q": #cek jika inputuser diubah menjadi huruf kecil dan hasilnya sama dengan q
        break #maka hentikan loop
    elif not pilihkaryawan.isdigit(): #cek jika inputuser bukan digit
        print("harus no yang ada di atas") #maka cetak teks ini
        continue #skip kode dibawahnya dan kembali ke bagian atas

    pilihkaryawan = int(pilihkaryawan) #ubah tipe data dari pilihankaryawan menjadi int lalu masukkan ke pil
    karyawandiberibonus = daftarkaryawan.get(pilihkaryawan) #untuk mendapatkn isi dari kunci yang ada di pilihankaryan lalu memasukkannya ke dalam 
                                                            #variable karyawandiberibonus 
            
    if karyawandiberibonus is not None: #CEK JIKA ISI NYA TIDAK NONE,JALANKAN DIBAWAH INI
            while True: #SEMASIH TRUE JALANKAN PROGRAM INI
                beribonus = input(f"masukkan bonus untuk {karyawandiberibonus.nama} (q to quit): ")
                
                if beribonus.lower() == "q": #cek jika inputuser diubah menjadi huruf kecil dan hasilnya sama dengan q  
                    break #maka hentikan loop
                elif not beribonus.isdigit(): #cek jika inputuser bukan digit
                    print("selain digit dilarang")
                    continue #skip kode dibawahnya dan kembali ke bagian atas (LOOP DALAM)
                
                beribonus = int(beribonus) # #ubah tipe data dari beribonus menjadi int lalu masukkan ke beribonus
                karyawandiberibonus.tampilkanprofil() #panggil metode ini milik objek yang sedang ditunjuk lalu jalankn sluruh instruksinya
                print()
                karyawandiberibonus.tambahgaji(beribonus) #panggil metode ini milik objek yang sedang ditunjuk dengan argumen beribonus
                                                          #lalu jalankn sluruh instruksinya
    else: #CEK JIKA ISI ADALAH NONE 
        print("no yang anda pilih tidak ada data karyawannya")
        continue #skip kode dibawahnya dan kembali ke bagian atas





