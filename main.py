from skimage import io, transform
import matplotlib.pyplot as plt
import os
import numpy as np

'''图片旋转'''
img_path = 'images/0.png'
img = io.imread('images/0.png')
img_rotate = transform.rotate(img, angle=30, resize=True)  # 旋转180度，不改变大小
# plt.figure('skimage')
# plt.imshow(img_rotate)

# img2 = transform.resize(img2, (480, 640))
# plt.imshow(img2)
# plt.show()
# print(img2.shape)
# print(img2.dtype)

label_path = img_path.replace(".png", ".txt").replace("images", "labelTxt")
datas = open(label_path, "r").readlines()
for data in datas:
    c_mask = np.full(img.shape[:2], 255)
    data = data.strip("\n").split(" ")
    p1 = (data[0], data[1])
    p2 = (data[2], data[3])
    p3 = (data[4], data[5])
    p4 = (data[6], data[7])
    c_mask[int(float(p1[1])), int(float(p1[0]))] = 1
    c_mask[int(float(p2[1])), int(float(p2[0]))] = 2
    c_mask[int(float(p3[1])), int(float(p3[0]))] = 3
    c_mask[int(float(p4[1])), int(float(p4[0]))] = 4
    label = data[8]
    diff = data[9]
    io.imsave("test.png", c_mask)
    pass
