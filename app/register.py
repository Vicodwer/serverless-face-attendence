# register.py

import cv2
import os
import face_recognition
import pickle

DATASET_DIR = "dataset"
MODEL_PATH = "models/face_encodings.pkl"

os.makedirs(DATASET_DIR, exist_ok=True)
os.makedirs("models", exist_ok=True)

def register_user(name):
    video = cv2.VideoCapture(0)
    print("Press 's' to capture image. Press 'q' to quit.")

    while True:
        ret, frame = video.read()
        cv2.imshow("Register - Press 's' to capture", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = face_recognition.face_locations(rgb_frame)

            if len(faces) == 0:
                print("No face detected. Try again.")
                continue

            encoding = face_recognition.face_encodings(rgb_frame, faces)[0]

            # Save encoding
            if os.path.exists(MODEL_PATH):
                with open(MODEL_PATH, "rb") as f:
                    data = pickle.load(f)
            else:
                data = {"names": [], "encodings": []}

            data["names"].append(name)
            data["encodings"].append(encoding)

            with open(MODEL_PATH, "wb") as f:
                pickle.dump(data, f)

            print(f"{name} registered successfully!")
            break

        elif key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    username = input("Enter student name: ")
    register_user(username)
