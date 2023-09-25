import cv2 
import dlib
import playsound
import numpy as np

 #Load the face detector and landmark prediimport cv2
 

 # Load the face detector and landmark predictor models # 
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

 # Define the eye aspect ratio (EAR) function
def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

 # Define the sound player function
def play_sound(sound_file):
    playsound.playsound(sound_file)
 # Define the threshold values for eye aspect ratio (EAR) and consecutive frames
EAR_THRESHOLD = 0.3
CONSECUTIVE_FRAMES_THRESHOLD = 48

 # Initialize the counters for consecutive frames and total number of blinks
COUNTER = 0
TOTAL_BLINKS = 0

 # Initialize the video capture object
cap = cv2.VideoCapture(0)

 # Loop over frames from the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
     # Resize the frame and convert it to grayscale
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     # Detect faces in the grayscale frame
    faces = detector(gray)

     # Loop over the faces
    for face in faces:
        # Detect the landmarks for the face
        landmarks = predictor(gray, face)
         # Extract the left and right eye landmarks
        left_eye = []
        for i in range(36, 42):
            left_eye.append((landmarks.part(i).x, landmarks.part(i).y))
        right_eye = []
        for i in range(42, 48):
            right_eye.append((landmarks.part(i).x, landmarks.part(i).y))
         # Compute the eye aspect ratio (EAR) for the left and right eyes
        left_ear = eye_aspect_ratio(np.array(left_eye))
        right_ear = eye_aspect_ratio(np.array(right_eye))
         # Compute the average eye aspect ratio (EAR)
        ear = (left_ear + right_ear) / 2.0

         # Check if the eye aspect ratio (EAR) is below the threshold value
        if ear < EAR_THRESHOLD:
            COUNTER += 1
        else:
            # If the eyes have been closed for a sufficient number of consecutive frames, sound the alarm
            if COUNTER >= CONSECUTIVE_FRAMES_THRESHOLD:
                # Reset the counters for consecutive frames and total number of blinks
                TOTAL_BLINKS += 1
                COUNTER = 0
                 # Play the sound file
                play_sound('alarm.wav')

         # Draw the left and right eye landmarks and the eye aspect ratio (EAR) on the frame
            cv2.drawContours(frame, [np.array(left_eye)], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [np.array(right_eye)], -1, (0, 255, 0), 1)
            cv2.putText(frame, 'EAR: {:.2f}'.format(ear), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)actor models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Define the eye aspect ratio (EAR) function
def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Define the sound player function
def play_sound(sound_file):
    playsound.playsound(sound_file)

# Define the threshold values for eye aspect ratio (EAR) and consecutive frames
EAR_THRESHOLD = 0.3
CONSECUTIVE_FRAMES_THRESHOLD = 48

# Initialize the counters for consecutive frames and total number of blinks
COUNTER = 0
TOTAL_BLINKS = 0

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Loop over frames from the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Resize the frame and convert it to grayscale
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    # Loop over the faces
    for face in faces:
        # Detect the landmarks for the face
        landmarks = predictor(gray, face)

        # Extract the left and right eye landmarks
        left_eye = []
        for i in range(36, 42):
            left_eye.append((landmarks.part(i).x, landmarks.part(i).y))
        right_eye = []
        for i in range(42, 48):
            right_eye.append((landmarks.part(i).x, landmarks.part(i).y))

        # Compute the eye aspect ratio (EAR) for the left and right eyes
        left_ear = eye_aspect_ratio(np.array(left_eye))
        right_ear = eye_aspect_ratio(np.array(right_eye))

        # Compute the average eye aspect ratio (EAR)
        ear = (left_ear + right_ear) / 2.0

        # Check if the eye aspect ratio (EAR) is below the threshold value
        if ear < EAR_THRESHOLD:
            COUNTER += 1
        else:
            # If the eyes have been closed for a sufficient number of consecutive frames, sound the alarm
            if COUNTER >= CONSECUTIVE_FRAMES_THRESHOLD:
                # Reset the counters for consecutive frames and total number of blinks
                TOTAL_BLINKS += 1
                COUNTER = 0

                # Play the sound file
                play_sound('alarm.wav')

        # Draw the left and right eye landmarks and the eye aspect ratio (EAR) on the frame
        cv2.drawContours(frame, [np.array(left_eye)], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [np.array(right_eye)], -1, (0, 255, 0), 1)
        cv2.putText(frame, 'EAR: {:.2f}'.format(ear), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    
