# Pertemuan 07 — Fungsi Python

| **Keterangan** | **Data** |
|---|---|
| **Nama** | Mafatihun Nabila |
| **NIM** | 2225250198 |
| **Kelas** | 3-B |
| **Jurusan** | Pendidikan Matematika |

## Tujuan

Menggunakan fungsi, parameter, `return value`, dan *scope* untuk membuat program Python yang modular. Praktik ini menerapkan fungsi pada beberapa perhitungan matematika sederhana sehingga kode lebih terstruktur, mudah dibaca, diuji, dan digunakan kembali.

## Struktur Proyek

```text
pertemuan-07-fungsi-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_salam.py
│   ├── 02_luas_persegi_panjang.py
│   ├── 03_jumlah_n.py
│   ├── 04_statistik_sederhana.py
│   └── 05_scope.py
└── praktik/
    └── utilitas_matematika.py
```

## Cara Menjalankan

**Melalui Pydroid 3:** Buka berkas `praktik/utilitas_matematika.py`, lalu tekan tombol **Run**. Pilih operasi dengan memasukkan angka pada menu.

**Melalui terminal (Python 3):** Jalankan perintah berikut dari folder utama proyek:

```bash
python3 praktik/utilitas_matematika.py
```

Untuk mencoba latihan, buka masing-masing berkas pada folder `latihan/` dan jalankan secara terpisah.

## Struktur Fungsi

Fungsi pada program utama `praktik/utilitas_matematika.py`:

| Nama fungsi | Parameter | Kegunaan | Nilai `return` |
|---|---|---|---|
| `luas_persegi_panjang(p, l)` | `p`: panjang, `l`: lebar | Menghitung luas persegi panjang | `p * l` |
| `luas_segitiga(a, t)` | `a`: alas, `t`: tinggi | Menghitung luas segitiga | `0.5 * a * t` |
| `jumlah_n(n)` | `n`: batas penjumlahan | Menjumlahkan bilangan dari 1 sampai n menggunakan perulangan | `total` |
| `faktorial(n)` | `n`: bilangan yang dihitung | Menghitung faktorial menggunakan perulangan | `hasil` |
| `tampilkan_menu()` | Tidak ada | Menampilkan pilihan operasi | Tidak ada (`None` secara implisit) |

Program utama menggunakan menu untuk memilih fungsi yang dipanggil. Input `n` pada operasi jumlah dan faktorial diperiksa agar berupa bilangan bulat nonnegatif.

## Hasil Pengujian

Tabel berikut memuat **hasil yang diharapkan** dan **hasil sesuai kode**. Isi kolom hasil aktual serta status setelah menjalankan setiap pengujian di Pydroid 3.

| Operasi | Input | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---:|---|---|
| Luas persegi panjang | `p = 8`, `l = 5` | `40` | Belum dicatat | Belum diuji |
| Luas segitiga | `a = 10`, `t = 6` | `30.0` | Belum dicatat | Belum diuji |
| Jumlah 1 sampai n | `n = 10` | `55` | Belum dicatat | Belum diuji |
| Faktorial | `n = 5` | `120` | Belum dicatat | Belum diuji |
| Faktorial | `n = 0` | `1` | Belum dicatat | Belum diuji |

**Pengujian tambahan:** coba masukkan nilai `n` negatif dan input yang bukan bilangan bulat pada menu jumlah maupun faktorial. Pastikan program menampilkan pesan kesalahan yang sesuai.

## Refleksi

Bagian perhitungan menjadi lebih sederhana setelah dipisahkan menjadi fungsi. Rumus luas, penjumlahan, dan faktorial cukup ditulis satu kali, sedangkan program utama hanya menerima input, memilih operasi, dan menampilkan hasil. Penggunaan parameter membuat fungsi dapat menerima nilai berbeda, sementara `return` memungkinkan hasil perhitungan digunakan kembali.

## Exit Ticket

1. **Satu alasan utama menggunakan fungsi:** agar kode yang memiliki tugas tertentu dapat digunakan kembali tanpa menulis proses yang sama berulang kali.
2. **Satu kesalahan yang saya temukan terkait parameter atau return:** perlu membedakan `print()` yang hanya menampilkan hasil dengan `return` yang mengirimkan nilai kembali kepada pemanggil fungsi.
3. **Materi Pertemuan 1–7 yang perlu saya ulang untuk UTS:** perulangan, *nested loop*, fungsi, parameter, `return value`, dan *scope* variabel.