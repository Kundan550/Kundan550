
import cv2
import socket
import numpy

#creating the socket
s=socket.socket() # default it takes IPV4 adress family and TCP protocol
print("\t SOCKET CREAETED \t")

#binding ip and port
ip="" # to use IP associaited with this device
port=1234 # can be given any  free port within a valid range
s.bind((ip,port)) 
print("\t BINDED ADDRESS WITH THIS PROGRAM  \t")

#listening and accepting the connection
s.listen(5)
c,addr=s.accept()
print("\t CONNECTION ACCEPTED \t")


cap=cv2.VideoCapture(0) 
while True:
    data=c.recv(100000000) 
    darray=numpy.frombuffer(data,numpy.uint8) #creating array of recevied data
    photo=cv2.imdecode(darray,cv2.IMREAD_COLOR) # decoding the video stream
    if type(photo)is type(None): #checking wheteher the image is None , if it is discarding it
        pass
    else:
        cv2.imshow("PersonA on video Call", photo) # displaying the window of videochat
        if cv2.waitKey(10)==13: #13 for enter key waits as long as enter key is pressed
            break #exiting
    r,photo=cap.read() 
    p_data=cv2.imencode('.jpg',photo)[1].tobytes() #encoding the data captured by the camera to send in packet
    c.sendall(p_data) # sending the data
cv2.destroyAllWindows() 
cap.release() 