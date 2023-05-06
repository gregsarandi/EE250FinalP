
Spring 2023 EE 250 Final Project

Team Members:
    1. Kameran Mody
    2. Greg Sarandi


DEMO VIDEO LINK: 
    https://youtu.be/K6HgRhEh0H8
    Video should be 10:02 in length
    If there are any issues with accessing the video or anything else, please contact Greg: sarandi@usc.edu

The four images provided in this submission folder show the functionality of the project:

    image4.jpg shows the image after it has been received from the Rpi server
    faces_detected13/35.jpg shows the image after it has been put through the computer vision facial detection processing
    5353_faces.jpg shows a cropped image of one of the identified faces after processing (this is a false positive)
    798798_faces.jpg shows a cropped image of the other identified face after processing (this is a true positive)


How to compile/execute program:

    server_final.py is a script that initializes a UDP server at a raspberry pi IP address (127.20.10.4). 
    Please note that server_final.py must be run on a Linux-based computer, such as a Raspberry pi.
    To compile and execute server_final.py, type in "python3 server_final.py" to the command line and press enter


    client_final.py is a script that initializes a UDP client to pair with the established UDP server
    Before compiling and executing client_final.py, make sure server_final.py is running.
    Once server_final.py is running, open a new terminal and type in "python3 client_final.py" to the command line and press enter

REQUIRED EXTERNAL LIBRARIES

    cv2

        cv2 is a computer vision python library created by open-source computer vision company "OpenCV"
        This library is used in client_final.py and thus must be installed on the system being used for the client
        Please note that openCV does not perform well on raspberry pi, and thus the client should be a stronger computer, such as a laptop
        Installation instructions can be found online, however this library can be installed using a virtual environment and pip

    picamera2

        picamera2 is a python library for using the Raspberry Pi extension.
        This library is used in server_final.py and thus must be installed on the system being used for the server
        Please not that picamera2 is a linux-based library, and thus must be installed on a Linux-based operating system, such as Raspbian Bullseye
        Installations instructions can be found online, however this library can be installed using pip


    datetime

        Used for taking the exact time at the moment an image was taken/received

    time
        
        Used for stopping the program for a desired amount of seconds and then starting back up

    socket

        Used for creating and maintaining a UDP client-server protocol

REQUIRED EXTERNAL COMPONENTS:

    Raspberry Pi Camera 2

        Note: We used the NoIR version in an attempt to make the system compatible 24 hours a day by allowing for night images using infrared lighting.
        Any Pi Camera 2 Module should work
        Link to component: https://www.canakit.com/raspberry-pi-noir-camera-v2-8mp.html
        If using this component, make sure to upgrade Raspbian OS from Buster to Bullseye


WORKS CITED/REFERENCES:

    OpenCV Face Detection Script: https://www.digitalocean.com/community/tutorials/how-to-detect-and-extract-faces-from-an-image-with-opencv-and-python
    Used in lines 34-60 of client_final.py

    Picamera Script: https://raspberrytips.com/picamera2-raspberry-pi/
    Used in lines 17-27 of server_final.py





