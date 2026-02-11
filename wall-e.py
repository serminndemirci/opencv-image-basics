import urllib.request #urlden fotoğraf indirme ve bu pythonda olan bir kütüphane
import cv2 # opencv import ettim
url= "https://static.wikia.nocookie.net/pixar/images/c/ce/Wall-E_Cubecolors.jpg/revision/latest?cb=20090615011459" 
filename="wall-e.jpg"
urllib.request.urlretrieve(url, filename)
img = cv2.imread(filename)

################ RESIZE
resized = cv2.resize(img, (150,500))

print("Yeni boyut:", resized.shape)


cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("wall-e_resized.jpg", resized)


################ CROP WITH MOUSE 
roi = cv2.selectROI("Select Area", img, showCrosshair=True)
x, y, w, h = roi

crop = img[y:y+h, x:x+w]

cv2.imshow("Crop", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()


################ CENTER CROP 
h, w = img.shape[:2]
crop_w = 200
crop_h = 200
x1 = w // 2 - crop_w // 2
y1 = h // 2 - crop_h // 2
crop = img[y1:y1+crop_h, x1:x1+crop_w]
cv2.imshow("Center Crop", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()


################ TEK BIR PIKSELIN RENGINI DEGISTIRME 
img[-250:-150, -250:-150] = [250, 180, 169] 
cv2.imshow("color",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


################ AYNALAMA 
mirror = cv2.flip(img, 1)
cv2.imshow("Yatay Ayna", mirror)
cv2.waitKey(0)
cv2.destroyAllWindows()


################ GRAYSCALE CONVERSİON
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


################ BLUR ( GÜRÜLTÜ AZALTMA )
blur = cv2.GaussianBlur(img, (15,15), 0)
cv2.imshow("Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


################ EDGE DETECTION
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


################ ROTATE 
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))

cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

################


































