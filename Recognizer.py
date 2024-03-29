import cv2
from PIL import Image
import face_recognition
import numpy as np
import glob
import  csv
from time import strftime
from Train_Dataset import dictionaryy

print("RECOGNIZER STARTED ")
print("Please wait, It will take some time.....")
print("Hit 'q' on the keyboard to quit!")

dictionary = dictionaryy
encodes = [i for i in dictionary.values()]
known_face_encodings = encodes
names1 = [w.replace('pics\\', '') for w in dictionary.keys()]
namess = [w.replace('.jpg', '') for w in names1]
known_face_names = namess

video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
names = list()
try:
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (102, 255, 102), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 204, 153), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0,0,0), 1)
            names.append(name)
            
        # Display the resulting image
        cv2.imshow('Recognizing: Hit q to quit', frame)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
except :
    print("No PHOTOS available to Compare, Please capture photos again!")



#time and date is imported from the time module
time = strftime("%I:%M%p") #%I is used  for 12hr format,use %H instead  of %I for 24Hr format,
                           #%p is used for AM/PM 
date = strftime("%d-%m-%Y")
#print("it is found",recognized_faces[Person])
#recognized_faces = ["IronMan", "Captain America", "Natasha"]

facings = list(set(names))
recognized_faces = []
for i in facings:
    if i == "Unknown":
        continue
    recognized_faces.append(i)
with open('Attendance_sheet_of_{}.csv'.format(date), 'w') as file:
    Shadow = csv.writer(file)
    Header = [['Name', 'Attendance','Time']]
    Shadow.writerows(Header)
    for Person in range(len(recognized_faces)):
        Column_values = [[recognized_faces[Person], 'yes', str(time)]]
        print("Attendance successfully marked for the person {}".format(recognized_faces[Person]))
        Shadow.writerows(Column_values)
f= open("totalmembers.csv", 'r')
file = csv.reader(f)
TotalStrength = list()
for i in file:
    TotalStrength.append(i[0])
absentees = sorted(list(set(TotalStrength).difference(set(recognized_faces))))
f = open('Attendance_sheet_of_{}.csv'.format(date), 'a')
Shadows = csv.writer(f)
for absent in absentees:
    Column_values = [[absent, 'No', str(time)]]
    Shadows.writerows(Column_values)