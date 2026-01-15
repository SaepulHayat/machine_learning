# 🌋 Disaster Risk Analytics System
### Machine Learning untuk Analisis Risiko Bencana Jawa Barat

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-success.svg)]() 

> **Tim Pengembang:** Saepul, Adit, Defran, Andrew  
> **Institusi:** Universitas Widyatama  
> **Tahun:** 2026

---

##  Deskripsi

Sistem Machine Learning berbasis **K-Means Clustering** untuk mengklasifikasikan 27 kabupaten/kota di Jawa Barat berdasarkan tingkat risiko bencana. Menggunakan 6 indikator bencana (banjir, gempa, longsor, cuaca ekstrem, kerusakan rumah, dan indeks risiko) untuk menghasilkan peta risiko interaktif yang membantu pengambilan keputusan mitigasi bencana.

###  Tujuan Utama
- ✅ **Automated Risk Assessment** - Klasifikasi wilayah secara objektif
- ✅ **Data-Driven Decision Making** - Rekomendasi prioritas berbasis metrik
- ✅ **Visual Communication** - Peta & grafik untuk stakeholder non-teknis
- ✅ **Scalable Architecture** - Mudah diadaptasi untuk provinsi lain

---

##  Arsitektur Sistem

```
┌─────────────────────────────────────────────────────┐
│               INPUT DATA LAYER                      │
├─────────────────────────────────────────────────────┤
│   6 CSV Files (Bencana)                             │
│   GeoJSON (Peta Indonesia Level 4)                  │
└──────────────────────┬──────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────┐
│            PROCESSING MODULES (src/)                │
├─────────────────────────────────────────────────────┤
│  1️⃣ data_loader.py     → Load & Validate            │
│  2️⃣ clustering.py      → K-Means Algorithm          │
│  3️⃣ evaluator.py       → Performance Metrics        │
│  4️⃣ geo_processor.py   → Spatial Join               │
│  5️⃣ visualizer.py      → Map & Plot Generation      │ 
└──────────────────────┬──────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────┐
│                OUTPUT LAYER                         │
├─────────────────────────────────────────────────────┤
│  🗺️ peta_risiko_final.png   (Choropleth Map)        │
│  📊 plot_pca_cluster.png     (PCA Scatter Plot)     │
│  📋 Console Metrics          (Silhouette, etc.)     │
└─────────────────────────────────────────────────────┘
```

---

##  Struktur Project

```
disaster-risk-analytics/
│
├── dataset/                          # Data mentah
│   ├── banjir.csv                   # Data kejadian banjir
│   ├── gempa.csv                    # Data kejadian gempa
│   ├── longsor.csv                  # Data kejadian longsor
│   ├── cuaca_ekstrem.csv            # Data cuaca buruk
│   ├── kerusakan_rumah.csv          # Data kerusakan properti
│   ├── indeks_risiko.csv            # Indeks risiko per wilayah
│   ├── gadm41_IDN_4.json            # Peta Indonesia Level 4
│   └── master_data_bencana.csv      # Data agregat (hasil preprocessing)
│
├── src/                              # Source code modules
│   ├── __init__.py                  # Package marker
│   ├── data_loader.py               # ✅ Load CSV & GeoJSON
│   ├── clustering.py                # ✅ K-Means implementation
│   ├── evaluator.py                 # ✅ Model evaluation metrics
│   ├── geo_processor.py             # ✅ Spatial data processing
│   └── visualizer.py                # ✅ Map & plot generation
│
├── output/                           # Generated outputs
│   ├── peta_risiko_final.png        # Peta warna risiko
│   └── plot_pca_cluster.png         # Grafik PCA
│
├── main.py                           # 🚀 Entry point (pipeline executor)
├── config.py                         # ⚙️ Configuration settings
├── requirements.txt                  # 📦 Python dependencies
├── DOCUMENTATION.md                  # 📖 Technical documentation
└── README.md                         # 📄 This file

```

---

##  Quick Start

### 1. Instalasi Dependencies

```bash
# Clone repository
git clone https://github.com/your-team/disaster-risk-analytics.git
cd disaster-risk-analytics

# Install required packages
pip install -r requirements.txt
```

