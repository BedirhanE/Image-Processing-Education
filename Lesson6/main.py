
"""import cv2

kamera = cv2.VideoCapture(0)


#while döngüsü içerisinde  read fonksiyonunu kullanarak kameradaki  görüntüyü okuma işlemi yapıyoruz
while (True):
    ret, videoGoruntu = kamera.read()
    cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)
    if cv2.waitKey(50) & 0xFF == ord('b'):#b tuşuna basıldığında döngüden çıkıyor ve kamera kapanıyor.
        break

cv2.VideoCapture(0).release()#kamerayı serbest bırakıyoruz
kamera.release()#kamerayı serbest bırakma işlemi.
cv2.destroyAllWindows()#tüm pencereleri kapatma işlemi."""

import tensorflow as tf
# Import TensorFlow Datasets
import tensorflow_datasets as tfds
tfds.disable_progress_bar()

# Helper libraries
import math
import numpy as np
import matplotlib.pyplot as plt