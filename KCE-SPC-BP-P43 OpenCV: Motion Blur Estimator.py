import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("blurred.jpg", 0)

# FFT magnitude spectrum
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude = 20 * np.log(np.abs(fshift) + 1)

# Detect lines using Hough
edges = cv2.Canny(magnitude.astype(np.uint8), 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

angle = None
if lines is not None:
    rho, theta = lines[0][0]
    angle = np.degrees(theta)
    print("Estimated Motion Blur Angle:", round(angle, 2), "degrees")
else:
    print("No dominant motion blur detected")

# Blur length estimation (rough: inverse of high-frequency energy)
laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
blur_length = round(1000 / (laplacian_var + 1), 2)
print("Estimated Blur Length:", blur_length)

# Show results
plt.subplot(1,2,1), plt.imshow(img, cmap="gray"), plt.title("Input Blurred")
plt.subplot(1,2,2), plt.imshow(magnitude, cmap="gray"), plt.title("FFT Spectrum")
plt.show()
