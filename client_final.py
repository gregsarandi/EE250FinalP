import socket
import cv2
from datetime import datetime


##UDP Client section
SERVER_IP = '127.10.10.4'  # Raspberry pi address
SERVER_PORT = 1230  # Replace with desired port number
BUFFER_SIZE = 1024  # Maximum buffer size to receive at once

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Please send image', (SERVER_IP, SERVER_PORT))

number = 1 #number of image received from server
image_name = "image" + str(number) + ".jpeg"
with open(image_name, 'wb') as file: #save image name as image1, image2, etc
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE) #receive image in 1024 byte packages
        if not data:
            number + 1 #increment image number for next image
            break
        file.write(data)

now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
print("image received at ", dt_string)
print("Analyzing image")


#Data Processing Start
#OpenCV Facial Detection
#Script largely obtained from the following source
#Source: https://www.digitalocean.com/community/tutorials/how-to-detect-and-extract-faces-from-an-image-with-opencv-and-python
image = cv2.imread("image.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Uses HaarCascade Weights. 
#Potential Improvement: Caffe weights. Unable to obtain them without paying $$
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

if (len(faces) >= 1):
    print("[INFO] {0} people have been detectedat the door.".format(len(faces)))

else:
    print("No faces detected")

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image[y:y + h, x:x + w]
    print("[INFO] Face found. Saving locally.")
    cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)

status = cv2.imwrite('faces_detected' + str(dt_string) +'.jpg', image) #saves image as faces_detected.jpg along with the data and time of the image stored in the name
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)

        