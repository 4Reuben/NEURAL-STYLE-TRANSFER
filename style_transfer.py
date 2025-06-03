import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

# Load and process image
def load_img(path, max_dim=512):
    img = Image.open(path).convert('RGB')
    long = max(img.size)
    scale = max_dim / long
    img = img.resize((round(img.size[0]*scale), round(img.size[1]*scale)))
    img = tf.keras.utils.img_to_array(img)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

def tensor_to_image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        tensor = tensor[0]
    return Image.fromarray(tensor)

# Paths
content_path = "content.png"
style_path = "style.png"

# Load images
print("📷 Loading images...")
content_image = load_img(content_path)
style_image = load_img(style_path)

# Load model
print("🧠 Loading style transfer model...")
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# Stylize
print("🎨 Applying style...")
start = time.time()
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
end = time.time()

print(f"✅ Style transferred in {end - start:.2f} seconds")

# Save result
output_image = tensor_to_image(stylized_image)
output_image.save("output.png")
print("🖼️ Saved styled image as output.png")
