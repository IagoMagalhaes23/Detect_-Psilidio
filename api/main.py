'''
    Autor: Iago e Vanessa
    Data: 13/11/2023
    Descrição:
        - 
'''

import os
import sys
import cv2
import numpy as np
from keras.models import load_model
from flask import Flask, request, jsonify



path = os.path.abspath("../")
sys.path.append(path)

from utils import functions as fct

app = Flask(__name__)





if(__name__) == '__main__':
    app.run(debug=True)