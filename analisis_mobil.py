import pandas as pd
import numpy as np

df = pd.read_csv("C:/data saya/latihan python/berisi.Csv/Cars Datasets 2025.csv",encoding='latin1')

print("Berikut adalah 5 baris pertama dari data mobil:")
print(df.head(15))

print("\nUkuran data (baris, kolom):")
print(df.shape)
print("\n--- Tipe Data Setiap Kolom ---")
print(df.info())

print("\n--- Statistik Dasar ---")
print(df.describe())

#mulai task

print("\n--- Memulai Proses Pembersihan Kolom Harga ---")

harga_bersih = df['Cars Prices'].copy()

harga_bersih = harga_bersih.str.replace('$', '')
harga_bersih = harga_bersih.str.replace(',', '')

def bersihkan_harga(harga_text):
    try:
        harga_str = str(harga_text)
        if '-' in harga_str:
            angka_pertama, angka_kedua = harga_str.split('-')
            return (float(angka_pertama) + float(angka_kedua)) / 2
        elif '/' in harga_str:
            angka_pertama, angka_kedua = harga_str.split('/')
            return (float(angka_pertama.strip()) + float(angka_kedua.strip())) / 2
        else:
            return float(harga_str)
    except ValueError:
        return np.nan

df['Cleaned Prices'] = harga_bersih.apply(bersihkan_harga)

print("...Pembersihan Selesai!")
print("\n--- Perbandingan Kolom Harga Asli dan Harga Bersih ---")
print(df[['Cars Prices', 'Cleaned Prices']].head())


df_ferrari = df[df['Company Names'] == 'FERRARI']

statistik_ferrari = df_ferrari['Cleaned Prices'].describe()

harga_rata_rata = statistik_ferrari['mean']
harga_terendah = statistik_ferrari['min']
harga_tertinggi = statistik_ferrari['max']
jumlah_mobil = statistik_ferrari['count']

print("\n--- Laporan Harga Final untuk Mobil FERRARI ---")

print(f"Berdasarkan analisis dari {jumlah_mobil:.0f} unit:")
print(f"Harga Rata-rata : ${harga_rata_rata:,.2f}")
print(f"Harga Terendah  : ${harga_terendah:,.2f}")
print(f"Harga Tertinggi : ${harga_tertinggi:,.2f}")