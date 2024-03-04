import random
import os
import time

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class DistribusiBarang:
    def __init__(self):
        self.head = None
        
    def tambah_diawal(self, data):
        node_baru = Node(data)
        if not self.head:
            node_baru.next = node_baru
            self.head = node_baru
        else:
            node_baru.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node_baru
            self.head = node_baru

    def tambah_ditengah(self, data, id_setelahnya):
        node_baru = Node(data)
        if not self.head:
            print("List kosong. Tidak dapat menambah di tengah.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
            return
        current = self.head
        while True:
            if current.data['id_pesanan'] == id_setelahnya:
                node_baru.next = current.next
                current.next = node_baru
                return
            current = current.next
            if current == self.head:
                break
        print("ID tidak ditemukan. Tidak dapat menambah di tengah.")
        a = input("Tekan Enter untuk kembali ke menu sebelumnya")
        if a == "":
            os.system('cls')
    
    def tambah_diakhir(self, data):
        node_baru = Node(data)
        if not self.head:
            node_baru.next = node_baru
            self.head = node_baru
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node_baru
            node_baru.next = self.head

    def display(self):
        if not self.head:
            os.system ('cls')
            print("Tidak ada barang yang di diantar")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                return
        current = self.head
        while True:
            print("ID Pesanan:", current.data['id_pesanan'])
            print("Nama Barang:", current.data['nama_barang'])
            print("Model Seri:", current.data['model_seri'])
            print("Nama Costumer:", current.data['nama_costumer'])
            print("Alamat:", current.data['alamat'])
            print("Kuantitas Barang:", current.data['kuantitas'])
            print("-------------------------------------------")
            current = current.next
            if current == self.head:
                break

    def cari(self, id_pesanan):
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data['id_pesanan'] == id_pesanan:
                return current.data
            current = current.next
            if current == self.head:
                break
        return None
    
    def hapus_diawal(self):
        if not self.head:
            print("Tidak ada pesanan yang dapat dihapus.")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        print("Pesanan di awal berhasil dihapus.")
        a = input("Tekan Enter untuk kembali ke menu sebelumnya")
        if a == "":
            os.system('cls')

    def hapus_ditengah(self, id_pesanan):
        if not self.head:
            print("Tidak ada pesanan yang dapat dihapus.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
            return
        if self.head.data['id_pesanan'] == id_pesanan:
            self.hapus_diawal()
            return
        current = self.head
        prev = None
        while True:
            if current.data['id_pesanan'] == id_pesanan:
                prev.next = current.next
                current = None
                print("Pesanan di tengah berhasil dihapus.")
                a = input("Tekan Enter untuk kembali ke menu sebelumnya")
                if a == "":
                    os.system('cls')
                return
            prev = current
            current = current.next
            if current == self.head:
                break
        print("ID pesanan tidak ditemukan. Tidak ada pesanan yang dihapus.")
        a = input("Tekan Enter untuk kembali ke menu sebelumnya")
        if a == "":
            os.system('cls')

    def hapus_diakhir(self):
        if not self.head:
            print("Tidak ada pesanan yang dapat dihapus.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
            return
        if self.head.next == self.head:
            self.head = None
            print("Pesanan di akhir berhasil dihapus.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
            return
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
        prev.next = self.head
        print("Pesanan di akhir berhasil dihapus.")
        a = input("Tekan Enter untuk kembali ke menu sebelumnya")
        if a == "":
            os.system('cls')

    def tambah_pesanan(self):
        print("Menu Tambah Pesanan:")
        print("1. Tambah di Awal")
        print("2. Tambah di Akhir")
        print("3. Tambah di Tengah")
        
        pilihan = input("Pilih tempat penambahan pesanan: ")
        if pilihan == "1":
            id_pesanan = generate_id_pesanan()
            nama_barang = input("Masukkan Nama Barang: ")
            model_seri = input("Masukkan Model Seri: ")
            nama_costumer = input("Masukkan Nama Costumer: ")
            alamat = input("Masukkan Alamat Costumer: ")
            kuantitas = int(input("Masukkan Kuantitas Barang: "))

            # Menampung semua data pesanan
            pesanan = {
                "id_pesanan": id_pesanan,
                "nama_barang": nama_barang,
                "model_seri": model_seri,
                "nama_costumer": nama_costumer,
                "alamat": alamat,
                "kuantitas": kuantitas,
            }
            self.tambah_diawal(pesanan)
        elif pilihan == "2":
            id_pesanan = generate_id_pesanan()
            nama_barang = input("Masukkan Nama Barang: ")
            model_seri = input("Masukkan Model Seri: ")
            nama_costumer = input("Masukkan Nama Costumer: ")
            alamat = input("Masukkan Alamat Costumer: ")
            kuantitas = int(input("Masukkan Kuantitas Barang: "))

            # Menampung semua data pesanan
            pesanan = {
                "id_pesanan": id_pesanan,
                "nama_barang": nama_barang,
                "model_seri": model_seri,
                "nama_costumer": nama_costumer,
                "alamat": alamat,
                "kuantitas": kuantitas,
            }
            self.tambah_diakhir(pesanan)
        elif pilihan == "3":
            id_pesanan = generate_id_pesanan()
            nama_barang = input("Masukkan Nama Barang: ")
            model_seri = input("Masukkan Model Seri: ")
            nama_costumer = input("Masukkan Nama Costumer: ")
            alamat = input("Masukkan Alamat Costumer: ")
            kuantitas = int(input("Masukkan Kuantitas Barang: "))

            # Menampung semua data pesanan
            pesanan = {
                "id_pesanan": id_pesanan,
                "nama_barang": nama_barang,
                "model_seri": model_seri,
                "nama_costumer": nama_costumer,
                "alamat": alamat,
                "kuantitas": kuantitas,
            }
            id_setelahnya = input("Masukkan ID Pesanan setelahnya: ")
            self.tambah_ditengah(pesanan, id_setelahnya)
        else:
            print("Opsi tidak valid.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
            return

    def lihat_pesanan(self):
        if not self.head:
            os.system ('cls')
            print("╔══════════════════════════════════╗")
            print(" Belum ada Pesanan yang dikirimkan ")
            print("╚══════════════════════════════════╝")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
        else:
            self.display()
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')

    def perbarui_barang(self, id_pesanan):
        pesanan = self.cari(id_pesanan)
        if pesanan:
            print("Pesanan ditemukan:")
            print("ID Pesanan:", pesanan['id_pesanan'])
            print("Nama Barang:", pesanan['nama_barang'])
            print("Model Seri:", pesanan['model_seri'])
            print("Nama Costumer:", pesanan['nama_costumer'])
            print("Alamat:", pesanan['alamat'])
            print("Kuantitas Barang:", pesanan['kuantitas'])
            print("-------------------------------------------")
            print("\nApa yang ingin Anda ubah pada pesanan ini?")
            print("1. Nama Barang")
            print("2. Model Seri")
            print("3. Nama Costumer")
            print("4. Alamat")
            print("5. Kuantitas Barang")
            print("6. Kembali ke Menu Utama")

            field_choice = input("Pilih opsi: ")
            if field_choice == "1":
                new_value = input("Masukkan Nama Barang baru: ")
                pesanan['nama_barang'] = new_value
                print("Nama Barang berhasil diperbarui.")
            elif field_choice == "2":
                new_value = input("Masukkan Model Seri baru: ")
                pesanan['model_seri'] = new_value
                print("Model Seri berhasil diperbarui.")
            elif field_choice == "3":
                new_value = input("Masukkan Nama Costumer baru: ")
                pesanan['nama_costumer'] = new_value
                print("Nama Costumer berhasil diperbarui.")
            elif field_choice == "4":
                new_value = input("Masukkan Alamat baru: ")
                pesanan['alamat'] = new_value
                print("Alamat berhasil diperbarui.")
            elif field_choice == "5":
                new_value = input("Masukkan Kuantitas Barang baru: ")
                pesanan['kuantitas'] = new_value
                print("Kuantitas Barang berhasil diperbarui.")
            elif field_choice == "6":
                print("Kembali ke Menu Utama.")
            else:
                print("Opsi tidak valid.")
                a = input("Tekan Enter untuk kembali ke menu sebelumnya")
                if a == "":
                    os.system('cls')
        else:
            print("Pesanan tidak ditemukan.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')

    def hapus_pesanan(self, id_pesanan):
        self.hapus_ditengah(id_pesanan)

def generate_id_pesanan():
    nomor_acak = random.randint(100000, 999999)
    id_pesanan = "ORD-" + str(nomor_acak)
    return id_pesanan

distributor = DistribusiBarang()

while True:
    os.system ('cls')
    print("═════════════════════════════")
    print("Distributor Hardware Komputer")
    print("═════════════════════════════")
    print("""
    1. Tambah Pesanan 
    2. Lihat Pesanan
    3. Perbarui Pesanan
    4. Hapus Pesanan
    5. Keluar
    """)
    print("═════════════════════════════")

    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        distributor.tambah_pesanan()
    elif pilihan == "2":
        os.system('cls')
        print("""
        ╔═════════════════════════════╗
         Sedang menampilkan pesanan...
        ╚═════════════════════════════╝
        """)
        time.sleep(2)
        distributor.lihat_pesanan()
    elif pilihan == "3":
        os.system('cls')
        distributor.lihat_pesanan()
        id_pesanan = input("Masukkan ID Pesanan yang ingin diperbarui: ")
        distributor.perbarui_barang(id_pesanan)
    elif pilihan == "4":
        os.system('cls')
        distributor.lihat_pesanan()
        id_pesanan = input("Masukkan ID Pesanan yang ingin dihapus: ")
        distributor.hapus_pesanan(id_pesanan)
    elif pilihan == "5":
        os.system ('cls')
        print("╔══════════════════════════════════╗")
        print(" Anda Telah keluar dari Program ini ")
        print("╚══════════════════════════════════╝")
        exit()
    else:
        os.system ('cls')
        print("╔═══════════════════╗")
        print(" Opsi Menu tidak ada ")
        print("╚═══════════════════╝")
        a = input("Tekan Enter untuk kembali ke menu sebelumnya")
        if a == "":
            os.system('cls')