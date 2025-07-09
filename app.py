import streamlit as st
import numpy as np
import tensorflow as tf
import keras
from PIL import Image
#Loading the model
my_model = keras.models.load_model('my_model.h5', compile=False)

#creating a gender dictionary
gen_dict = {0: "Male", 1: "Female"}



#Feature Extraction
def feature_extraction(image):
    features = []
    img = image.convert("L")
    img = img.resize((128,128), Image.Resampling.LANCZOS)
    img = np.array(img)
    features.append(img)

    features = np.array(features)
    features = features.reshape(len(features),128,128,1)
    return features


st.set_page_config(page_title="Age Gender Detection App", layout="centered")

st.title(" Upload an Image")

# Upload the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=False)
    
    #feature extration
    img_pred = feature_extraction(image)
    img_pred = img_pred/255.0

    #making the prediction from the uploaded model
    pred = my_model.predict(img_pred)

    #extracting the predicted age and gender
    age = round(pred[1][0][0])
    gender = gen_dict[round(pred[0][0][0])]  # 1 if > 0.5 else 0

    

    st.success(f"The predicted gender is {gender} and the predicted age is {age}!")
