import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

def calculate_psnr(original, processed):
    return peak_signal_noise_ratio(original, processed)

def calculate_ssim(original, processed):
    return structural_similarity(original, processed)
