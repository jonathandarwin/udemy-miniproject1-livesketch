import cv2
import numpy as np

def sketch(image):
    # step 1 : gambar di grayscale
    # step 2 : gambar di filter menggunakan gaussian blur
    # step 3 : mendeteksi edge pada gambar menggunakan canny
    # step 4 : return gambar yang hitam putih beserta edge nya
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(gaussian, 10, 70)
    ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

# open laptop cam
cap = cv2.VideoCapture(0)

while True:
    # return 2 value -> we only use the frame
    ret, frame = cap.read()
    cv2.imshow('Live Sketcher', sketch(frame))
    # enter pressed -> close
    if(cv2.waitKey(1) == 13) :
        break

cap.release()
cv2.destroyAllWindows()