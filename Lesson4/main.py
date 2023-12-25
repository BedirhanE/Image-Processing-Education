#resim üzerinde piramit oluşturma işlemi
#Gauss Piramidi oluşturma işlemi

import cv2

resim=cv2.imread('doga.jpg')

print("Resmin Boyutu:",resim.size)#resmin size değerini yazdırdık.
print("Resmin Şekli:",resim.shape)#resmin shape değerini yazdırdık.(Yükseklik genişlik ve renk kanal sayısı)
print("Resmin İçerik değerleri:",resim)#resmin içeriğini yazdırdık.

#bu fonksiyon ile resmi bir üst seviyeye getirerek pixel sayısını artırmış olduk.
piramitustseviye=cv2.pyrUp(resim);
#bu işlem ile resmi bir alt seviyeye getirerek pixel sayısını düşürmüş olduk.
piramitaltseviye=cv2.pyrDown(resim);

cv2.imshow('Piramit Ornek Resim Görüntüsü',resim)
cv2.imshow('Piramit Bir Üst Seviye haliyle  Resim ',piramitustseviye)
cv2.imshow('Piramit Bir Alt Seviye haliyle  Resim ',piramitaltseviye)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""import cv2

#resim üzerinde piramit oluşturma işlemi.

# Resmi okuyun
img = cv2.imread('doga.jpg')

# Piramit oluşturun
pyramid = [img]
for i in range(4):
    pyramid.append(cv2.pyrDown(pyramid[-1]))

# Piramidi gösterin
for i in range(len(pyramid)):
    cv2.imshow('Level ' + str(i), pyramid[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""

