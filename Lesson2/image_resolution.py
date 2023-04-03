
#ojinal resmin çözünürlüğüne göre bencere boyutlandırma

import cv2

resim=cv2.imread('doga.jpg')#resmi okumak için ,resmi resim değişkenine atıyorum


cozunurluk=480,720


resim_genislik_olcegi = cozunurluk[0] / resim.shape[1]
resim_yukseklik_olcegi = cozunurluk[1] / resim.shape[0]
yeni_olcek_degeri=min(resim_genislik_olcegi,resim_yukseklik_olcegi)
pencere_genislik= int(resim.shape[1]*yeni_olcek_degeri)
pencere_yukseklik=int(resim.shape[0]*yeni_olcek_degeri)



cv2.namedWindow('doga',cv2.WINDOW_NORMAL)
cv2.resizeWindow('doga',pencere_genislik,pencere_yukseklik)


#resmi ekranda görüntüle pencereyi hemen kapama bekle ve herhangi bir tuşa basınca pencereyi kapama işlemi
cv2.imshow('doga',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()