import os
import colorsys
import numpy as np
import cv2 as openCV


# Boş görüntü oluştur.
zeros = np.zeros([100,100])
openCV.imshow("black", zeros)


openCV.namedWindow("BlackImage", openCV.WINDOW_NORMAL)

# Görüntü oku.
image = openCV.imread("McQueen.jpg")
openCV.imshow("MissionImpossible", image)

# RGB'den Grayscale çevir.
image_gray = openCV.cvtColor(image, openCV.COLOR_BGR2GRAY)

# Görüntüyü Kaydet.
openCV.imwrite("McQueen_Gray.jpg", image_gray)

# Belirli pixel değerlerini oku. tam ortası pixelin değeri.
print(type(image.shape[0]))
print(image[image.shape[0] / 2][image.shape[1] / 2])

# RGB değerleri HSV değerlerine çevir. sadece r'yi göster. sadece v göster
(b, g, r) = image[10][15]
print(r)
(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
print(v)
print(f"HSV: {h:.2f}, {s:.2f}, {v:.2f}")

openCV.waitKey(0)

openCV.destroyAllWindows()

#%%
# 5 Görüntü Oku, İsimlerini Değiştir.
file_path = os.getcwd()
destination_path = os.getcwd() + "\Circles"

file_list = os.listdir(file_path)

circle_images = []

for count, filename in enumerate(file_list):
    if filename.endswith(".png"):
        circle = openCV.imread(filename)
        circle_images.append(circle)
        name = f"Circle {str(count)}.jpg"
        source = f"{file_path}\{filename}"
        destination = f"{destination_path}\{name}"
        os.rename(source, destination)

print(len(circle_images))


#%%
# Görüntüye yazı ekle.
text_image = openCV.putText(image,
                            "Kachika Kachika",
                            (500,650),
                            openCV.FONT_HERSHEY_SIMPLEX,
                            1,
                            (255, 255, 255),
                            2,
                            openCV.LINE_AA)

# Görüntüye daire ekle.
text_image = openCV.circle(image_gray,
                             (800, 540),
                             35,
                             (0,0,0),
                             -1)

# Görüntüye kare ekle.
text_image = openCV.rectangle(image_gray,
                              (900, 750),
                              (1100, 850),
                              (0,0,0),
                              2)

openCV.imshow("McQueen_Edited", text_image)

#%%
# Görüntüyü Döndür.
rotated_image = openCV.rotate(image, openCV.ROTATE_90_CLOCKWISE)
openCV.namedWindow("RotetedMcQueen", openCV.WINDOW_NORMAL)
openCV.imshow("RotetedMcQueen", rotated_image)
openCV.waitKey(0)

# Görüntüyü küçült.
width = int(image.shape[1] * 0.2)
height = int(image.shape[0] * 0.2)
smalled_image = openCV.resize(image, (width, height))
openCV.imshow("SmalledMcQueen", smalled_image)
openCV.waitKey(0)

#%%
# Görüntüyü taşı
move_matrix = np.float32([[1, 0, 100], [0, 1, 100]])
dimensions = (image.shape[1], image.shape[0])
moved_image = openCV.warpAffine(image, move_matrix, dimensions)
openCV.imshow("MovedMcQueen", moved_image)
openCV.waitKey(0)

#%%
# Görüntüleri bulanıklaştırma
blured_image = openCV.GaussianBlur(image, (15,15), 0)
openCV.imshow("BlurredMcQueen", blured_image)
openCV.waitKey(0)

#%%
# Görüntüde Gürültüden Kurtulma.
termometer = openCV.imread("Termometer.jpg", 0)
openCV.imshow('normal', termometer)  
se=openCV.getStructuringElement(openCV.MORPH_RECT , (8,8))
bg=openCV.morphologyEx(termometer, openCV.MORPH_DILATE, se)
out_gray=openCV.divide(termometer, bg, scale=255)
out_binary=openCV.threshold(out_gray, 0, 255, openCV.THRESH_OTSU)[1] 

openCV.imshow('binary', out_binary)  

openCV.waitKey(0)