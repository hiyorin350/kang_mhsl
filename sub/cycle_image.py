import numpy as np
import cv2
import conversions

# 画像の読み込み
image = cv2.cvtColor(cv2.imread('images/chart26/chart26.ppm'), cv2.COLOR_BGR2RGB)

height, width, channels = image.shape
N = height * width

hsl_image = conversions.rgb_to_hsl(image)
mhsl_image = conversions.hsl_to_mhsl(hsl_image)

flat_hsl = mhsl_image.reshape(N, 3)

hsl_out = np.zeros_like(image)

u = np.array([ -0.10725397, 0.99423166, 0.])
optimum_theta = (np.arctan2(u[1], u[0]))
print(np.rad2deg(optimum_theta))
dichromatic_theta = 50.19789 #ls=50での2色覚平面

cycled_hsl_image = mhsl_image.copy()
print(cycled_hsl_image[100, 100, 0])
cycled_hsl_image[:, :, 0] = (cycled_hsl_image[:, :, 0] + (dichromatic_theta - np.rad2deg(optimum_theta) + 90)) % 360
cycled_hsl_image[:, :, 0] = cycled_hsl_image[:, :, 0]
print(cycled_hsl_image[100, 100, 0])

# 色相を調整
# mhsl_image[:, :, 0] = (mhsl_image[:, :, 0] + (dichromatic_theta - (np.rad2deg(optimum_theta)) + 90)) % 360

img_out = cv2.cvtColor(conversions.hsl_to_rgb(conversions.mhsl_to_hsl(cycled_hsl_image)), cv2.COLOR_RGB2BGR)

# 回転された画像を表示
cv2.imwrite('images/chart26/chart26_kang_plus_rotate_mhsl.ppm',img_out)
cv2.imshow('cycle_image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()