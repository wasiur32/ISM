import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import rasterio
from tensorflow.keras.models import load_model
from PIL import Image
import os

from flask import Flask, render_template

app = Flask(__name__)

def getPrediction(filename):
    model_path = 'model/model3.h5'
    my_model = load_model(model_path, compile=False)
    
    img_path = 'static/image/' + filename
    img_op = 'static/output/'
    
    # Open the image using rasterio
    with rasterio.open(img_path) as dataset:
        # Read all bands (assuming it's a multi-band image)
        img = dataset.read()
        
        # Get the metadata from the original image
        metadata = dataset.profile

    # Scale pixel values using min-max scaling
    img = (img - img.min()) / (img.max() - img.min())
    
    # Transpose the image to match the channel order expected by Keras (channels last)
    img = np.transpose(img, (1, 2, 0))
    
    img = np.expand_dims(img, axis=0)  # Get it ready as input to the network
    
    # Predict
    threshold = 0.5
    pred = my_model.predict(img)
    pred = (pred > threshold).astype(np.uint8)
    output_path_tiff = 'static/output/test_output.tif'  # TIFF output
    output_path_jpg = 'static/output/test_output.jpg'  # JPG output
    
    # Save the prediction as a TIFF file with metadata
    with rasterio.open(
        output_path_tiff,
        'w',
        driver='GTiff',
        height=pred.shape[1],
        width=pred.shape[2],
        count=1,
        dtype=str(pred.dtype),
        crs=metadata.get('crs'),  # Copy the coordinate reference system
        transform=metadata.get('transform'),  # Copy the transformation
    ) as dst:
        dst.write(pred[0, :, :, 0], 1)
    
    # Convert the TIFF image to grayscale using Pillow (PIL) and save as JPG
    img_tiff = Image.open(output_path_tiff)
    img_pil = Image.fromarray((np.array(img_tiff) * 255).astype(np.uint8))
    img_pil = img_pil.convert('L')  # Convert to grayscale
    img_pil.save(output_path_jpg, 'JPEG')

    return output_path_tiff, output_path_jpg