import cv2, os
import numpy as np
import urllib
import PIL import Image



def get_images_and_labels(path,faceCascade):
    image_paths = [];
    x = 0
    while(x<9):
        image_paths.append("%sm_pic_%d.png" % (path,x));
        image_paths.append("%sr_pic_%d.png" % (path,x));
    images = []
    labels = []

    for image_path in image_paths:
        img = cv2.imread(image_path);
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        image_pil = np.array(gray, 'uint8')
        nbr = 0;
        if "m" in image_path:
            nbr = 1;

        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

        for(x,y,w,h) in faces:
            images.append(image[y: y+h, x: x+w])
            labels.append(nbr)
            print "appending pic with nbr%d" % (nbr);

    return images, labels

def predict(recognizer, img_path_to_test):
    img = cv2.imread(img_path_to_test);
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    image_pil = np.array(gray, 'uint8')
    faces = faceCascade.detectMultiScale(image_pil)
    nbr_predicted, conf = recognizer.predict(predict_image[y: y+h, x:x+w])
    nbr_actual = 0;
    if "m" in image_path:
        nbr_actual = 1;
    if nbr_actual == nbr_predicted:
        print "%d is correctly recognized with confidence: %d" % (nbr_actual, conf)
    else
        print "%d is NOT correctly recognized with confidence: %d" % (nbr_actual, conf)

def take_pic(save_file_path):
    ret, frame = cap.read()
    cv2.imwrite(save_file_path,frame)


def main():
    cap = cv2.VideoCapture(0)
    ##get cascase xml file
    urllib.urlretrieve("https://raw.githubusercontent.com/Itseez/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml","haarcascade_frontalface_default.xml")

    # Create the classifier and run the algorithm
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    recognizer = cv2.createLBPHFaceRecognizer()

    path = "img/"
    images, labels = get_images_and_labels(path,faceCascade)
    recognizer.train(images, np.array(labels))

    #cv2.imwrite("rich_facefound.png",img)

    cap.release()
    exit()


if __name__ == "__main__": main()
