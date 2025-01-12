import os
import array

if __name__ == "__main__":
    sistem_operasi = os.name

    while True:
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("\nCardio Shield: HERALTIS (Heart Health Risk)\n")
        print("         - CARDIO SHIELD -")
        print("-" * 35)
        print("       Welcome To HERALTIS!")
        print("-" * 35)
        print("  Silakan Masukan Data Anda (-^v^-)!")
        print("-" * 35)

        print("\n             Data Pengguna")
        print("-" * 35)
        nama = input("Nama           : ")
        umur = input("Umur           : ")
        jk = input("Jenis Kelamin  : ")
        gd = input("Golongan Darah : ")
        print("-" * 35)

        aktivitas_fisik = []

        def menu0():
            while True:
                print("-" * 35)
                print("         MENU DI HERALTIS")
                print("-" * 35)
                print("-> Aktivitas Fisik                  [1]")
                print("-> Rekomendasi Makanan dan Minuman  [2]")
                print("-> Analisis Resiko                  [3]")
                print("-> Pengelolaan Stress               [4]")
                print("-> SELESAI                          [5]")
                print("-" * 35)
                opsi = input("Masukkan Opsi: ")
                print("-" * 35)

                match opsi:
                    case "1": main()  
                    case "2": menu2()  
                    case "3": menu3()
                    case "4": menu4()
                    case "5":
                        print("Terima Kasih Atas Kunjungan Anda!")
                        return

        def menu1():
            print("\n" + "-" * 35)
            print("         AKTIVITAS FISIK")
            print("-" * 35)
            print("1. Masukkan Aktivitas Fisik")
            print("2. Menampilkan Aktivitas Fisik")
            print("3. Cari Aktivitas Fisik")
            print("4. Kembali ke Menu Utama")
            print("-" * 35)

        def ma_aktivitas_fisik():
            print("\nMasukkan Durasi Aktivitas Harian (Menit) untuk 7 hari")
            print("-" * 56)
            for i in range(7):
                hari = f"Hari ke-{i+1}"
                durasi = int(input(f"Masukkan durasi aktivitas pada {hari} (menit): "))
                jenis = input(f"Masukkan jenis  aktivitas pada {hari}        : ")
                aktivitas_fisik.append({"hari": hari, "durasi": durasi, "jenis": jenis})    

        def me_aktivitas_fisik():
            print("\n  Aktivitas Fisik Mingguan \n")
            total_aktivitas = sum(aktivitas["durasi"] for aktivitas in aktivitas_fisik)
            rata_rata = total_aktivitas / len(aktivitas_fisik) if aktivitas_fisik else 0
            for aktivitas in aktivitas_fisik:
                print(f"{aktivitas['hari']}: {aktivitas['durasi']} menit - {aktivitas['jenis']}")
            print(f"\nTotal aktivitas fisik dalam seminggu: {total_aktivitas} menit")
            print(f"Rata-rata aktivitas per hari: {rata_rata:.2f} menit")

        def ca_aktivitas_fisik():
            kk = input("Masukkan Hari atau Jenis Aktivitas: ")
            found = False
            print("\nHasil Pencarian:")
            for aktivitas in aktivitas_fisik:
                if kk in aktivitas["hari"] or kk in aktivitas["jenis"]:
                    print(f"{aktivitas['hari']}: {aktivitas['durasi']} menit - {aktivitas['jenis']}")
                    found = True
            if not found:
                print("Tidak ada aktivitas yang cocok dengan pencarian")

        def main():
            while True:
                menu1()
                pil = input("Pilih opsi [1-4]: ")
                match pil:
                    case "1": ma_aktivitas_fisik()
                    case "2": me_aktivitas_fisik()
                    case "3": ca_aktivitas_fisik()
                    case "4": 
                        print("Kembali ke Menu Utama ..\n")
                        break

        head = None
        tail = None

        stack_favorit = []
        queue_heraltis = []

        def tambah_data(kategori, sub_kategori, favorit):
            global head, tail
            newNode = {
                "kategori": kategori,
                "sub_kategori": sub_kategori,
                "favorit": favorit,
                "prev": None,
                "next": None
            }
            if head is None:
                head = newNode
                tail = newNode
                head["next"] = head
                head["prev"] = head
            else:
                tail["next"] = newNode
                newNode["prev"] = tail
                newNode["next"] = head
                head["prev"] = newNode
                tail = newNode

        def tampilkan_data():
            global head
            if head is None:
                print("\nBelum ada data yang ditambahkan.")
                return

            print("\n" + "=" * 70)
            print(f"{'Kategori':<20}{'Sub-Kategori':<30}{'Favorit':<20}")
            print("-" * 70)
            current = head
            while True:
                print(f"{current['kategori']:<20}{current['sub_kategori']:<30}{current['favorit']:<20}")
                current = current["next"]
                if current == head:
                    break
            print("=" * 70)

        def tambah_stack(data):
            stack_favorit.append(data)
            
        def tambah_queue(data):
            queue_heraltis.append(data)

        from tabulate import tabulate

        referensi_sub_kategori = [
            {"No": "1", "Kategori": "Makanan", "Sub-Kategori": "Buah", "Contoh": "Apel, Alpukat, Anggur"},
            {"No": "2", "Kategori": "Makanan", "Sub-Kategori": "Karbohidrat", "Contoh": "Nasi Merah"},        
            {"No": "3", "Kategori": "Makanan", "Sub-Kategori": "Protein Hewani", "Contoh": "Ikan Kembung"},
            {"No": "4", "Kategori": "Makanan", "Sub-Kategori": "Protein Nabati", "Contoh": "Tahu"},
            {"No": "5", "Kategori": "Makanan", "Sub-Kategori": "Sayur", "Contoh" : "Brokoli, Kangkung, Bayam, Pak Choy, Asparagus, Tomat dan Sawi Hijau"},
            {"No": "6", "Kategori": "Makanan", "Sub-Kategori": "Cemilan", "Contoh": "Oatmeal dan Yogurt"},
            {"No": "7", "Kategori": "Minuman", "Sub-Kategori": "Dingin", "Contoh": "Air Mineral"},
            {"No": "8", "Kategori": "Minuman", "Sub-Kategori": "Hangat", "Contoh": "Air Mineral"}
        ]

        def tampilan_referensi():
            print("\n|Masukkan Data|")

        table_data = []
        for ref in referensi_sub_kategori:
            table_data.append([ref['No'], ref['Kategori'], ref['Sub-Kategori'], ref['Contoh']])
    
        print(tabulate(table_data, headers=["No", "Kategori", "Sub-Kategori", "Contoh Favorit"], tablefmt="grid"))

        def menu2():
            global head, tail, stack_favorit, queue_heraltis
            while True:
                print("\n" + "-" * 50)
                print("         REKOMENDASI MAKANAN DAN MINUMAN")
                print("-" * 50)
                print("1. Masukkan Kategori")
                print("2. Rekomendasi Dari HERALTIS")
                print("3. Tampilkan Semua Data")
                print("4. Kembali ke Menu Utama")
                print("-" * 50)

                pilihan = input("Pilih opsi [1-4]: ")
                if pilihan == "1":
                    tampilan_referensi()
                    kategori = input("|Pilih Kategori     : ")
                    sub_kategori = input("|Pilih Sub-Kategori : ")
                    favorit = input("|Favorit Anda       : ")
                    tambah_data(kategori, sub_kategori, favorit)
                    tambah_stack(f"{kategori} - {sub_kategori} - {favorit}")
                elif pilihan == "2":
                    if not queue_heraltis:
                        print("Belum ada data rekomendasi dari Heralt is!")
                    else:
                        print("\nRekomendasi dari Heraltis: ")
                        print("=" * 75)
                        while queue_heraltis:
                            print(queue_heraltis.pop(0))
                        print("=" * 75)
                elif pilihan == "3":
                    tampilkan_data()
                elif pilihan == "4":
                    print("\nKembali ke menu utama ..\n")
                    break
                else:
                    print("Pilihan tidak valid. Coba lagi!")

        tambah_queue("Kategori: Minuman - Sub-Kategori: Dingin - Contoh: Air Mineral")
        tambah_queue("Kategori: Makanan - Sub-Kategori: Buah - Contoh: Apel")
        tambah_queue("Kategori: Makanan - Sub-Kategori: Karbohidrat - Contoh: Nasi Merah")       
        tambah_queue("Kategori: Makanan - Sub-Kategori: Protein Hewani - Contoh: Ikan Kembung")
        tambah_queue("Kategori: Makanan - Sub-Kategori: Protein Nabati - Contoh: Tahu")
        tambah_queue("Kategori: Makanan - Sub-Kategori: Sayur - Contoh : Asparagus dan Bayam")
        tambah_queue("Kategori: Makanan - Sub-Kategori: Cemilan - Contoh: Yogurt")
        
        class HealthRiskGraph:
            def __init__(self, nodes):
                self.numNodes = nodes
                self.adjMatrix = [[0.0] * nodes for _ in range(nodes)]  
                self.nodeLabels = [""] * nodes

            def setNodeLabel(self, node, label):
                """Set label for each node"""
                self.nodeLabels[node] = label

            def addEdge(self, u, v, weight):
                """Add a directed edge with weight between two nodes"""
                self.adjMatrix[u][v] = weight

            def printGraph(self):
                """Print the adjacency matrix with labels"""
                print("Adjacency Matrix:")
                print("\t", end="")
                for label in self.nodeLabels:
                    print(f"{label}\t", end="")
                print()

                for i in range(self.numNodes):
                    print(f"{self.nodeLabels[i]}\t", end="")
                    for j in range(self.numNodes):
                        print(f"{self.adjMatrix[i][j]}\t", end="")
                    print()

            def printEdges(self):
                """Print edges with weights"""
                print("Edges and Weights:")
                for i in range(self.numNodes):
                    for j in range(self.numNodes):
                        if self.adjMatrix[i][j] > 0:
                            print(f"{self.nodeLabels[i]} -> {self.nodeLabels[j]} (Weight: {self.adjMatrix[i][j]})")

        def menu3():
            while True:
                print("\n" + "-" * 55)
                print("                   ANALISIS RESIKO")
                print("-" * 55)
                print("1. Resiko Penyakit Jantung")
                print("2. Hubungan Faktor Resiko Penyakit Jantung")
                print("3. Kembali ke Menu Utama")
                print("-" * 55)
                choice = input("Pilih opsi: ")

                if choice == '1':
                    print("Melakukan Analisis Resiko...")

                    pasiens = [
                        {"Nama": "Joshua", "Umur": 45, "Tekanan_Darah": 130, "Kadar Kolesterol": 180},
                        {"Nama": "Mareet", "Umur": 65, "Tekanan_Darah": 150, "Kadar Kolesterol": 220},
                        {"Nama": "Amin", "Umur": 55, "Tekanan_Darah": 145, "Kadar Kolesterol": 210},
                        {"Nama": "Erna", "Umur": 40, "Tekanan_Darah": 120, "Kadar Kolesterol": 170},
                        {"Nama": "Loak", "Umur": 70, "Tekanan_Darah": 160, "Kadar Kolesterol": 230},
                    ]

                    def analisis_resiko(umur, tekanan_darah, kolesterol):
                        if umur > 50:
                            if tekanan_darah > 140:
                                if kolesterol > 200:
                                    return "Resiko [High] Penyakit Jantung"
                                else:
                                    return "Resiko [Medium] Penyakit Jantung"
                            else:
                                return "Resiko [Medium] Penyakit Jantung"
                        else:
                            if tekanan_darah > 140 or kolesterol > 200:
                                return "Resiko [Medium] Penyakit Jantung"
                            else:
                                return "Resiko [Low] Penyakit Jantung"

                    results = []
                    for pasien in pasiens:
                        risk = analisis_resiko(pasien["Umur"], pasien["Tekanan_Darah"], pasien["Kadar Kolesterol"])
                        results.append({"Nama": pasien["Nama"], "Resiko": risk})

                    def sort_results(results, order="ascending"):
                        risk_order = {
                            "Resiko [Low] Penyakit Jantung": 1,
                            "Resiko [Medium] Penyakit Jantung": 2,
                            "Resiko [High] Penyakit Jantung": 3
                        }
                        
                        if order == "descending":
                            reverse = True
                        else:
                            reverse = False  
                        return sorted(results, key=lambda x: risk_order[x["Resiko"]], reverse=reverse)

                    order = input("Pilih urutan (ascending/descending): ").strip().lower()

                    if order not in ['ascending', 'descending']:
                        print("Input tidak valid, menggunakan urutan default ascending.")
                        order = 'ascending'  

                    sorted_results = sort_results(results, order)

                    print("=" * 55)
                    print("\nHasil Analisis Risiko Penyakit Jantung: ")
                    print("=" * 55)
                    for result in sorted_results:
                        print(f"Nama: {result['Nama']}, Resiko: {result['Resiko']}")
                        print("-" * 55)

                elif choice == '2':
                    print("Hubungan Faktor Resiko Penyakit Jantung...")

                    nodes = 5  
                    graph = HealthRiskGraph(nodes)

                    graph.setNodeLabel(0, "Merokok")
                    graph.setNodeLabel(1, "Obesitas")
                    graph.setNodeLabel(2, "Tekanan Darah Tinggi")
                    graph.setNodeLabel(3, "Kolesterol Tinggi")
                    graph.setNodeLabel(4, "Serangan Jantung")

                    graph.addEdge(0, 2, 0.8)  # Merokok -> Tekanan Darah Tinggi
                    graph.addEdge(1, 3, 0.7)  # Obesitas -> Kolesterol Tinggi
                    graph.addEdge(2, 4, 0.9)  # Tekanan Darah Tinggi -> Serangan Jantung
                    graph.addEdge(3, 4, 0.85)  # Kolesterol Tinggi -> Serangan Jantung

                    graph.printGraph()
                    print()
                    graph.printEdges()

                elif choice == '3':
                    print("Kembali ke Menu Utama ..")
                    break
                else:
                    print("Pilihan tidak valid, silakan coba lagi.")

        def menu4():
            class StressManagementTree:
                def __init__(self):
                    self.tree = {
                        "Teknik Relaksasi": ["Meditasi", "Bernapas Dalam dan Yoga."],
                        "Tidur Cukup": ["Tidur 7-8 Jam Sehari", "Tidur tanpa gangguan."],
                        "Aktivitas Sosial": ["Interaksi dengan keluarga dan berkumpul dengan teman."],
                        "Manajemen Waktu": ["Prioritaskan tugas dan jadwalkan waktu untuk diri sendiri."],
                    }

                def show_options(self, category):
                    return self.tree.get(category, [])

            def menu_stress_management():
                stress_tree = StressManagementTree()
                categories = list(stress_tree.tree.keys())

                while True:
                    print("\n" + "-" * 50)
                    print("               Menu Pengelolaan Stres")
                    print("-" * 50)
                    for i, category in enumerate(categories, 1):
                        print(f"{i}. {category}")
                    print("5. Kembali ke Menu Utama")
                    print("-" * 50)
                    choice = input("Pilih opsi [1-5]: ")
                    if choice == "5":
                        break
                    elif choice in map(str, range(1, 5)):
                        category = categories[int(choice) - 1]
                        options = stress_tree.show_options(category)
                        print("\n" + "-" * 80)
                        print(f"{category}: {', '.join(options)}")
                        print("-" * 80)
                    else:
                        print("Pilihan tidak valid.")

            menu_stress_management()

        if __name__ == "__main__":
            menu0()                                           
