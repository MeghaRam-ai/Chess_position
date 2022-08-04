
import numpy as np
import pandas as pd

import os
import cv2
from dotenv import load_dotenv


def process_test_img(chess_board_image):
    if os.getenv('ROOT') is None:
        load_dotenv()

    test_image_ = [img.reshape(1875,1) for img in chess_board_image]
    test_image_ = (np.array(test_image_))

    size_x=test_image_.shape[0]
    size_y=test_image_.shape[1]*test_image_.shape[2]

    test_board_img = [img.reshape(size_y,1) for img in test_image_]
    test_board_array = np.array(test_board_img).reshape((size_x,size_y))
    processed_test_img = pd.DataFrame(test_board_array)

    return processed_test_img

#
# def preprocess_img(X):
#     if os.getenv('ROOT') is None:
#         load_dotenv()
#     # temp=[]
#     # for i in X:
#     img  =cv2.resize(X, (200, 200))
#     temp = split_chess_board(img)
#     return temp

def split_chess_board(board):
    img = cv2.resize(board, (200, 200))
    temp = []
    for x in range(0,8):
        temp2 = img[(x*25):((x+1)*25),:]
        for y in range(0,8):
            temp.append(temp2[:,(y*25):((y+1)*25)].flatten().reshape(25,25,3))
    return temp
