# author: Asmaa Mirkhan ~ 2019

import os
import argparse
import cv2 as cv
from .DetectorAPI import DetectorAPI

MODEL_PATH = os.path.join(os.getcwd(), "src/mlmodel/face.pb")

def blurBoxes(image, boxes):
    """
    Argument:
    image -- the image that will be edited as a matrix
    boxes -- list of boxes that will be blurred, each box must be int the format (x_top_left, y_top_left, x_bottom_right, y_bottom_right)
    
    Returns:
    image -- the blurred image as a matrix
    """

    for box in boxes:
        # unpack each box
        x1, y1, x2, y2 = [d for d in box]

        # crop the image due to the current box
        sub = image[y1:y2, x1:x2]

        # apply GaussianBlur on cropped area
        blur = cv.blur(sub, (25, 25))

        # paste blurred image on the original image
        image[y1:y2, x1:x2] = blur

    return image

def blurit(imagepath, threshold=0.3):
    odapi = DetectorAPI(path_to_ckpt=MODEL_PATH)
    image = cv.imread(imagepath)
    boxes, scores, classes, num = odapi.processFrame(image)
    boxes = [boxes[i] for i in range(0, num) if scores[i] > threshold]
    image = blurBoxes(image, boxes)
    cv.imshow(imagepath, image)
