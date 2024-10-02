import cv2
import numpy as np
import scipy.ndimage

a= cv2.imread('ultrasound_muscle.png')
a=cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

k= np.ones((5,5))/25
b = scipy.ndimage.convolve(a, k)
cv2.imwrite('mean_output.png',b)

cv2.imshow('original',a)
cv2.imshow('suave',b)

cv2.waitKey(0)
cv2.destroyAllWindows()