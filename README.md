# Chess_position

## Objective : Build a Vision AI which understands a position by looking at the board !
Take a chess board image as input and properly identify the position (FEN format).

#### Dataset : https://www.kaggle.com/koryakinp/chess-positions
#### Dataset Description
The dataset Chess Position contains 100000 images of randomly generated chess positions. The images are generated using 28 styles of chess boards and 32 styles of chess pieces. All the images are 400X400 pixels. Train set contains 80000 images and Test set contains 20000 images.  The labels are given in FEN notation. FEN is a standard notation of describing a chess board positions. Generally a chess board contains 32 items. There are 13 unique labels including empty space to occupy.

#### Models used in this project
1. CNN
2. SVM

#### To run the notebooks, first install necessary packages

 ```bash 
   $ pip install -r requirements.txt
   ```
#### To start streamlit application

1. Open terminal and go to the location frontend and excecute the following command
```bash
  $ streamlit run page.py
  ```
