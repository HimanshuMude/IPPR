import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


img = Image.open("image.jpg")
M = np.asarray(img)

red_channel = M[:, :, 0]
green_channel = M[:, :, 1]
blue_channel = M[:, :, 2]

green_enhanced = np.clip(green_channel * 1.75, 0, 255)  

enhanced_image = np.stack((red_channel, green_enhanced, blue_channel), axis=-1).astype(np.uint8)
enhanced_image = Image.fromarray(enhanced_image)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(enhanced_image)
plt.title("Enhanced Image (Green Channel)")

plt.show()