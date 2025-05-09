dataSiswaSiswi = {
    1001: {"nis": 1001, "nama": "Matthew", "nilai": 85, "kelas": "12A", "jurusan": "IPA"},
    1002: {"nis": 1002, "nama": "Joshua", "nilai": 90, "kelas": "11B", "jurusan": "IPS"},
    1003: {"nis": 1003, "nama": "Gloria", "nilai": 78, "kelas": "10C", "jurusan": "IPA"},
    1004: {"nis": 1004, "nama": "Ruben", "nilai": 92, "kelas": "12B", "jurusan": "IPS"},
    1005: {"nis": 1005, "nama": "Yolla", "nilai": 88, "kelas": "11C", "jurusan": "IPA"}
}

def konfirmasi(aksi):
    while True:
        konfirmasi = input(f"Apakah Anda yakin ingin {aksi}? [Y/N]: ").upper()
        if konfirmasi == "Y":
            return True
        elif konfirmasi == "N":
            print("Aksi dibatalkan.\n")
            return False
        else:
            print("Input tidak valid. Masukkan Y atau N.")

def inputNIS():
    while True:
        nis = input("Masukkan NIS (angka): ")
        if nis.isdigit():
            return int(nis)
        else:
            print("Hanya angka untuk NIS!")

def addData():
    print("\n=== TAMBAH DATA SISWA/SISWI ===")
    nis = inputNIS()
    if nis in dataSiswaSiswi:
        print("NIS sudah terdaftar.")
        return
    nama = input("Masukkan nama: ")
    nilai = input("Masukkan nilai: ")
    kelas = input("Masukkan kelas: ")
    jurusan = input("Masukkan jurusan (IPA/IPS): ").upper()
    
    if not nilai.isdigit():
        print("Nilai harus berupa angka.")
        return
    if jurusan not in ["IPA", "IPS"]:
        print("Jurusan tidak valid.")
        return

    if konfirmasi("menambahkan data"):
        dataSiswaSiswi[nis] = {"nis": nis, "nama": nama, "nilai": int(nilai), "kelas": kelas, "jurusan": jurusan}
        print("Data berhasil ditambahkan.\n")

def updateData():
    print("\n=== UBAH DATA SISWA/SISWI ===")
    nis = inputNIS()
    if nis not in dataSiswaSiswi:
        print("Data tidak ditemukan.")
        return

    print("Field yang bisa diubah: nama, nilai, kelas, jurusan")
    field = input("Masukkan field yang ingin diubah: ").lower()
    if field not in ["nama", "nilai", "kelas", "jurusan"]:
        print("Field tidak valid.")
        return
    
    new_value = input(f"Masukkan nilai baru untuk {field}: ")
    if field == "nilai" and not new_value.isdigit():
        print("Nilai harus berupa angka.")
        return
    if field == "jurusan" and new_value.upper() not in ["IPA", "IPS"]:
        print("Jurusan tidak valid.")
        return

    if konfirmasi(f"mengubah {field}"):
        if field == "nilai":
            new_value = int(new_value)
        if field == "jurusan":
            new_value = new_value.upper()
        dataSiswaSiswi[nis][field] = new_value
        print("Data berhasil diperbarui.\n")

def deleteData():
    print("\n=== HAPUS DATA SISWA/SISWI ===")
    nis = inputNIS()
    if nis in dataSiswaSiswi:
        if konfirmasi("menghapus data"):
            del dataSiswaSiswi[nis]
            print("Data berhasil dihapus.\n")
    else:
        print("Data tidak ditemukan.")

def showAllData():
    if not dataSiswaSiswi:
        print("Tidak ada data.")
    else:
        print("\n=== DATA SISWA/SISWI ===")
        for nis, info in dataSiswaSiswi.items():
            print(f"NIS: {nis}, Nama: {info['nama']}, Nilai: {info['nilai']}, Kelas: {info['kelas']}, Jurusan: {info['jurusan']}")

def searchByName():
    keyword = input("Masukkan kata kunci nama: ").lower()
    found = False
    for info in dataSiswaSiswi.values():
        if keyword in info["nama"].lower():
            print(f"NIS: {info['nis']}, Nama: {info['nama']}, Nilai: {info['nilai']}, Kelas: {info['kelas']}, Jurusan: {info['jurusan']}")
            found = True
    if not found:
        print("Tidak ada data yang cocok.\n")

def top3Nilai():
    print("\n=== TOP 3 NILAI TERTINGGI ===")
    top_data = sorted(dataSiswaSiswi.values(), key=lambda x: x["nilai"], reverse=True)[:3]
    for info in top_data:
        print(f"{info['nama']} - Nilai: {info['nilai']}")

def rataRataJurusan():
    jurusan = {"IPA": [], "IPS": []}
    for data in dataSiswaSiswi.values():
        jurusan[data["jurusan"]].append(data["nilai"])
    
    print("\n=== RATA-RATA NILAI PER JURUSAN ===")
    for jrs, nilai_list in jurusan.items():
        if nilai_list:
            avg = sum(nilai_list) / len(nilai_list)
            print(f"{jrs}: {avg:.2f}")
        else:
            print(f"{jrs}: Tidak ada data")

def showData():
    while True:
        print("\n=== MENU TAMPILKAN DATA ===")
        print("1. Tampilkan Semua Data")
        print("2. Cari Nama Siswa")
        print("3. Tampilkan Top 3 Nilai")
        print("4. Rata-rata Nilai per Jurusan")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih menu [1-5]: ")
        if pilihan == "1":
            showAllData()
        elif pilihan == "2":
            searchByName()
        elif pilihan == "3":
            top3Nilai()
        elif pilihan == "4":
            rataRataJurusan()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

def home():
    print("\n=== SMA Matthew 18 ===")
    print("Selamat datang di aplikasi Data Nilai Siswa/Siswi SMA Matthew 18\n")

def menu():
    home()
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")
        pilihan = input("Pilih menu [1-5]: ")
        if pilihan == "1":
            showData()
        elif pilihan == "2":
            addData()
        elif pilihan == "3":
            updateData()
        elif pilihan == "4":
            deleteData()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

menu()