**Dependencies:**
```
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
geopandas>=0.13.0
matplotlib>=3.7.0
seaborn>=0.12.0
pyogrio>=0.6.0
```

### 2. Persiapan Data

Pastikan folder `dataset/` berisi:
- ✅ 6 file CSV bencana (dari Open Data Jabar)
- ✅ File `gadm41_IDN_4.json` (peta digital)
- ✅ File `master_data_bencana.csv` (hasil agregasi)

### 3. Jalankan Pipeline

```bash
# Eksekusi pipeline lengkap
python main.py
```

**Output yang dihasilkan:**
```
output/
├── peta_risiko_final.png        ✅ Peta choropleth
└── plot_pca_cluster.png         ✅ Grafik PCA

Terminal:
├── Silhouette Score: 0.47       ✅ Validasi clustering
├── Davies-Bouldin: 0.78         ✅ Kualitas cluster
└── Cluster Profiles             ✅ Statistik per cluster
```

---

##  Metodologi Machine Learning

### K-Means Clustering

**Mengapa K-Means?**
- ✅ Unsupervised Learning (tidak butuh label manual)
- ✅ Menemukan pola alami dalam data
- ✅ Cepat & scalable untuk dataset regional
- ✅ Mudah diinterpretasi oleh stakeholder

**Preprocessing:**
```python
# 1. Feature Selection
features = ['jml_banjir', 'jml_gempa', 'jml_longsor', 
            'jml_cuaca_ekstrem', 'rumah_kerusakan', 'indeks_risiko']

# 2. Standardization (PENTING!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_scaled)
```

**Parameter:**
- `n_clusters=3` → Risiko Tinggi, Sedang, Rendah
- `random_state=42` → Reproducible results
- `n_init=10` → Coba 10 inisialisasi berbeda

---

##  Evaluasi Model

### Metrik Validasi

| Metrik | Nilai | Interpretasi |
|--------|-------|--------------|
| **Silhouette Score** | 0.47 | ✅ Clustering valid (>0.3 = good) |
| **Davies-Bouldin Index** | 0.78 | ✅ Cluster compact (<1.0 = good) |
| **Calinski-Harabasz** | 145.32 | ✅ Separasi jelas (>100 = good) |

### Profil Cluster

```
Cluster 0 (LOW RISK):
  - 8 kabupaten/kota
  - Rata-rata kerusakan: 1,441 unit
  - Contoh: Bekasi, Depok, Karawang
  → Budget: 10% untuk monitoring

Cluster 1 (HIGH RISK):
  - 9 kabupaten/kota  
  - Rata-rata kerusakan: 39,343 unit ⚠️
  - Contoh: Bogor, Garut, Sukabumi
  → Budget: 60% untuk mitigasi prioritas

Cluster 2 (MEDIUM RISK):
  - 10 kabupaten/kota
  - Rata-rata kerusakan: 5,000 unit
  - Contoh: Bandung, Cirebon, Tasikmalaya
  → Budget: 30% untuk preparedness
```

---

##  Output Visualisasi

### 1. Peta Choropleth
![Peta Risiko](output/peta_risiko_final.png)

**Fitur:**
- 🔴 Merah = Risiko TINGGI (Prioritas)
- 🟡 Kuning = Risiko SEDANG (Waspada)
- 🟢 Hijau = Risiko RENDAH (Monitor)
- ⬜ Abu-abu = Data tidak lengkap

### 2. PCA Scatter Plot
![PCA Plot](output/plot_pca_cluster.png)

**Interpretasi:**
- **PC1 (45%)** → Overall Severity (kanan = parah, kiri = ringan)
- **PC2 (25%)** → Disaster Type Mix
- **Cluster separation** → Pemisahan jelas = clustering valid

---

##  Use Cases

### 1. Pemerintah Daerah (BPBD)
```
✅ Prioritas alokasi anggaran mitigasi
✅ Identifikasi wilayah untuk early warning system
✅ Perencanaan infrastruktur tahan bencana
✅ Pemetaan shelter & evacuation routes
```

