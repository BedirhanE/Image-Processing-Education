

#kullanıcağım kütüphaneleri import ettim
import  cv2
#import  numpy as np

#resmi kaydet fonksiyonu içerisinde jpg formatındaki resmi farklı kalitelerde kaydetme işlemini ve
#png yi sıkıştırma işlemi yöntemini bu fonksiyon içerisinde yapmış oldum
def resmiKaydet(path,image,jpg_quality=None,png_compress=None):
    if jpg_quality:
        cv2.imwrite(path,image,[int(cv2.IMWRITE_JPEG_QUALITY),jpg_quality])
    elif png_compress:
        cv2.imwrite(path,image,[int(cv2.IMWRITE_PNG_COMPRESSION),png_compress])
    else:
        cv2.imwrite(path,image)

#resmiKaydet fonksiyonunu  ana fonksiyon içerisinde çağırıp kullanıyorum
def main():
    resimYolu="istanbul.jpg"
    resim=cv2.imread(resimYolu)
    cv2.imshow('istanbul',resim)

# değişim farkını görmek için tekrardan yeni bir resim  okuyup kaydettim.
    son_jpg="istanbulJPG.jpg"
    resmiKaydet(son_jpg,resim,jpg_quality=6)

#png sıkıştırması yaptığım kısım
    son_png = "istanbulPNG.png"
    resmiKaydet(son_png,resim,png_compress=9)

#ekranda resmin kaybolmadan gözükmesi işlemi
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()


#OpenCV de Format Ve çözünürlük işlemleri

""" IMWRITE_JPEG_QUALITY fonksiyonu belirli bir kalite düzeyiyle görüntüyü kaydetmek için kullanılan
 JPEG sıkıştırma algoritmasını kontrol etmek için kullanılan  bir parametredir.Bu fonksiyon kullanılarak
 kalite düzeyi ayarlanabilir  ve böylece dosya boyutu  ve görüntü kalitesi arasında bir denge sağlanabilir.
"""