from src.data_loader import clean_text

def process_geodata(gdf_indo, df_csv, target_provinsi, col_csv_city):
    """
    Logika utama pengolahan data spasial:
    1. Filter Provinsi
    2. Normalisasi Nama
    3. Join Data
    """
    print(f"[PROCESS] Memfilter wilayah provinsi: {target_provinsi}...")

    # 1. Filter Provinsi (Menggunakan kolom NAME_1)
    if 'NAME_1' not in gdf_indo.columns:
        raise KeyError("Kolom 'NAME_1' (Provinsi) tidak ditemukan di file GeoJSON.")
        
    gdf_filter = gdf_indo[gdf_indo['NAME_1'].str.upper() == target_provinsi].copy()

    if gdf_filter.empty:
        raise ValueError(f"Provinsi '{target_provinsi}' tidak ditemukan di peta!")

    # 2. Normalisasi Key untuk Join
    print("[PROCESS] Melakukan normalisasi nama wilayah...")
    # CSV Key
    df_csv['join_key'] = df_csv[col_csv_city].apply(clean_text)
    # Map Key (Level 4 menggunakan NAME_2 untuk Kabupaten/Kota)
    gdf_filter['join_key'] = gdf_filter['NAME_2'].apply(clean_text)

    # 3. Merge Data (Left Join)
    print("[PROCESS] Menggabungkan data spasial & tabular...")
    merged = gdf_filter.merge(df_csv, on='join_key', how='left')
    
    return merged