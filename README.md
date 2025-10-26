# 🧠 UTS Citra Digital - Pengolahan Citra dengan Filter

Proyek ini merupakan tugas UTS mata kuliah **Citra Digital**, yang berfokus pada penerapan berbagai teknik filter untuk memperbaiki kualitas citra yang terkontaminasi noise menggunakan Python.

## 📂 Struktur Proyek
- `main.py` → Program utama untuk menjalankan semua proses
- `filters.py` → Berisi fungsi filter (Gaussian, Median, dan Hybrid)
- `metrics.py` → Menghitung metrik evaluasi (PSNR & SSIM)
- `gambar_ujj.jpg` → Citra asli yang digunakan untuk pengujian
- hasil-uji.png  → ini adalah output dari filter (Gaussian, Median, dan Hybrid)
- Folder `output/` → Menyimpan hasil pemrosesan

## ⚙️ Teknologi yang Digunakan
- **Python**
- **OpenCV (`cv2`)**
- **NumPy**
- **Matplotlib**
- **scikit-image**

## 📸 Hasil Output
Berikut hasil perbandingan antara citra asli, noisy, dan hasil setelah difilter:

![Hasil Output](https://raw.githubusercontent.com/XyzpaulV/UTS-Citra_Digital/refs/heads/main/hasil-uji.png)

## 📈 Hasil Evaluasi PSNR & SSIM

| Jenis Citra  | PSNR  |  SSIM |
|--------------|-------|-------|
| Noisy        | 22.17 | 0.404 |
| Gaussian     | 27.89 | 0.736 |
| Median       | 26.48 | 0.658 |
| Hybrid       | 26.99 | 0.736 |

✅ Semua hasil disimpan di folder `output/`

## 🧩 Penjelasan Singkat
Citra yang rusak akibat noise diproses menggunakan tiga teknik filter:
- **Gaussian Filter:** Menghaluskan gambar dan mengurangi noise acak  
- **Median Filter:** Menghilangkan noise impuls (salt & pepper)  
- **Hybrid Filter:** Kombinasi Gaussian + Median untuk hasil yang lebih seimbang  

Metrik **PSNR (Peak Signal-to-Noise Ratio)** dan **SSIM (Structural Similarity Index)** digunakan untuk menilai seberapa baik hasil filter mempertahankan kualitas citra asli.
 Hasil menunjukkan bahwa filter Gaussian dan Hybrid mampu meningkatkan kualitas citra (PSNR dan SSIM lebih tinggi) dibanding citra noisy. Namun secara visual, perbedaannya tidak terlalu terlihat karena intensitas noise yang rendah, dan citra asli tetap tampak paling baik karena belum kehilangan detail akibat proses filtering.

