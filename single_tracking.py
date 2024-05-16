import cv2
import sys
from random import randint
# defining the algorithm used
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'MEDIANFLOW', 'CSRT']
tracker_type = tracker_types[4] # can select the object we want to track
print(tracker_type)
#creating the tracking algorithm
if tracker_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting_create()
elif tracker_type == 'MIL':
    tracker = cv2.legacy.TrackerMIL_create()
elif tracker_type == 'KCF':
    tracker = cv2.legacy.TrackerKCF_create()
elif tracker_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow_create()
elif tracker_type == 'CSRT':
    tracker = cv2.legacy.TrackerCSRT_create()
#printing the tracker information
#print(tracker)

#adding video to capture the object and track it
video = cv2.VideoCapture('Videos/race.mp4')
if not video.isOpened():
    print('Error while loading the video!')
    sys.exit()
# reading the first frame
ok, frame = video.read()
if not ok: # printing the error message if not loaded 
    print("Error while loading the frame")
    sys.exit()
#print(ok)

 #end region of interest
bbox = cv2.selectROI(frame)
print(bbox)
# initializing frame
ok = tracker.init(frame, bbox)
#print(ok)

colors = (randint(0,255), randint(0,255), randint(0,255) )
#print(colors)

while True:
    ok, frame = video.read()
    #print(ok)
    if not ok:
        break

    ok, bbox = tracker.update(frame)  # updating frame
    #print(ok,bbox)
    if ok == True:         # True if the tracker is tracking correctly
        (x, y, w, h) = [int(v) for v in bbox]
        #print(x, y, w, h)
        cv2.rectangle(frame, (x,y), (x+w , y+h), colors, 2, 1)
    else: # printing tracking failure message if the tracker fails to track the desired object
        cv2.putText(frame, 'Tracking Failure!', (100,80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)

 # adding specifications to the text printing on the frame
    cv2.putText(frame, tracker_type, (100,20), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)
# displaying the window 
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: #esc
        break

