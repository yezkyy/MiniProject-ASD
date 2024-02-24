import os
import random

#Pembuatan ID Pesanan otomatis untuk menunjukan identitas pesanan
def generate_id_pesanan():
    nomor_acak = random.randint(100000, 999999)
    id_pesanan = "ORD-" + str(nomor_acak)
    return id_pesanan

class Distribusi:
    def __init__(self,nama_barang,model_seri,nama_costumer,alamat,kuantitas):
        self.nama_barang = nama_barang
        self.model_seri = model_seri
        self.nama_costumer = nama_costumer
        self.alamat = alamat
        self.kuantitas = kuantitas

class DistribusiBarang:
    def __init__(self):
        self.list_pesanan = [
            {
                "id_pesanan": "ORD-453891",
                "nama_barang": "RAM 8GB",
                "model_seri": "Kingston HyperX FURY",
                "nama_costumer": "Budi Santoso",
                "alamat": "Jl. Samanhudi No 45, Samarinda",
                "kuantitas": 20
            },
            {
                "id_pesanan": "ORD-622437",
                "nama_barang": "Hardisk 2TB",
                "model_seri": "Transcend StoreJet 25C3S",
                "nama_costumer": "PT.Hosting Ficer",
                "alamat": "Jl. Sudirman No. 23, Bandung",
                "kuantitas": 40
            },
            {
                "id_pesanan": "ORD-905331",
                "nama_barang": "Mikrotik Indoor",
                "model_seri": "RB1100AHx4",
                "nama_costumer": "Toko Lizi Network",
                "alamat": "Jl. Diponegoro No. 34, Semarang",
                "kuantitas": 24
            }
        ]
    
    def tambah_pesanan(self):
        id_pesanan = generate_id_pesanan()

        # Input Informasi Pesanan
        nama_barang = input ("Masukan Nama Barang: ")
        model_seri = input ("Masukan Model Seri: ")
        nama_costumer = input ("Masukan Nama Costumer: ")
        alamat = input ("Masukan Alamat Costumer: ")
        kuantitas = int(input("Masukan Kuantitas Barang: "))

        pesanan = {
            "id_pesanan": id_pesanan,
            "nama_barang": nama_barang,
            "model_seri": model_seri,
            "nama_costumer": nama_costumer,
            "alamat": alamat,
            "kuantitas": kuantitas,
        }

        self.list_pesanan.append(pesanan)
        os.system ("cls")
        print ("Pesanan Berhasil dibuat dan akan di proses ke Costumer dengan Informasi")
        print (f"Nama Barang : {nama_barang}")
        print (f"Model Seri : {model_seri}")
        print (f"Nama Costumer : {nama_costumer}")
        print (f"Alamat : {alamat}")
        print (f"Kuantitas Barang : {kuantitas}")
        os.system ("pause")

    def lihat_pesanan(self):
        if len(self.list_pesanan) == 0:
            print("╔══════════════════════════════════╗")
            print(" Belum ada Pesanan yang dikirimkan ")
            print("╚══════════════════════════════════╝")
            os.system("pause")
            return
        else:
            print("\nDaftar Pesanan")
            for i, pesanan in enumerate(self.list_pesanan):
                print("==============================================================")
                print(f"Pesanan {i+1}:")
                print(f"ID Pesanan: {pesanan['id_pesanan']}")
                print(f"Nama Barang: {pesanan['nama_barang']}")
                print(f"Model Seri: {pesanan['model_seri']}")
                print(f"Nama Costumer: {pesanan['nama_costumer']}")
                print(f"Alamat: {pesanan['alamat']}")
                print(f"Kuantitas Barang: {pesanan['kuantitas']}")
                print("==============================================================")
        os.system ("pause")

    def perbarui_barang(self):
        if len(self.list_pesanan) == 0:
            print("╔══════════════════════════════════╗")
            print(" Belum ada Pesanan yang dikirimkan ")
            print("╚══════════════════════════════════╝")
            os.system("pause")
            return

        # Menampilkan daftar pesanan
        self.lihat_pesanan()
        nomor_pesanan = int(input("Masukkan nomor pesanan yang ingin diubah: ")) - 1

        #Memastikan nomor pesanan valid/ada
        if nomor_pesanan < 0 or nomor_pesanan >= len(self.list_pesanan):
            print("╔═══════════════════════════╗")
            print("  Nomor Pesanan Tidak Valid ")
            print("╚═══════════════════════════╝")
            os.system("pause")
            return

        pesanan_terpilih = self.list_pesanan[nomor_pesanan]
        print("\nApa yang ingin Anda ubah pada pesanan ini?")
        print("1. Nama Barang")
        print("2. Model Seri")
        print("3. Nama Costumer")
        print("4. Alamat")
        print("5. Kuantitas Barang")
        print("6. Kembali ke Menu Utama")

        pilihan = input("Pilih opsi: ")

        #Memproses pilihan
        if pilihan == '1':
            nama_barang_baru = input("Masukkan Nama Barang baru: ").strip()
            pesanan_terpilih['nama_barang'] = nama_barang_baru
        elif pilihan == '2':
            model_seri_baru = input("Masukkan Model Seri baru: ").strip()
            pesanan_terpilih['model_seri'] = model_seri_baru
        elif pilihan == '3':
            nama_costumer_baru = input("Masukkan Nama Costumer baru: ").strip()
            pesanan_terpilih['nama_costumer'] = nama_costumer_baru
        elif pilihan == '4':
            alamat_baru = input("Masukkan Alamat Costumer baru: ").strip()
            pesanan_terpilih['alamat'] = alamat_baru
        elif pilihan == '5':
            kuantitas_baru = int(input("Masukkan Kuantitas Barang baru: ").strip())
            pesanan_terpilih['kuantitas'] = kuantitas_baru
        elif pilihan == '6':
            return
        else:
            print("Opsi tidak valid.")
            os.system("pause")
            return

        print("╔════════════════════════════╗")
        print(" Pesanan Berhasil Diperbarui ")
        print("╚════════════════════════════╝")
        os.system("pause")

    def hapus_barang(self):
        if len(self.list_pesanan) == 0:
            print("╔══════════════════════════════════╗")
            print(" Belum ada Pesanan yang dikirimkan ")
            print("╚══════════════════════════════════╝")
            os.system("pause")
            return
        
        #Menampilkan Daftar Pesanan
        self.lihat_pesanan()

        #Meminta nomor pesanan yang ingin dihapus
        while True:
            nomor_pesanan = int(input("Masukkan nomor pesanan yang ingin dihapus: ")) - 1
            if nomor_pesanan < 0 or nomor_pesanan >= len(self.list_pesanan):
                print("╔═══════════════════════════╗")
                print("  Nomor Pesanan Tidak Valid ")
                print("╚═══════════════════════════╝")
                continue
            break

        #Proses Menghapus pesanan
        del self.list_pesanan[nomor_pesanan]

        print("╔═════════════════════════╗")
        print(" Pesanan Berhasil Dihapus ")
        print("╚═════════════════════════╝")
        os.system("pause")

distribusi_barang = DistribusiBarang()

# Menampilkan Menu
while True:
    os.system ("cls")
    print("═════════════════════════════")
    print("Distributor Hardware Komputer")
    print("═════════════════════════════")
    print("Menu :")
    print("1. Tambah Pesanan Barang")
    print("2. Lihat Pesanan Barang")
    print("3. Perbarui Pesanan Barang")
    print("4. Hapus Pesanan Barang")
    print("5. Keluar")
    pilihan = int(input("Pilih Menu : "))

    if pilihan == 1:
        distribusi_barang.tambah_pesanan()
    elif pilihan == 2:
        distribusi_barang.lihat_pesanan()
    elif pilihan == 3:
        distribusi_barang.perbarui_barang()
    elif pilihan == 4:
        distribusi_barang.hapus_barang()
    elif pilihan == 5:
        print("╔══════════════════════════════════╗")
        print(" Anda Telah keluar dari Program ini ")
        print("╚══════════════════════════════════╝")
        exit()
    else:
        print("╔═══════════════════╗")
        print(" Opsi Menu tidak ada ")
        print("╚═══════════════════╝")
        os.system ("pause")