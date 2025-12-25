import pandas as pd
import geopandas as gpd
from pathlib import Path

def clean_text(text):
    """
    Membersihkan teks nama wilayah.
    Contoh: 'Kab. Bandung' -> 'BANDUNG'
    """
    if pd.isna(text): return ""
    
    # Ubah ke uppercase & hapus kata-kata tidak perlu
    text = str(text).upper()
    text = text.replace("KABUPATEN", "").replace("KOTA", "")
    text = text.replace("KAB.", "").replace("ADM.", "")
    
    return text.strip()

def load_data(path_csv, path_peta):
    """
    Membaca file CSV dan GeoJSON dari disk.
    """
    print(f"[LOADER] Memeriksa file...")
    
    if not Path(path_csv).exists():
        raise FileNotFoundError(f"File CSV tidak ditemukan: {path_csv}")
    
    if not Path(path_peta).exists():
        raise FileNotFoundError(f"File Peta tidak ditemukan: {path_peta}")

    print(f"[LOADER] Membaca CSV: {Path(path_csv).name}")
    df = pd.read_csv(path_csv)
    
    print(f"[LOADER] Membaca GeoJSON (Mungkin agak lama)...")
    # Menggunakan engine pyogrio jika tersedia (lebih cepat)
    try:
        gdf = gpd.read_file(path_peta, engine="pyogrio")
    except:
        gdf = gpd.read_file(path_peta) # Fallback ke default
        
    return df, gdf