import cv2, sys, os
from random import randint
#adding framework to the neural network
if not (os.path.isfile('goturn.caffemodel') and os.path.isfile('goturn.prototxt')):
    print('Error loading the network files!')
    sys.exit()
#creating the algorithm
tracker = cv2.TrackerGOTURN_create()
#importing the video from our system
video = cv2.VideoCapture('Videos/race.mp4')
if not video.isOpened():
    print('Error while loading the video!')
    sys.exit()
#reading the first frame
ok, frame = video.read()
if not ok:
    print('Erro while loading the frame!')
    sys.exit()
# selecting the object
bbox = cv2.selectROI(frame) # region of interest
#initializing the frame
ok = tracker.init(frame, bbox)
#adding colors to the bounding box
colors = (randint(0, 255), randint(0, 255), randint(0, 255))
#adding conditions to the reading of frames
while True:
    ok, frame = video.read()
    if not ok:
        break
#updating the frames
    ok, bbox = tracker.update(frame)
    if ok == True:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), colors, 2)
    else:
        cv2.putText(frame, 'Tracking failure!', (100,80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255))
# adding text on the frame
    cv2.putText(frame, 'GOTURN', (100, 20), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255))
# displaying the video
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: # esc
        break


