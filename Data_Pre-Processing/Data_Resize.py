import cv2
import glob
from numpy.lib import math

# gamma1 = 0.2
# gamma2 = 0.3
# gamma3 = 0.4
# gamma4 = 0.5

size = (320,240)

root_path_testing = "D:/Deny/Dataset/Result/RVOT 4 SEC/Gamma 0.8/*.jpg" ## di path mana gambar akan di blend
root_path_saving = "D:/Deny/Dataset/Result/RVOT 4 SEC/Gamma 0.8/"  ## dimana gambar akan disave
file_path = glob.glob(root_path_testing)

# img = cv2.imread(root_path_saving)

# print(img.shape)

for path in file_path:
    img=cv2.imread(path,cv2.IMREAD_UNCHANGED)

    re = cv2.resize(img, size)

    #re = gamma_correction.adjust_gamma(img, gamma4)

    # split filename
    filename = path.split('\\')[-1]
    cv2.imwrite(root_path_saving + filename, re)