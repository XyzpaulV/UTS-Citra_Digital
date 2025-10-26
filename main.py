import cv2
import numpy as np
import matplotlib.pyplot as plt
from filters import apply_gaussian, apply_median, apply_hybrid
from metrics import calculate_psnr, calculate_ssim

# 1️⃣ Baca gambar input
img = cv2.imread('input/gambar_uji.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("❌ Gambar tidak ditemukan! Pastikan file ada di folder 'input/' dan bernama 'gambar_uji.jpg'")
    exit()

# 2️⃣ Tambahkan noise Gaussian ke gambar
noise = np.random.normal(0, 20, img.shape)
noisy = img + noise
noisy = np.clip(noisy, 0, 255).astype(np.uint8)
cv2.imwrite('output/noisy.jpg', noisy)

# 3️⃣ Terapkan filter ke gambar noisy
gaussian = apply_gaussian(noisy)
median = apply_median(noisy)
hybrid = apply_hybrid(noisy)

# 4️⃣ Hitung metrik kualitas (PSNR dan SSIM)
print("=== 📈 Hasil Evaluasi PSNR & SSIM ===")
print(f"Noisy   -> PSNR: {calculate_psnr(img, noisy):.2f}, SSIM: {calculate_ssim(img, noisy):.3f}")
print(f"Gaussian-> PSNR: {calculate_psnr(img, gaussian):.2f}, SSIM: {calculate_ssim(img, gaussian):.3f}")
print(f"Median  -> PSNR: {calculate_psnr(img, median):.2f}, SSIM: {calculate_ssim(img, median):.3f}")
print(f"Hybrid  -> PSNR: {calculate_psnr(img, hybrid):.2f}, SSIM: {calculate_ssim(img, hybrid):.3f}")

# 5️⃣ Tampilkan hasil semua gambar
titles = ['Asli', 'Noisy', 'Gaussian', 'Median', 'Hybrid']
images = [img, noisy, gaussian, median, hybrid]

plt.figure(figsize=(12, 8))
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

# 6️⃣ Simpan hasil
cv2.imwrite('output/hasil_gaussian.jpg', gaussian)
cv2.imwrite('output/hasil_median.jpg', median)
cv2.imwrite('output/hasil_hybrid.jpg', hybrid)

print("\n✅ Semua hasil disimpan di folder 'output/'")
