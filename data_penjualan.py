import pandas as pd
import matplotlib.pyplot as plt

# Muat kembali dataframe dari file CSV
df = pd.read_csv(r'C:\data saya\latihan python\berisi.Csv\data_penjualan.csv')

# Hitung kembali kolom 'total_penjualan'
df['total_penjualan'] = df['jumlah_penjualan'] * df['harga_satuan']

# Lakukan pengelompokan (grouping) untuk mendapatkan total penjualan per produk
df_grouped = df.groupby('nama_produk')['total_penjualan'].sum().reset_index()

# Buat bar chart
plt.figure(figsize=(10, 6))
plt.bar(df_grouped['nama_produk'], df_grouped['total_penjualan'], color='skyblue')

# Tambahkan label dan judul
plt.xlabel('Nama Produk')
plt.ylabel('Total Penjualan (Rp)')
plt.title('Total Penjualan per Produk')
plt.xticks(rotation=45)
plt.tight_layout()

# Simpan grafik ke file
plt.savefig('total_penjualan_per_produk.png')

print("Bar chart telah disimpan ke file 'total_penjualan_per_produk.png'")