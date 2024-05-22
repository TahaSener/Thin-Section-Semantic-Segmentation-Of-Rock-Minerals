from mmseg.apis import MMSegInferencer
import numpy as np
import glob
from PIL import Image
import os

# Initialize the model
inferencer = MMSegInferencer(model='Model/mask2former_swin-s_8xb2-90k_cityscapes-512x1024.py',
                             weights='Model/Model.pth')

# Paths
image_dir = 'Example Dataset/'
output_dir = 'Predictions/'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define the color palette for the 4 classes
palette = [
    (0, 0, 0),        # Class 0: Black
    (255, 0, 0),      # Class 1: Red
    (0, 255, 0),      # Class 2: Green
    (0, 0, 255)       # Class 3: Blue
]

# Lists to store IoU values
ious = []

# Loop through the images
for image_path in glob.glob(os.path.join(image_dir, '*.jpg')):
    # Predict the mask for the image
    result = inferencer(image_path)
    predicted_mask = result['predictions']
    
    # Convert the predicted mask to a PIL Image
    predicted_mask_image = Image.fromarray(predicted_mask.astype(np.uint8))

    # Apply the color palette
    predicted_mask_image.putpalette(np.array(palette, dtype=np.uint8).flatten())

    # Create the output file path
    base_name = os.path.basename(image_path)
    output_path = os.path.join(output_dir, base_name.replace('.jpg', '.png'))

    # Save the image
    predicted_mask_image.save(output_path)

    print(f"Saved prediction for {image_path} to {output_path}")
