def luas_persegi_panjang(p, l):
    return p * l

def luas_segitiga(a, t):
    return 0.5 * a * t

def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def tampilkan_menu():
    print("\n" + "=" * 30)
    print("   PROGRAM UTILITAS MATEMATIKA")
    print("=" * 30)
    print("1. Luas Persegi Panjang")
    print("2. Luas Segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")
    print("-" * 30)

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            try:
                p = float(input("Masukkan panjang: "))
                l = float(input("Masukkan lebar: "))
                hasil = luas_persegi_panjang(p, l)
                print(f"-> Luas Persegi Panjang: {hasil}")
            except ValueError:
                print("Error: Masukkan angka yang valid!")
                
        elif pilihan == '2':
            try:
                a = float(input("Masukkan alas: "))
                t = float(input("Masukkan tinggi: "))
                hasil = luas_segitiga(a, t)
                print(f"-> Luas Segitiga: {hasil}")
            except ValueError:
                print("Error: Masukkan angka yang valid!")
                
        elif pilihan == '3':
            try:
                n = int(input("Masukkan nilai n (bilangan bulat nonnegatif): "))
                if n < 0:
                    print("Error: n harus berupa bilangan bulat nonnegatif (>= 0)!")
                else:
                    hasil = jumlah_n(n)
                    print(f"-> Jumlah 1 sampai {n}: {hasil}")
            except ValueError:
                print("Error: Masukkan bilangan bulat yang valid!")
                
        elif pilihan == '4':
            try:
                n = int(input("Masukkan nilai n (bilangan bulat nonnegatif): "))
                if n < 0:
                    print("Error: n harus berupa bilangan bulat nonnegatif (>= 0)!")
                else:
                    hasil = faktorial(n)
                    print(f"-> Faktorial dari {n}: {hasil}")
            except ValueError:
                print("Error: Masukkan bilangan bulat yang valid!")
                
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program utilitas matematika!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1 sampai 5.")

# Menjalankan program utama
if __name__ == "__main__":
    main()