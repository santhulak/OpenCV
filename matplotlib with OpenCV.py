import cv2
import numpy as np

import pandas as pd
from matplotlib import pyplot as plt
#import matplotlib as plt

img = cv2.imread('lena.jpg')
#reads in BGR format
cv2.imshow("image",img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# matplot imshow method
# matplot shows image in RBG format
plt.imshow(img)
#To hide the x and y cordinates
plt.xticks([]),plt.yticks([])
#to show matplot window
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()