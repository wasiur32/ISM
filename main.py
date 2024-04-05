import numpy as np
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model

def getPrediction(filename):
    # Define your class names and associated medicines
    classes = ['Cherry_(including_sour)___Powdery_mildew',
               'Cherry_(including_sour)___healthy',
               'Corn_(maize)___Common_rust_',
               'Corn_(maize)___Northern_Leaf_Blight',
               'Corn_(maize)___healthy',
               'Pepper,_bell___healthy',
               'Potato___Early_blight',
               'Tomato___Bacterial_spot',
               'Tomato___Septoria_leaf_spot',
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
               'Tomato___healthy']
    
    medicines = {'Cherry_(including_sour)___Powdery_mildew': 'Medicine A',
                 'Cherry_(including_sour)___healthy': 'Medicine B',
                 'Corn_(maize)___Common_rust_': 'Medicine C',
                 'Corn_(maize)___Northern_Leaf_Blight': 'Medicine D',
                 'Corn_(maize)___healthy': 'Medicine E',
                 'Pepper,_bell___healthy': 'Medicine F',
                 'Potato___Early_blight': 'Medicine G',
                 'Tomato___Bacterial_spot': 'Medicine H',
                 'Tomato___Septoria_leaf_spot': 'Medicine I',
                 'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Medicine J',
                 'Tomato___healthy': 'Medicine K'}
    
    # Fit LabelEncoder to your class names
    le = LabelEncoder()
    le.fit(classes)
    
    # Load the model
    my_model = load_model(r"C:\Users\Windows 10 Pro\Desktop\kb\model\model.h5")

    
    # Resize image
    SIZE = 256
    img_path = filename  # Use the absolute file path directly
    img = np.asarray(Image.open(img_path).resize((SIZE, SIZE)))
    
    # Scale pixel values
    img = img / 255.0
    
    # Expand dimensions for model input
    img = np.expand_dims(img, axis=0)
    
    # Make prediction
    pred = my_model.predict(img)
    
    # Convert prediction to class name
    pred_class = le.inverse_transform([np.argmax(pred)])[0]
    
    # Get medicine for the predicted disease
    medicine = medicines.get(pred_class, 'Unknown')
    
    # Print diagnosis and associated medicine
    print("Diagnosis is:", pred_class)
    print("Prescribed medicine is:", medicine)
    
    return pred_class, medicine


