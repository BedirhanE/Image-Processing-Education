#resim üzerinde piramit oluşturma işlemi
#Gauss Piramidi oluşturma işlemi

import cv2

resim=cv2.imread('doga.jpg')

#bu fonksiyon ile resmi bir üst seviyeye getirerek pixel sayısını artırmış olduk.
piramitustseviye=cv2.pyrUp(resim);
#bu işlem ile resmi bir alt seviyeye getirerek pixel sayısını düşürmüş olduk.
piramitaltseviye=cv2.pyrDown(resim);

cv2.imshow('Piramit Ornek Resim Görüntüsü',resim)
cv2.imshow('Piramit Bir Üst Seviye haliyle  Resim ',piramitustseviye)
cv2.imshow('Piramit Bir Alt Seviye haliyle  Resim ',piramitaltseviye)
cv2.waitKey(0)
cv2.destroyAllWindows()