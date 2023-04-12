#Bu derste de opencv kütüphanesini kullanarak resim üzerine Çizgi, Daire ve Metin Ekleme işlemi yaptık.
import cv2

resim = cv2.imread('image.jpeg')

cv2.imshow('Ornek Resim', resim)
cv2.rectangle(resim, (350, 40), (200, 230), (125, 40, 20), 3)

#line fonksiyonu ile resim içerisinde belirlediğimiz koordinata çizgi ekleyebiliriz
cv2.line(resim, (200, 40), (100, 100), (0, 255, 200), 5)

#resime daire ekleme işlemi
cv2.circle(resim, (80, 110),20,(0, 0, 200), 5)

#resime metin ekleme işlemi
cv2.putText(resim,"Bedirhan Education",(190,260),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255,255),2,cv2.LINE_4);

cv2.imshow('Dortgen ve Çizgi Eklenmis Resim', resim)
cv2.waitKey(0)
cv2.destroyAllWindows()