import cv2
from PIL import Image
Image_path = "Cat1.jpeg"
image = cv2.imread(Image_path)
cat_face_nm = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
cat_face = cat_face_nm.detectMultiScale(image)
cat = Image.open(Image_path)
glasses = Image.open("glasses.png")
cap = Image.open("red_cap.png")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
cap = cap.convert("RGBA")
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w,int(h/3)))
    cat.paste(glasses, (x,int(y+h/4)),glasses)
    cap = cap.resize((w,int(h/1)))
    cat.paste(cap,(x,int(y+h/-2)),cap)
cat.save('cat_with_da_glasses.png')
cat_with_da_glasses = cv2.imread('cat_with_da_glasses.png')
cv2.imshow("doom", cat_with_da_glasses)
cv2.waitKey()