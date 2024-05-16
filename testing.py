import cv2, sys, os
from random import randint

if not (os.path.isfile('goturn.caffemodel') and os.path.isfile('goturn.prototxt')):
    print('Error loading the network files!')
    sys.exit()


tracker = cv2.TrackerGOTURN_create()