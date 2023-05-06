import socket
import time
from picamera2 import Picamera2, Preview #linux package, will need to use RPi for this 
from datetime import datetime


SERVER_IP = '127.20.10.4'  # Raspberry Pi IP address
SERVER_PORT = 1230  # Replace with your desired port number. Should be same as port number in client_final.py
BUFFER_SIZE = 1024  # Maximum buffer size to send at once

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

while(1):
    #Lines 17 - 27 obtained from following source
    #source https://raspberrytips.com/picamera2-raspberry-pi/`
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    picam = Picamera2()
    config = picam.create_preview_configuration()
    picam.configure(config)
    picam.start_preview(Preview.QTGL)

    picam.start()
    time.sleep(2) #allow camera to adjust to lighting
    picam.capture_file("image.jpeg") #save image as "image.jpeg"
    print("image captured at ", dt_string) #output message showing time image was captured at

    picam.close()

    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size of 1024 bytes
        with open('image.jpeg', 'rb') as file:
            while True:
                print("sending image info")
                chunk = file.read(BUFFER_SIZE)
                if not chunk: # if all UDP packets have been sent
                    print("finished sending image info")
                    time.sleep(19) #takes photo about every 19+2 = 21 seconds. Line 20 adds 2 seconds, which is why total time is 19+2
                    break
                sock.sendto(chunk, addr) #send UDP package
    

    
