# Proyek Analisis Data — Beijing Air Quality (PM2.5)

Proyek akhir kelas **Belajar Fundamental Analisis Data** (Dicoding). Menggunakan **seluruh 12 file CSV PRSA Beijing Multi-Site Air Quality** periode 1 Maret 2013–28 Februari 2017 untuk menjawab dua pertanyaan SMART tentang variasi konsentrasi PM2.5 antarlokasi dan menurut bulan kalender. Terdapat analisis lanjutan **binning kuartil** tanpa machine learning.

## Struktur

```text
submission/
├── data/                      # 12 CSV asli
├── dashboard/
│   ├── dashboard.py           # Streamlit
│   └── main_data.csv          # pengamatan PM2.5 yang telah dibersihkan
├── notebook.ipynb             # mengikuti template resmi Dicoding
├── requirements.txt
└── README.md
```

## Setup dan menjalankan dashboard lokal

Pastikan **Python 3.10 atau lebih baru** terpasang, lalu dari folder root proyek:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run dashboard/dashboard.py
```

Buka alamat lokal yang ditampilkan Streamlit, biasanya `http://localhost:8501`.

## Menjalankan ulang notebook

Notebook final `notebook.ipynb` berasal dari berkas final pemilik proyek dan disertakan tanpa perubahan.
Buka dengan Google Colab atau Jupyter, instal dependensi yang dibutuhkan dengan
`pip install -r requirements.txt`, lalu jalankan sel secara berurutan.

Pada tahap **Gathering Data**, notebook mengunduh arsip dataset melalui `gdown`
(dari tautan Google Drive Dicoding) dan membaca 12 CSV langsung dari ZIP tanpa
mengekstraknya secara manual. **Akses internet diperlukan ketika menjalankan
bagian ini pertama kali**. Jika arsip `air_quality.zip` sudah berada di direktori
kerja, notebook dapat menggunakannya kembali.

Folder `data/` berisi 12 CSV asli tetap disertakan untuk memenuhi persyaratan
submission Dicoding dan dokumentasi sumber data.
Notebook menuliskan `dashboard/main_data.csv`, jadi jalankan notebook dari root
proyek agar file dashboard tetap di lokasi yang benar.

## Pertanyaan bisnis

1. Rata-rata PM2.5 tertinggi di stasiun mana selama Mar 2013–Feb 2017, sebagai masukan prioritas pemantauan?
2. Bulan kalender apa yang memiliki rata-rata PM2.5 tertinggi sepanjang periode yang sama, sebagai masukan prioritas pemantauan musiman?

## Teknik dan kehati-hatian data

- `PM2.5` hilang: pengamatan dikeluarkan, tidak dilakukan imputasi.
- Nilai ekstrem ditandai berdasarkan IQR dan dipertahankan karena dapat mencerminkan peristiwa polusi yang nyata.
- Ketidaksesuaian sebagian pasangan `PM10 < PM2.5` dicatat sebagai isu kualitas, tetapi PM10 tidak dipakai dalam indikator atau kesimpulan. Tidak dipastikan variabel mana yang bermasalah.
- Binning Q1–Q4 menggunakan kuartil **global sampel asli yang valid**; ini kategori relatif, **bukan ambang resmi AQI atau kesehatan**.
- Rata-rata adalah rata-rata pengamatan yang tersedia, bukan nilai populasi yang bebas bias missing.
- Tidak menggunakan algoritma machine learning. Hasil tidak menunjukkan hubungan kausal maupun kualitas udara saat ini.

## Deployment Streamlit Community Cloud — perlu dikerjakan pemilik akun

1. Push isi root folder proyek ke repositori GitHub milik Anda (perhatikan ukuran file dan kebijakan repositori).
2. Buka https://share.streamlit.io/ kemudian login dan pilih **Create app / Deploy**.
3. Pilih repositori, branch, dan file utama `dashboard/dashboard.py`.
4. Tunggu aplikasi dibangun dan periksa semua grafik dengan berbagai filter.
5. **Setelah berhasil**, buat file `url.txt` di root berisi URL aplikasi yang benar-benar aktif, lalu masukkan ke ZIP submission sesuai instruksi Dicoding.

`url.txt` tidak disertakan karena belum ada URL deployment nyata. Jangan mengirim URL contoh atau mengklaim aplikasi sudah online. Kriteria nilai 5 bintang mensyaratkan deployment nyata.

## Pra-submission

- [ ] Ganti **[ISI USERNAME DICODING ANDA]** pada sel pertama notebook.
- [ ] Pastikan nama/email identitas sesuai akun Anda.
- [ ] Buka notebook dan baca seluruh insight dan keputusan cleaning.
- [ ] Jalankan ulang notebook sampai semua sel berhasil.
- [ ] Jalankan dashboard lokal dan uji filter tanggal/stasiun serta ekspor.
- [ ] Deploy Streamlit Cloud jika mengejar 5 bintang dan buat `url.txt` yang berisi URL asli.
- [ ] ZIP folder beserta CSV, notebook, dashboard, requirements, dan README.

**Dataset:** Air Quality Dataset yang disediakan dalam halaman proyek akhir Dicoding; CSV PRSA Multi-Station Beijing. **Penulis notebook:** Asta Destian Yudha Praja.
