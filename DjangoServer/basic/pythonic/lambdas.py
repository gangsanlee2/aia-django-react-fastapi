import os.path

import cv2 as cv
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from admin.path import dir_path


def MosaicLambdas(cmd, target): #Command Pattern
    #cmd = params[0]
    #target = params[1]
    if cmd == 'IMAGE_READ':
        return (lambda x: cv.imread(os.path.join(dir_path('mosaic'), 'data', x)))(target)
    elif cmd == 'GRAYSCALE':
        return (lambda x: cv.cvtColor(x, cv.COLOR_BGR2GRAY))(target)
    elif cmd == 'FROM_ARRAY':
        return (lambda x: Image.fromarray(x))(target)

def Learning(cmd):
    if cmd == "랜덤포레스트분류기":
        return RandomForestClassifier()
    elif cmd == "결정트리분류기":
        return DecisionTreeClassifier()
    elif cmd == "로지스틱회귀":
        return LogisticRegression()
    elif cmd == "서포트벡터머신":
        return LinearSVC()

