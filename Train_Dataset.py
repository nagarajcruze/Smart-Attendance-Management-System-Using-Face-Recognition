import cv2
from PIL import Image
import face_recognition
import numpy as np
import glob


dictionary = {}

for i in glob.glob('pics/*.jpg'):
    m = face_recognition.load_image_file(i)
    print("############",i,"###############\n")
    face_encoding = face_recognition.face_encodings(m)
    a  = np.array(face_encoding).tolist()
    dictionary[i]= a[0]
    print("Face Location is Succeffully trained, Stored at",i,"\n")
