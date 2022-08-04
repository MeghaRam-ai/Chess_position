from chess_board.preprocess import process_test_img
import joblib
import numpy as np

import os
from dotenv import load_dotenv


def load_model():
    file_name = os.getenv('ROOT') + '/models/pipeline_model.pkl'
    # file_name = 'models/pipeline_model.pkl'
    loaded_model = joblib.load(file_name)
    return loaded_model


def load_encoder():
    file_name = os.getenv('ROOT')+'/models/label_encoder.pkl'
    encoder = joblib.load(file_name)
    return encoder


def decode_fen(prediction):
    predicted_fen = []
    for i in prediction:
        le = load_encoder()
        row = le.inverse_transform(i)
        fen = ''
        count = 0
        digit_flag = False
        for j in range(len(row)):
            if row[j].isdigit():
                count = count + 1
                digit_flag = True
                if j == 7:
                    fen = fen + str(count)
            else:
                if digit_flag:
                    fen = fen + str(count)
                    fen = fen + row[j]
                else:
                    fen = fen + row[j]
                digit_flag = False
                count = 0
        predicted_fen.append(fen)
    return '-'.join(predicted_fen)


def predict(chess_board_image):
    if os.getenv('ROOT') is None:
        load_dotenv()

    processed_test_img = process_test_img(chess_board_image)
    model = load_model()
    prediction = model.predict(processed_test_img)
    fen_predicted = decode_fen(np.array(prediction).reshape(8, 8))
    return fen_predicted
