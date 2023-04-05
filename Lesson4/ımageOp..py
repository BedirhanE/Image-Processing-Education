

import cv2

resim=cv2.imread('doga.jpg')

cv2.imshow('Ornek Resim',resim)
cv2.rectangle(resim,(350,40),(200,230),(125,40,20),3)
cv2.imshow('Dortgen Eklenmis Resim',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()

#orjinal bir resmin içerisine dörtgen ekleme işleminin basit yolu#

######################################################
#Rectangle Fonksiyonunun Parametreleri
#Dörtgen eklenecek olan resim
#Oluşturulacak olan dörtgenin koordinat başlangıç noktası
#Oluşturulacak olan dörtgenin koordinat bitiş noktası
#RGB renk kodları (değerleri değiştirerek farklı renkler elde edebilirsiniz.)
#Dörtgenin çerçeve kalınlığı
#######################################################