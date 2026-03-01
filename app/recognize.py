# recognize.py

import cv2
import face_recognition
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
import os

MODEL_PATH = "models/face_encodings.pkl"
ATTENDANCE_FILE = "attendance.csv"

def mark_attendance(name):
    if os.path.exists(ATTENDANCE_FILE):
        df = pd.read_csv(ATTENDANCE_FILE)
    else:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    today = datetime.now().strftime("%Y-%m-%d")
    
    if ((df["Name"] == name) & (df["Date"] == today)).any():
        return

    new_entry = {
        "Name": name,
        "Date": today,
        "Time": datetime.now().strftime("%H:%M:%S")
    }

    df = pd.concat([df, pd.DataFrame([new_entry])])
    df.to_csv(ATTENDANCE_FILE, index=False)
    print(f"Attendance marked for {name}")

def recognize_faces():
    if not os.path.exists(MODEL_PATH):
        print("No registered users found.")
        return

    with open(MODEL_PATH, "rb") as f:
        data = pickle.load(f)

    video = cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faces = face_recognition.face_locations(rgb_frame)
        encodings = face_recognition.face_encodings(rgb_frame, faces)

        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            face_distances = face_recognition.face_distance(data["encodings"], encoding)

            if len(face_distances) > 0:
                best_match = np.argmin(face_distances)

                if matches[best_match]:
                    name = data["names"][best_match]
                    mark_attendance(name)

        cv2.imshow("Recognition - Press 'q' to exit", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    recognize_faces()
