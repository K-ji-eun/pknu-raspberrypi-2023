import cv2
import sys

# 01. 일반이미지
#img = cv2.imread('./Day07/test.jpg')
# 02. 흑백이미지
img = cv2.imread('./Day07/test.jpg')

if img is None:
    print('이미지 로드 실패!')
    sys.exit()

cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

