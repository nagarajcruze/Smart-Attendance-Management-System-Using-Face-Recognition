import cv2
import os
import time

cap = cv2.VideoCapture(0)
count = 1

current_working_dir = os.getcwd()
pictures_dir = current_working_dir+'\\pics'
if not os.path.exists(pictures_dir):
    os.mkdir(pictures_dir)

face_id = input("enter your Register Number: ")

for _ in range(5):
    ret ,image = cap.read()
    cv2.imshow('Please Look into this FRAME', image)
    cv2.imwrite("pics/"+face_id+".jpg", image)
    print("%d --> successfull "%count)
    time.sleep(1)
    count +=1
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
