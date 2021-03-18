import cv2

cap = cv2.VideoCapture(0)
count = 1

face_id = input("enter your Register Number: ")

for _ in range(20):
    ret ,image = cap.read()
    cv2.imshow('frame', image)
    cv2.imwrite("pics/"+face_id+".jpg", image)
    print("%d --> successfull "%count)
    count +=1
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
