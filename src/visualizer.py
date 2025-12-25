import matplotlib.pyplot as plt

def generate_map(gdf_merged, output_path, col_risk, prov_name):
    """
    Fungsi khusus untuk visualisasi peta choropleth.
    """
    print("[VISUAL] Sedang me-render peta...")
    
    # Setup Kanvas
    fig, ax = plt.subplots(figsize=(14, 10))

    # Plotting Data
    gdf_merged.plot(
        column=col_risk,
        cmap='RdYlGn_r',      # Merah (Tinggi) -> Hijau (Rendah)
        linewidth=0.1,        # Garis batas tipis agar rapi
        edgecolor='gray',
        legend=True,
        missing_kwds={
            "color": "whitesmoke",
            "label": "Data Tidak Tersedia"
        },
        legend_kwds={
            'title': "Tingkat Risiko",
            'loc': 'lower right'
        },
        ax=ax
    )

    # Menambahkan Judul & Kosmetik
    ax.set_title(f"Peta Risiko Bencana: {prov_name}\n(Visualisasi Level Desa/Kelurahan)", 
                    fontsize=16, pad=15)
    ax.set_axis_off() # Hilangkan koordinat X/Y

    # Simpan Gambar
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    print(f"[SUCCESS] Gambar berhasil disimpan di:\n          {output_path}")