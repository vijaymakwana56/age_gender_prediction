#  Age & Gender Prediction App (Streamlit + Keras)

This is a simple Streamlit web app that predicts **age and gender** from an uploaded image using a trained Keras `.h5` model. The used in this model is imported from kaggle face dataset.

---

##  Features

- Upload an image (JPG/PNG)
- Convert to grayscale and preprocess for model input
- Predict **age** (as a number) and **gender** (Male/Female)
- Display uploaded image with predictions

---

##  Demo

https://agegenderprediction-tpnc7ahqkahkrcqet6hjml.streamlit.app/

---

##  Project Structure

```
age_gender_prediction/
│
├── app.py # Streamlit app
├── my_model.h5 # Pre-trained Keras model
├── requirements.txt # Dependencies
├── README.md # This file
├── .gitignore
└── lib/, Scripts/, Include/ # Virtual environment
```

