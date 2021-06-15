
import socket


import numpy

import cv2

#creating the socket
s=socket.socket() # default it takes IPV4 adress family and TCP protocol
print("\t SOCKET CREAETED \t")

#Connecting with server
ip="192.168.141.116" # IP of server
port=1234 # port of server program
s.connect((ip,port))
print("\t CONNECTED WITH THE SERVER \t")

cap=cv2.VideoCapture(0)
while True:
    r,photo=cap.read()
    p_data=cv2.imencode('.jpg',photo)[1].tobytes() #encoding the data captured by the camera to send in packet
    s.sendall(p_data) # sending the data

    data=s.recv(100000000)
    darray=numpy.frombuffer(data,numpy.uint8) #creating array of recevied data
    photo=cv2.imdecode(darray,cv2.IMREAD_COLOR) # decoding the video stream
    if type(photo)is type(None): #checking wheteher the image is None , if it is discarding it
        pass
    else:
        cv2.imshow("Person B on video Call", photo) # displaying the window of videochat
        if cv2.waitKey(10)==13: #13 for enter key waits as long as enter key is pressed
            break


cv2.destroyAllWindows() 
cap.release() 