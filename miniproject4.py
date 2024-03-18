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

    def quick_sort(self, arr, attribute, pesanan):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x.data[attribute] < pivot.data[attribute] or (x.data[attribute] == pivot.data[attribute] and x.data['id_pesanan'] < pivot.data['id_pesanan'])]
        middle = [x for x in arr if x.data[attribute] == pivot.data[attribute]]
        right = [x for x in arr if x.data[attribute] > pivot.data[attribute] or (x.data[attribute] == pivot.data[attribute] and x.data['id_pesanan'] > pivot.data['id_pesanan'])]

        if pesanan == "ascending":
            return self.quick_sort(left, attribute, pesanan) + middle + self.quick_sort(right, attribute, pesanan)
        else:
            return self.quick_sort(right, attribute, pesanan) + middle + self.quick_sort(left, attribute, pesanan)

    def jump_search(self, key, attribute='id_pesanan'):
        if not self.head:
            return None
        
        n = 0
        current = self.head
        while True:
            n += 1
            current = current.next
            if current == self.head:
                break

        step = int(n ** 0.5)
        prev = None
        while True:
            for i in range(min(step, n)):
                if attribute == 'id_pesanan':
                    if current.data[attribute] == key:
                        return current.data
                elif attribute in current.data and current.data[attribute] == key:
                    return current.data
                prev = current
                current = current.next
            n -= step
            if n <= 0:
                break
        return None


    def get_list(self):
        if not self.head:
            return []
        current = self.head
        node_list = []
        while True:
            node_list.append(current)
            current = current.next
            if current == self.head:
                break
        return node_list
        
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
            os.system("cls")
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
        os.system("cls")
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
                return []
        current = self.head
        node_list = []
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
        while True:
            print("Menu Tambah Pesanan:")
            print("1. Tambah di Awal")
            print("2. Tambah di Akhir")
            print("3. Tambah di Tengah")
            
            pilihan = input("Pilih tempat penambahan pesanan: ")
            if pilihan == "1" or pilihan == "2" or pilihan == "3":
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
                if pilihan == "1":
                    self.tambah_diawal(pesanan)
                elif pilihan == "2":
                    self.tambah_diakhir(pesanan)
                else:
                    id_setelahnya = input("Masukkan ID Pesanan setelahnya: ")
                    self.tambah_ditengah(pesanan, id_setelahnya)
                break
            else:
                print("Opsi tidak valid.")
                a = input("Tekan Enter untuk kembali ke menu sebelumnya")
                if a == "":
                    os.system('cls')

    def lihat_pesanan(self, sorted_pesanan=None):
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
                if sorted_pesanan:
                    os.system ("cls")
                    print("Pesanan setelah diurutkan:")
                    for pesanan in sorted_pesanan:
                        print("ID Pesanan:", pesanan.data['id_pesanan'])
                        print("Nama Barang:", pesanan.data['nama_barang'])
                        print("Model Seri:", pesanan.data['model_seri'])
                        print("Nama Costumer:", pesanan.data['nama_costumer'])
                        print("Alamat:", pesanan.data['alamat'])
                        print("Kuantitas Barang:", pesanan.data['kuantitas'])
                        print("-------------------------------------------")
                else:
                    while True:
                        print("╔════════════╗")
                        print(" Menu Pesanan ")
                        print("╚════════════╝")
                        print ("1. Sorting Pesanan")
                        print ("2. Searching Pesanan")
                        print ("3. Kembali Ke Menu Awal")
                        pilihan = input ("Pilih Opsi Menu : ")
                        if pilihan == "1":
                            self.sort_pesanan()
                        elif pilihan == "2":
                            self.search_pesanan()
                        elif pilihan == "3":
                            return
                        else:
                            print("Opsi tidak valid.")
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
    
    def sort_pesanan_ascending(self):
        os.system("cls")
        pesanan_list = self.get_list()
        sorted_pesanan = self.quick_sort(pesanan_list, 'id_pesanan', 'ascending')
        self.lihat_pesanan(sorted_pesanan)

    def search_pesanan(self):
        os.system("cls")
        print("Menu Pencarian Pesanan:")
        print("1. Search Berdasarkan Order ID")
        print("2. Search Berdasarkan Nama Costumer")
        print("3. Search Berdasarkan Nama Barang")
        print("4. Kembali ke Menu Pesanan")

        choice = input("Pilih opsi pencarian: ")
        if choice == "1":
            id_pesanan = input("Masukkan Order ID yang ingin dicari: ")
            result = self.jump_search(id_pesanan)
            if result:
                os.system("cls")
                print("Pesanan ditemukan:")
                print("ID Pesanan:", result['id_pesanan'])
                print("Nama Barang:", result['nama_barang'])
                print("Model Seri:", result['model_seri'])
                print("Nama Costumer:", result['nama_costumer'])
                print("Alamat:", result['alamat'])
                print("Kuantitas Barang:", result['kuantitas'])
                print("-------------------------------------------")
            else:
                print("Pesanan tidak ditemukan.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
        elif choice == "2":
            nama_costumer = input("Masukkan Nama Costumer yang ingin dicari: ")
            result = self.jump_search(nama_costumer, attribute='nama_costumer')
            if result:
                os.system("cls")
                print("Pesanan ditemukan:")
                print("ID Pesanan:", result['id_pesanan'])
                print("Nama Barang:", result['nama_barang'])
                print("Model Seri:", result['model_seri'])
                print("Nama Costumer:", result['nama_costumer'])
                print("Alamat:", result['alamat'])
                print("Kuantitas Barang:", result['kuantitas'])
                print("-------------------------------------------")
            else:
                print("Pesanan tidak ditemukan.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
        elif choice == "3":
            nama_barang = input("Masukkan Nama Barang yang ingin dicari: ")
            result = self.jump_search(nama_barang, attribute='nama_barang')
            if result:
                os.system("cls")
                print("Pesanan ditemukan:")
                print("ID Pesanan:", result['id_pesanan'])
                print("Nama Barang:", result['nama_barang'])
                print("Model Seri:", result['model_seri'])
                print("Nama Costumer:", result['nama_costumer'])
                print("Alamat:", result['alamat'])
                print("Kuantitas Barang:", result['kuantitas'])
                print("-------------------------------------------")
            else:
                print("Pesanan tidak ditemukan.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
        elif choice == "4":
            return
        else:
            print("Opsi tidak valid.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')

    def sort_pesanan(self):
        if not self.head:
            os.system("cls")
            print("Tidak ada pesanan untuk diurutkan.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
            return
        os.system("cls")
        print("╔═════════════════════╗")
        print(" Menu Sorting Pesanan:")
        print("╚═════════════════════╝")
        print("1. Sorting berdasarkan Nama Barang")
        print("2. Sorting berdasarkan Nama Costumer")
        print("3. Kembali ke Menu Utama")
        
        choice = input("Pilih opsi: ")
        if choice == "1":
            os.system("cls")
            order = input("Pilih urutan (ascending/descending): ").lower()
            pesanan_list = self.get_list()
            sorted_pesanan = self.quick_sort(pesanan_list, 'nama_barang', order)
            self.lihat_pesanan(sorted_pesanan)
        elif choice == "2":
            os.system("cls")
            order = input("Pilih urutan (ascending/descending): ").lower()
            pesanan_list = self.get_list()
            sorted_pesanan = self.quick_sort(pesanan_list, 'nama_costumer', order)
            self.lihat_pesanan(sorted_pesanan)
        elif choice == "3":
            print("Kembali ke Menu Utama.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')
            return
        else:
            print("Opsi tidak valid.")
            a = input("Tekan Enter untuk kembali ke menu sebelumnya")
            if a == "":
                os.system('cls')

def generate_id_pesanan():
    nomor_acak = random.randint(100000, 999999)
    id_pesanan = "ORD-" + str(nomor_acak)
    return id_pesanan

distributor = DistribusiBarang()
#Record Data
distributor.tambah_diakhir({
    "id_pesanan": "ORD-123456",
    "nama_barang": "Keyboard Gaming",
    "model_seri": "KB-G123",
    "nama_costumer": "Cici",
    "alamat": "Jl. Raya No. 123",
    "kuantitas": 20,
})

distributor.tambah_diakhir({
    "id_pesanan": "ORD-234567",
    "nama_barang": "Mouse Wireless",
    "model_seri": "MS-W456",
    "nama_costumer": "Amir",
    "alamat": "Jl. Cemara No. 456",
    "kuantitas": 11,
})

distributor.tambah_diakhir({
    "id_pesanan": "ORD-345678",
    "nama_barang": "Monitor LED",
    "model_seri": "MN-L789",
    "nama_costumer": "Arey",
    "alamat": "Jl. Mangga No. 789",
    "kuantitas": 31,
})

distributor.tambah_diakhir({
    "id_pesanan": "ORD-456789",
    "nama_barang": "Headset Gaming",
    "model_seri": "HS-G012",
    "nama_costumer": "Ney",
    "alamat": "Jl. Anggrek No. 012",
    "kuantitas": 24,
})

distributor.tambah_diakhir({
    "id_pesanan": "ORD-567890",
    "nama_barang": "Webcam HD",
    "model_seri": "WC-H345",
    "nama_costumer": "Rizky",
    "alamat": "Jl. Dahlia No. 345",
    "kuantitas": 10,
})


# Memulai menu
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