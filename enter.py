import face_recognition
import cv2
import numpy as np
from PIL import Image
import requests
import os


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
# Create arrays of known face encodings and their names
known_face_encodings = [
]
known_face_names = [
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = color_image_rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        if face_encodings:
            print(1)
            pil_image = Image.fromarray(frame)
            pil_image.save('test.jpg')

            with open('test.jpg', 'rb') as file:
            # указываем дополнительные заголовки и параметры
                files = {'file': file.read()}
                data = {'filename': 'test.jpg'}
                headers = {'Authorization': '1234'}
                test = requests.post('http://31.129.102.179/api/enter_person', files=files, data=data, headers=headers)
            try:
                test.raise_for_status()
                print(test.json())
            except requests.exceptions.HTTPError:
                name = 'Unknown@'
            os.remove('test.jpg')

    # cv2.imshow('Enter', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Display the resulting image


video_capture.release()
cv2.destroyAllWindows()
