import cv2
import urllib


urllib.urlretrieve("https://raw.githubusercontent.com/Itseez/opencv/master/data/haarcascades/haarcascade_frontalface_alt.xml","haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

cv2.imwrite('rich_pic.png',frame)

img = frame;

# And convert to gray-scale for processing
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Create the classifier and run the algorithm
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

# For each face found in the image, draw a box around it
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# Write the image back out to a file
cv2.imwrite("rich_facefound.png",img)

cap.release()
exit()
