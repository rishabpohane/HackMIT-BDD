import cv2, os
import numpy as np
import urllib
import time

def get_faces(img_path, faceCascade):
    img = cv2.imread(img_path)
    # And convert to gray-scale for processing
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.array(gray,'uint8')
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
    return faces, gray

def get_images_and_labels(path):
    image_paths = [];
    x = 0
    while(x<2):
        image_paths.append("%sm_%d.jpg" % (path,x));
        image_paths.append("%sr_%d.png" % (path,x));
        x = x +1
    images = []
    labels = []
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

    for image_path in image_paths:
        print "working on this file %s" % (image_path);
        faces, gray = get_faces(image_path,faceCascade);
        nbr = 0;
        if "m" in image_path:
            nbr = 1;

        for(x,y,w,h) in faces:
            images.append(gray[y: y+h, x: x+w])
            labels.append(nbr)
            print "appending pic with nbr%d" % (nbr);

    return images, labels

def predict(recognizer, img_path_to_test):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    faces, gray = get_faces(img_path_to_test,faceCascade);

    for (x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y: y+h, x:x+w])
        nbr_actual = 0;
        if "m" in img_path_to_test:
            nbr_actual = 1;
        if nbr_actual == nbr_predicted:
            print "%d is correctly recognized with confidence: %d" % (nbr_actual, conf)
        else:
            print "%d is NOT correctly recognized with confidence: %d" % (nbr_actual, conf)

def take_pic(save_file_path):
    print "taking pic in .... 4"
    time.sleep(1);
    print "taking pic in .... 3"
    time.sleep(1);
    print "taking pic in .... 2"
    time.sleep(1);
    print "taking pic in .... 1"
    time.sleep(1);
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(save_file_path,frame)
    cap.release()


def main():
    #cap = cv2.VideoCapture(0)
    ##get cascase xml file
    #urllib.urlretrieve("https://raw.githubusercontent.com/Itseez/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml","haarcascade_frontalface_alt.xml")

    # Create the classifier and run the algorithm
    recognizer = cv2.createLBPHFaceRecognizer()

    #path = "/home/root/hackmit/drone/pic/"
    path = "pic/"
    images, labels = get_images_and_labels(path)
    recognizer.train(images, np.array(labels))

    take_pic("pic/r_10.png");

    predict(recognizer, "pic/r_10.png")

    #cv2.imwrite("rich_facefound.png",img)

    #cap.release()
    exit()


if __name__ == "__main__": main()
