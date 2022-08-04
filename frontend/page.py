import sys
sys.path.append("..")
import streamlit as st
from chess_board.inference import predict
from chess_board.preprocess import split_chess_board
from PIL import Image
import numpy as np


def load_image(image_file):
    img = Image.open(image_file)
    img_ = np.array(img)
    return img_


st.subheader("FEN Prediction from Chess board Image")
image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

if image_file is not None:
    img = load_image(image_file)
    st.image(img,caption="Given Image:")

    split = split_chess_board(img)
    predicted_fen = predict(split)

    out = "Predicted FEN :", predicted_fen
    st.subheader(out)
