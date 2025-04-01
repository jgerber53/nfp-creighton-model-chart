#!/usr/bin/env python
# coding: utf-8

# Run combineCharts.py to combine multiple single cycle charts into a full chart 
# (the group of 6 cycles you are used to seeing on paper charts). 
# Move or copy charts you wish to include to the "to_combine/" directory.

import numpy as np
from pathlib import Path
from PIL import Image

# Define paths
charts_path = Path("/Users/gerb5/vscode-projects/nfp-creighton-model-chart/Charts/")
combine_path = charts_path / "to_combine"
cropped_path = charts_path / "cropped"
complete_path = charts_path / "complete"

# Ensure directories exist
combine_path.mkdir(exist_ok=True)
cropped_path.mkdir(exist_ok=True)
complete_path.mkdir(exist_ok=True)

list_images = list(combine_path.glob("*.png"))

# Check if images exist
if not list_images:
    print("No images found in the to_combine/ directory. Please add images and retry.")
    exit()

# Load images
images = [Image.open(img) for img in list_images]

# Crop images
shave_top, shave_bottom = 62, 25  # pixels to shave
cropped = []

for idx, img in enumerate(images):
    w, h = img.size
    crop_box = (0, shave_top if idx > 0 else 0, w, h - shave_bottom)
    cropped_name = cropped_path / list_images[idx].name  # Keep original filename
    img.crop(crop_box).save(cropped_name)
    cropped.append(cropped_name)

# Reload cropped images
images = [Image.open(img) for img in cropped]

# Resize to smallest width while maintaining aspect ratio
min_shape = min((img.size for img in images), key=lambda s: s[0] * s[1])
min_width = min(img.size[0] for img in images)
images_resized = [img.resize((min_width, int(img.size[1] * (min_width / img.size[0])))) for img in images]

##
# Use the first image's dimensions as the reference size
header_image = images[0]  # Keep the first image as header
header_width, header_height = header_image.size

# Resize all other images to match the header width while maintaining aspect ratio
body_images = [
    img.resize((header_width, int(img.size[1] * (header_width / img.size[0]))), Image.Resampling.LANCZOS)
    for img in images[1:]  # Exclude header from resizing
]

# Stack images together (header first, then body images)
imgs_comb = np.vstack([np.asarray(header_image)] + [np.asarray(img) for img in body_images])

# Convert back to Image object
imgs_comb = Image.fromarray(imgs_comb)

# Create a proper filename
output_name = charts_path / complete_path / f"{list_images[0].stem}_to_{list_images[-1].stem}.png"

# Save the final combined image
imgs_comb.save(output_name)

print(f"Saved as {output_name}")

# Function to delete all files in a directory
def clear_directory(directory: Path):
    for file in directory.glob("*"):
        file.unlink()  # Remove file
    print(f"Cleared {directory}")

# Remove all files from temp directories after processing
# Comment out the next two lines for troubleshooting
clear_directory(combine_path)
clear_directory(cropped_path)

print("Done.")