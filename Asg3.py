import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image=Image.open("image.jpg")
M=np.asarray(image)

plt.figure(figsize=(12,6))
plt.subplot(121)
plt.imshow(M)
plt.title("Original Image")

red_channel=M[:,:,0]
green_channel=M[:,:,1]
blue_channel=M[:,:,2]


green_inverted=abs(255-green_channel)
red_inverted=abs(255-red_channel)
blue_inverted=abs(255-blue_channel)

inverted_image=np.stack((red_inverted,green_inverted,blue_inverted),axis=-1).astype(np.uint8)
inverted_image=Image.fromarray(inverted_image)

plt.subplot(122)
plt.imshow(inverted_image)
plt.title("Inverted Image")

plt.show()