### 2. BNPB (Nasional)
```
✅ Pemetaan zona risiko tinggi nasional
✅ Deployment resource dan logistik
✅ Benchmarking antar provinsi
✅ Policy recommendation
```

### 3. Perusahaan Asuransi
```
✅ Risk assessment untuk perhitungan premi
✅ Underwriting decisions
✅ Reinsurance portfolio optimization
✅ Claims prediction
```

---

##  Konfigurasi

Edit file `config.py` untuk customize:

```python
class Config:
    # Data paths
    DATASET_DIR = Path("dataset")
    OUTPUT_DIR = Path("output")
    
    # Target analysis
    TARGET_PROVINCE = "Jawa Barat"
    
    # ML parameters
    N_CLUSTERS = 3
    RANDOM_STATE = 42
    
    # Features
    FEATURES = [
        'jml_banjir',
        'jml_gempa', 
        'jml_longsor',
        'jml_cuaca_ekstrem',
        'rumah_kerusakan',
        'indeks_risiko_bencana'
    ]
```

---

##  Untuk Peneliti

### Ekspansi ke Provinsi Lain

```python
# Ubah target provinsi di config.py
Config.TARGET_PROVINCE = "Jawa Tengah"

# Jalankan pipeline
python main.py

# Otomatis akan filter data untuk provinsi tersebut
```

### Tuning Hyperparameter

```python
# Coba jumlah cluster berbeda
from src.clustering import run_kmeans

for k in range(2, 6):
    df_result, X_scaled = run_kmeans(df, features, n_clusters=k)
    # Analisis metrik untuk setiap k
```

---

##  Limitasi

1. **Analisis Statis** - Tidak memperhitungkan trend temporal
2. **Equal Weight Features** - Semua fitur dianggap sama penting
3. **Manual k Selection** - Jumlah cluster ditentukan manual
4. **Single Province** - Fokus pada Jawa Barat
5. **No External Factors** - Belum include ekonomi, demografi

---

##  Future Work

- [ ] **Time Series Analysis** - Analisis trend tahunan
- [ ] **Weighted Features** - Bobot berbeda per fitur
- [ ] **Auto k-Selection** - Elbow method untuk k optimal
- [ ] **National Scale** - Ekspansi seluruh Indonesia
- [ ] **Deep Learning** - LSTM untuk prediksi risiko
- [ ] **Real-time Dashboard** - Web interface dengan Streamlit
- [ ] **API Endpoint** - REST API untuk integrasi

---

##  Referensi

1. **Data Source**: [Open Data Jabar](https://opendata.jabarprov.go.id/)
2. **GeoJSON**: [GADM Database](https://gadm.org/download_country.html)
3. **Algoritma**: Scikit-learn K-Means Documentation
4. **Spatial Analysis**: GeoPandas Documentation

---

## 👥 Tim Pengembang

| Nama | Role | Kontribusi |
|------|------|------------|
| **Saepul** | Project Lead | System architecture & ML modeling |
| **Adit** | Data Engineer | ETL pipeline & data preprocessing |
| **Defran** | GIS Specialist | Spatial analysis & mapping |
| **Andrew** | ML Engineer | Clustering & evaluation metrics |

---

##  Kontak

Untuk pertanyaan atau kolaborasi:
- 📧 Email: [saepul.hayat@widyatama.ac.id]
- 🌐 Website: [adoyzola.site]
- 💬 GitHub Issues: [Open an issue](https://github.com/your-team/disaster-risk-analytics/issues)

---

##  License

MIT License - lihat file [LICENSE](LICENSE) untuk detail.

---

##  Acknowledgments

Terima kasih kepada:
- **Open Data Jabar** untuk penyediaan dataset bencana
- **GADM** untuk peta digital Indonesia
- **Dosen Pembimbing** atas guidance dan feedback
- **Komunitas Python Indonesia** untuk support

---

<div align="center">

**⭐ Jika project ini bermanfaat, jangan lupa kasih star! ⭐**

Made with ❤️ by **Saepul, Adit, Defran, Andrew**

</div>
