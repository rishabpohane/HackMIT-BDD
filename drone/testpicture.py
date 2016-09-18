import cv2, os
import numpy as np
import urllib

def get_images_and_labels(path,faceCascade):
    print "starting to get imiages and labels"
    image_paths = [];
    x = 0
    while(x<4):
        image_paths.append("%sm_%d.jpg" % (path,x));
        image_paths.append("%sr_%d.png" % (path,x));
        x = x +1
    images = []
    labels = []

    for image_path in image_paths:
        print "working on this file %s" % (image_path);
        gray = cv2.imread(image_path,0);
        image_pil = np.array(gray, 'uint8')
        nbr = 0;
        if "m" in image_path:
            nbr = 1;

        faces = faceCascade.detectMultiScale(gray)#,scaleFactor=1.1,minNeighbors=5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

        for(x,y,w,h) in faces:
            images.append(image_pil[y: y+h, x: x+w])
            labels.append(nbr)
            print "appending pic with nbr%d" % (nbr);

    return images, labels

def predict(recognizer, faceCascade, img_path_to_test):
    gray = cv2.imread(img_path_to_test,0);
    predict_image= np.array(gray, 'uint8')
    faces = faceCascade.detectMultiScale(predict_image)
    for (x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(predict_image[y: y+h, x:x+w])
        nbr_actual = 0;
        if "m" in image_path:
            nbr_actual = 1;
        if nbr_actual == nbr_predicted:
            print "%d is correctly recognized with confidence: %d" % (nbr_actual, conf)
        else:
            print "%d is NOT correctly recognized with confidence: %d" % (nbr_actual, conf)

def take_pic(save_file_path):
    ret, frame = cap.read()
    cv2.imwrite(save_file_path,frame)


def main():
    #cap = cv2.VideoCapture(0)
    ##get cascase xml file
    urllib.urlretrieve("https://raw.githubusercontent.com/Itseez/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml","haarcascade_frontalface_default.xml")

    # Create the classifier and run the algorithm
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    recognizer = cv2.createLBPHFaceRecognizer()

    #path = "/home/root/hackmit/drone/pic/"
    path = "pic/"
    images, labels = get_images_and_labels(path,faceCascade)
    recognizer.train(images, np.array(labels))

    predict(recognizer, faceCascade, "pic/m_9.jpg")

    #cv2.imwrite("rich_facefound.png",img)

    #cap.release()
    exit()


if __name__ == "__main__": main()
