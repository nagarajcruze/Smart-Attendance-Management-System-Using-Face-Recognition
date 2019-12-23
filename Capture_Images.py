import cv2

cap = cv2.VideoCapture(0)
count = 1

face_id = input("enter your name: ")

for _ in range(10):
    ret ,image = cap.read()
    cv2.imshow('frame', image)
    cv2.imwrite("pics/"+face_id+"_%d.jpg" % count, image)
    print("%d --> successfull "%count)
    count +=1
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
