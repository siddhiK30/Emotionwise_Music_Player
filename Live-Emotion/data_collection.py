import mediapipe as mp 
import numpy as np 
import cv2 
import os

cap = cv2.VideoCapture(0)

name = input("Enter the name of the data: ")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

X = []

# Check if file already exists
if os.path.exists(f"{name}.npy"):
    # Load existing data
    X = list(np.load(f"{name}.npy"))

data_size = len(X)

while True:
    lst = []

    _, frm = cap.read()

    frm = cv2.flip(frm, 1)

    res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.face_landmarks:
        for i in res.face_landmarks.landmark:
            lst.append(i.x - res.face_landmarks.landmark[1].x)
            lst.append(i.y - res.face_landmarks.landmark[1].y)

        X.append(lst)
        data_size += 1

    drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
    cv2.putText(frm, str(data_size), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break

np.save(f"{name}.npy", np.array(X))
print(np.array(X).shape)