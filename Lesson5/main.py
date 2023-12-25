# opencv kütüphanesini kullanarak resim üzerine Çizgi, Daire ve Metin Ekleme işlemi yaptık.
import cv2

resim = cv2.imread('image.jpeg')

cv2.imshow('Ornek Resim', resim)
cv2.rectangle(resim, (450, 120), (250, 230), (125, 80, 30), 5)#resim içerisinde dikdörtgen çizme işlemi.

print(resim)
#line fonksiyonu ile resim içerisinde belirlediğimiz koordinata çizgi ekleyebiliriz
cv2.line(resim, (200, 40), (100, 100), (0, 255, 200), 5)

#resime daire ekleme işlemi
cv2.circle(resim, (80, 110),20,(0, 0, 200), 5)

#resime metin ekleme işlemi
cv2.putText(resim,"Bedirhan Education",(190,260),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255,255),2,cv2.LINE_4);

cv2.divide(resim, 2, resim, 1, cv2.CV_32F)#resim içerisindeki pikselleri 2'ye bölme işlemi
#cv2.imshow("pixelleri iki ye bölme işlmei", resim)



cv2.imshow('Dortgen ve Çizgi Eklenmis Resim', resim)
cv2.waitKey(0)
cv2.destroyAllWindows()