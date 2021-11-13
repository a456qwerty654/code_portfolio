import cv2

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

    #If an image frame is found, display the image
    if is_frame_found:
        cv2.imshow("webcam", webcam_frame)

        #After 25ms if q is pressed, display no further frames
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break
    
#Release the video capture from the webcam
webcam.release()

#Destroy all frames being displayed
cv2.destroyAllWindows()