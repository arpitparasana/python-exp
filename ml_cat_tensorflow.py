# Step 1: Import TensorFlow and other necessary libraries
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np

# Step 2: Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Step 3: Load a sample cat image for testing
img_path = 'img/cat_face.jpg'  # Provide the path to your cat image
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Step 4: Make predictions using the pre-trained model
predictions = model.predict(img_array)

# Step 5: Decode and display the predictions
decoded_predictions = decode_predictions(predictions, top=1)[0]
print("Predictions:")
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i + 1}: {label} ({score:.2f})")