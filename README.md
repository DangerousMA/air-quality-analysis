# Beijing Air Quality Dashboard ✨

**Final Project — Belajar Fundamental Analisis Data (Dicoding)**  
**Nama:** Asta Destian Yudha Praja  
**Dataset:** PRSA Multi-Site Air Quality, Beijing (1 Maret 2013–28 Februari 2017)

**Dashboard:** [Air Quality Analysis — Streamlit](https://air-quality-analysis-asta.streamlit.app/)  
**Repository:** [DangerousMA/air-quality-analysis](https://github.com/DangerousMA/air-quality-analysis)

## Setup Environment - Anaconda

Jalankan perintah di bawah ini dari folder utama proyek yang berisi `requirements.txt`.

```bash
conda create --name air-quality python=3.11 -y
conda activate air-quality
python -m pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

Jika tidak menggunakan Anaconda, buat lingkungan Python virtual. Jalankan dari folder utama proyek.

**Windows (Command Prompt):**

```bat
py -3.11 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

**Windows (PowerShell):**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
## Run Streamlit App

Jalankan dari **folder utama proyek**:

```bash
python -m streamlit run dashboard/dashboard.py
```

Dashboard akan terbuka melalui alamat lokal yang ditampilkan terminal, biasanya **http://localhost:8501**.

**Dashboard online:** https://air-quality-analysis-asta.streamlit.app/

## Deskripsi Proyek

Proyek ini menganalisis **konsentrasi PM2.5 (µg/m³)** dari 12 stasiun kualitas udara Beijing menggunakan 12 file CSV yang disediakan Dicoding. Tahapan analisis mencakup data gathering, assessing, cleaning, exploratory data analysis (EDA), visualisasi, kesimpulan, dan rekomendasi tindakan. Hasil analisis disajikan melalui dashboard interaktif Streamlit.

### Pertanyaan Bisnis

1. Selama **1 Maret 2013–28 Februari 2017**, bagaimana peringkat rata-rata PM2.5 pada 12 stasiun Beijing, dan stasiun mana yang perlu diprioritaskan untuk pemantauan lanjutan?
2. Selama periode yang sama, bagaimana rata-rata PM2.5 menurut **bulan kalender**, dan pada bulan apa perhatian pemantauan dapat diprioritaskan?

### Ringkasan Hasil

- Jumlah data awal: **420.768** pengamatan per jam dari 12 stasiun.
- Setelah mengeluarkan data PM2.5 yang hilang, tersedia **412.029** pengamatan PM2.5 valid.
- Rata-rata PM2.5 tertinggi berdasarkan stasiun: **Dongsi (86,19 µg/m³)**; terendah: **Dingling (65,99 µg/m³)**.
- Rata-rata PM2.5 gabungan periode tertinggi berdasarkan bulan kalender: **Desember (104,58 µg/m³)**.
- Analisis lanjutan menggunakan **binning kuartil** (`pandas.cut`) untuk memetakan distribusi konsentrasi relatif antarstasiun, **tanpa machine learning**.

## Fitur Dashboard

- Filter stasiun dan rentang tanggal.
- Ringkasan PM2.5 serta jumlah pengamatan valid.
- Grafik perbandingan rata-rata PM2.5 antarstasiun.
- Grafik pola PM2.5 berdasarkan bulan kalender dan tren harian.
- Komposisi konsentrasi PM2.5 berdasarkan kelompok kuartil relatif.
- Tabel ringkasan dan fitur unduh hasil filter ke CSV.

## Project Structure

```text
submission/
├── dashboard/
│   ├── dashboard.py          # Aplikasi Streamlit
│   └── main_data.csv         # Data hasil cleaning untuk dashboard
├── data/
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv
│   ├── PRSA_Data_Changping_20130301-20170228.csv
│   └── ... 10 CSV stasiun lainnya
├── notebook.ipynb            # Notebook analisis dengan output tersimpan
├── README.md                 # Panduan proyek dan cara menjalankan dashboard
├── requirements.txt          # Library Python yang diperlukan
└── url.txt                   # Tautan publik dashboard Streamlit
```

## Menjalankan Notebook

1. Buka `notebook.ipynb` pada Google Colab atau Jupyter Notebook.
2. Instal dependensi yang diperlukan.
3. Jalankan seluruh sel notebook secara berurutan.
4. Notebook ini menggunakan **`gdown`** untuk mengunduh arsip data dari Google Drive dan `zipfile` untuk membaca CSV dari dalamnya, sehingga memerlukan internet pada tahap *gathering*. Dua belas CSV asli tetap disertakan pada folder `data/` untuk memenuhi ketentuan submission Dicoding.

## Deployment Streamlit Cloud

| Pengaturan | Nilai |
|---|---|
| Repository | `DangerousMA/air-quality-analysis` |
| Branch | `main` |
| Main file path | `dashboard/dashboard.py` |
| URL | `https://air-quality-analysis-asta.streamlit.app/` |

Link yang sama disimpan dalam file `url.txt` untuk kebutuhan submission.

## Sumber Data

- [Air Quality Dataset — Dicoding](https://drive.google.com/file/d/1RhU3gJlkteaAQfyn9XOVAz7a5o1-etgr/view)
- PRSA Multi-Site Air Quality, Beijing, 2013–2017.

---

Dibuat sebagai tugas akhir kelas **Belajar Fundamental Analisis Data — Dicoding**.
