#kullanıcağım OpenCV kütüphanesini import etttim.
import cv2

image = cv2.imread("doga.jpg") #resmi dosyadan orjinal hali ile okuma işlemi.
cv2.imshow("doga",image)  #resmi ekranda gösterme işlemi
#cv2.imwrite("doga.png",resim) #png uzantılı resim oluşturma işlemi.

#resimdeki RGB özelliklerini incelemek için
#resmimde  herhangi bir pikselin renk değerini görüntülemek için
print ("100x100'lük Alan İçin Mavi Renk Değeri:" + str(image.item (100,100,0)))
print ("200x200'lük Alan İçin Yeşil Renk Değeri:" + str(image.item (200,200,1)))
print ("200x200'lük Alan İçin Kırmızı Renk Değeri:" + str(image.item (200,200,2)))

#resmime ait genişlik ve yükseklik değerlerini ekranda görüntülemek için.
yukseklik = image.shape[0]
genislik = image.shape[1]
print('Resim Yüksekliği (px)      :', yukseklik)
print('Resim Genişliği  (px)     :', genislik)

cv2.waitKey(0) # resmimi pencerede sabit olarak kalması  ve herhangi bir tuşabasınca kaybolması işlemini gerçekleştirdik.
cv2.destroyAllWindows()
#resim = cv2.imread("everest.jpg",0) #resme sıfır parametresini göndererek resmi gri tonda filtrelemiş oluyorum.