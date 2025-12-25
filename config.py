"""
Konfigurasi Global Proyek
Lead Architect: [Nama Kamu]
"""
from pathlib import Path

# 1. PATH SYSTEM (Otomatis deteksi lokasi file)
BASE_DIR = Path(__file__).resolve().parent

# Input Files
PATH_PETA = BASE_DIR / "dataset" / "gadm41_IDN_4.json"
# CSV hasil clustering tersimpan di output; sesuaikan bila dipindah ke folder lain
PATH_CSV  = BASE_DIR / "output" / "hasil_clustering.csv"

# Output Files
PATH_OUTPUT = BASE_DIR / "output" / "peta_risiko_final.png"

# 2. PARAMETER ANALISIS
# Ubah ini sesuai kebutuhan tim
TARGET_PROVINSI = "JAWA BARAT"       # Filter wilayah biar ringan
KOLOM_RISIKO    = "kategori_risiko"  # Nama kolom cluster di CSV
KOLOM_KOTA_CSV  = "nama_kabupaten_kota" # Nama kolom kota di CSV