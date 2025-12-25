import sys
import config
from src import data_loader, geo_processor, visualizer

def main():
    print("="*50)
    print("   SISTEM ANALISIS GEOSPASIAL RISIKO BENCANA")
    print("="*50)
    
    try:
        # 1. LOAD DATA
        df_risk, gdf_raw = data_loader.load_data(
            config.PATH_CSV, 
            config.PATH_PETA
        )

        # 2. PROCESS & FILTER
        gdf_final = geo_processor.process_geodata(
            gdf_raw, 
            df_risk, 
            config.TARGET_PROVINSI,
            config.KOLOM_KOTA_CSV
        )

        # 3. VISUALIZE
        visualizer.generate_map(
            gdf_final, 
            config.PATH_OUTPUT, 
            config.KOLOM_RISIKO,
            config.TARGET_PROVINSI
        )

    except Exception as e:
        print(f"\n[CRITICAL ERROR] Terjadi kesalahan sistem:")
        print(f"{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()