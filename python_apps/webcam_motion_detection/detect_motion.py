import cv2
import pathlib

#set current working directory
cwd = pathlib.Path(__file__).parent.resolve()

#Reading in facial detection file
face_detection = cv2.CascadeClassifier(f'{cwd}\haarcascade_frontalface_default.xml')

#Initialising video capture for the webcam at index 0 (in most cases this will be the in-built webcam if using a laptop)
webcam = cv2.VideoCapture(0)

#If the webcam cannot be found and opened, print error message
if webcam.isOpened() == False:
    print('Error with opening webcam')

#Create loop which will relay image frames until the letter q is pressed
while webcam.isOpened():

    #Read the image frame from the webcam
    #   is_frame_found: Boolean, returns True if an image frame is found, False otherwise
    #   webcam_frame: numpy array, returns the image frame captured by the webcam
    is_frame_found, webcam_frame = webcam.read()

    #Converting image frame to greyscale for quicker and better face detection
    greyscale_frame=cv2.cvtColor(webcam_frame, cv2.COLOR_BGR2GRAY)

    #Detect all faces in frame
    faces_detected = face_detection.detectMultiScale(
        greyscale_frame,
        scaleFactor=1.05,
        minNeighbors=5
    )

    #For each face detected, display a green rectangle surrounding the face
    for x, y, w, h in faces_detected:
        webcam_frame = cv2.rectangle(webcam_frame, (x,y), (x+w,y+h),(0,255,0),3)

    #If an image frame is found, display the image
    if is_frame_found:
        cv2.imshow("webcam", webcam_frame)

        #After 25ms if q is pressed, display no further frames
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break
    
#Release the video capture from the webcam
webcam.release()

#Destroy all frames being displayed
cv2.destroyAllWindows()