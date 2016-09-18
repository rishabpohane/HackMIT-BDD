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
    while(x<4):
        image_paths.append("%sd_%d.png" % (path,x));
#        image_paths.append("%sr_%d.png" % (path,x));
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


    best_good = 60;
    best_bad = 200;
    return_value = False;
    for (x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y: y+h, x:x+w])
        nbr_actual = 0;
        if "d" in img_path_to_test:
            nbr_actual = 0;
        print "processing face..."

        if nbr_actual == nbr_predicted:
            if(conf < best_good):
                return_value = True;
                best_good = conf
        else:
            if(conf<best_bad):
                best_bad = conf
            
    fo = open("f_status.txt", "w")
    if(return_value):
        fo.write("1\nConf of %d" % (best_good))
        print "Good %d" % (best_good)
    else:
        fo.write("0\nConf of %d" % (best_bad))
        print "bad conf%d" % (best_bad)

    fo.close()

    return return_value

def take_pic(save_file_path):
    print "taking pic in .... 2"
    time.sleep(1);
    print "taking pic in .... 1"
    time.sleep(1);
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(save_file_path,frame)
    cap.release()


def main():
    fo = open("f_status.txt", "w")
    fo.write("0\nConf of 199")
    fo.close()
    #cap = cv2.VideoCapture(0)
    ##get cascase xml file
    #urllib.urlretrieve("https://raw.githubusercontent.com/Itseez/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml","haarcascade_frontalface_alt.xml")

    # Create the classifier and run the algorithm
    take_pic_init_path ="demo_pic/d_0.png"
    take_pic_init_path1="demo_pic/d_1.png"
    take_pic_init_path2 ="demo_pic/d_2.png"
    take_pic_init_path3="demo_pic/d_3.png"
    take_pic(take_pic_init_path)
    take_pic(take_pic_init_path1)
    take_pic(take_pic_init_path2)
    take_pic(take_pic_init_path3)

    time.sleep(5)


    take_pic_path = "demo_pic/cap.png"
    path = "demo_pic/"

    images, labels = get_images_and_labels(path)
    recognizer = cv2.createLBPHFaceRecognizer()
    recognizer.train(images, np.array(labels))

    found_right_face = False;
    while(not found_right_face):
        take_pic(take_pic_path)
        found_right_face = predict(recognizer, take_pic_path)

    exit()


if __name__ == "__main__": main()
