#kullanıcağım OpenCV kütüphanesini import etttim.
import cv2


image = cv2.imread("doga.jpg") #resmi dosyadan orjinal hali ile okuma işlemi.
cv2.imshow("doga",image)  #resmi ekranda gösterme işlemi
cv2.imwrite("doga.png",image) #png uzantılı resim oluşturma işlemi.
print("Resmin Pİxel Değerleri:",image) #resmin piksel değerlerini ekranda gösterme işlemi.

#resimdeki RGB özelliklerini incelemek için
#resmimde  herhangi bir pikselin renk değerini görüntülemek için BGR değerlerini kullanıyorum.
print ("100x100'lük Alan İçin Mavi Renk Değeri:" + str(image.item (100,100,0)))
print ("200x200'lük Alan İçin Yeşil Renk Değeri:" + str(image.item (200,200,1)))
print ("200x200'lük Alan İçin Kırmızı Renk Değeri:" + str(image.item (200,200,2)))

#resmime ait genişlik , yükseklik  ve Derinlik değerlerini ekranda görüntülemek için.
yukseklik = image.shape[0]
genislik = image.shape[1]
derinlik = image.shape[2]

print('Resim Yüksekliği (px)      :', yukseklik)#resim yüksekliğini piksel cinsinden döndürür.
print('Resim Genişliği  (px)     :', genislik)#resim genişliğini piksel cinsinden döndürür.
print('Piksel Derinliği (bit)    :', derinlik)#resimdeki her bir pikselin 3 renk kanalı olduğu için 3 değeri döndürür.

cv2.waitKey(0) # resmimi pencerede sabit olarak kalması  ve herhangi bir tuşabasınca kaybolması işlemini gerçekleştirdik.
cv2.destroyAllWindows()#pencereyi kapatma işlemi.
#resim = cv2.imread("doga.jpg",0) #resme sıfır parametresini göndererek resmi gri tonda filtrelemiş oluyorum.

#Resmi Gri tonda ekrana yazdırma işlemi
cv2.imshow("doga",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Resmin Gri Tonlamalı Hali:",image)