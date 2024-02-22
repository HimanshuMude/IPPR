import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("peacock.jpg")

M = np.asarray(img)
# print(M)

plt.figure(figsize=(12, 12))

plt.subplot(221)
plt.imshow(M)
plt.title("Original Image")

plt.subplot(222)

plt.imshow(M[:, :, 0], cmap='Reds', vmin=0, vmax=255)
plt.title("Red Channel")
plt.subplot(223)

plt.imshow(M[:, :, 1], cmap='Greens', vmin=0, vmax=255)
plt.title("Green Channel")
plt.subplot(224)

plt.imshow(M[:, :, 2], cmap='Blues', vmin=0, vmax=255)
plt.title("Blue Channel")

plt.show()