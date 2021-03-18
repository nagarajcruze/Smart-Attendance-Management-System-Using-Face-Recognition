import cv2
from PIL import Image
import face_recognition
import numpy as np
import glob


dictionaryy = {}

for i in glob.glob('pics\\*.jpg'):
    m = face_recognition.load_image_file(i)
    face_encoding = face_recognition.face_encodings(m)
    a  = np.array(face_encoding).tolist()
    try:
        dictionaryy[i] = a[0]
    except IndexError:
        print("{} Face is Not Clear".format(i))
    print(i[5:]+"'s Model Trained Succeffully \n")
