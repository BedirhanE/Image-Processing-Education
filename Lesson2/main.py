
import cv2

#cerceve rengini belirlediğim işlem
cerceve_rengimiz=[144, 12, 63 ]

resim=cv2.imread('kalem.jpg')

#çerceve işlemini yapacağım resmin yolu
#cerceve=cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_CONSTANT,value=cerceve_rengimiz)
#cerceve=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_REFLECT)
#cerceve=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_REPLICATE)
cerceve=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_WRAP)

#cerceve işlemi için borderType Türleri
"""cv2.BORDER_CONSTANT: #Belirlenen renkte çerçeve ekler.
   cv2.BORDER_REFLECT: #Resmin sınırlar ayna efekti eklenir.
   cv2.BORDER_REPLICATE: #Resmin belirlenen piksel alanından çekme yapılmış gibi bir görüntü verir.
   cv2.BORDER_WRAP: #Son elemanının belli bir kısmında kesme işlemi yapar."""

cv2.imshow("kalem",cerceve)
cv2.waitKey(0)
cv2.destroyAllWindows()