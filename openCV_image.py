import time
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('cat.jpeg')

# print(image.shape)
# print(image.size)
#
# # 이미지 numpy 객체의 특정 픽셀을 가리킵니다
# px = image[100,100]
#
# #BRG 순서로 출력
# #( 단 Gray Scale 인 경우는 BGR로 구분되지 않음)
# print(px)
#
# # R 값만 출력
# print(px[2])

# start_time = time.time()
# for i in range(0,100):
#     for j in range(0, 100):
#         image[i, j] = [255,255,255]

# image[0:100, 0:100] = [0, 0, 0]
# print("--- %s seconds ---" % (time.time() - start_time))


#  Numpy slicing : ROI 처리 가능
# roi = image[200:350, 50:200]
#ROI 단위로 이미지 복
# image[0:150, 0:150] = roi

image[:,:,2]=0

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()