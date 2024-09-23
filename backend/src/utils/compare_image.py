from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
from PIL import Image

before = cv2.imread("before.png")
after = cv2.imread("after.png")

resized_before = cv2.resize(before, (300, 300))
resized_after = cv2.resize(after, (300, 300))

# Convert the images to grayscale
before_gray = cv2.cvtColor(resized_before, cv2.COLOR_BGR2GRAY)
after_gray = cv2.cvtColor(resized_after, cv2.COLOR_BGR2GRAY)

# diff2 = cv2.absdiff(before_gray, after_gray)
# cv2.imshow("diff2", diff2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Compute SSIM between the two images
(score, diff) = ssim(before_gray, after_gray, full=True)
print("Image Similarity: {:.4f}%".format(score * 100))

# The diff image contains the actual image differences between the two images
# and is represented as a floating point data type in the range [0,1]
# so we must convert the array to 8-bit unsigned integers in the range
# [0,255] before we can use it with OpenCV
diff = (diff * 255).astype("uint8")
diff_box = cv2.merge([diff, diff, diff])

# Threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

mask = np.zeros(resized_before.shape, dtype="uint8")
filled = resized_after.copy()

for c in contours:
    area = cv2.contourArea(c)
    if area > 40:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(resized_before, (x, y), (x + w, y + h), (36, 255, 12), 2)
        cv2.rectangle(resized_after, (x, y), (x + w, y + h), (255, 255, 12), 2)
        cv2.rectangle(diff_box, (x, y), (x + w, y + h), (36, 255, 12), 2)
        cv2.drawContours(mask, [c], 0, (255, 0, 0), -1)
        cv2.drawContours(filled, [c], 0, (0, 0, 255), -1)

# cv2.imshow("before", resized_before)
# cv2.imshow("after", resized_after)
cv2.imshow("diff", diff)
# cv2.imshow("diff_box", diff_box)
cv2.imshow("mask", mask)
cv2.imshow("filled after", filled)
cv2.waitKey()


# def overlay_image_alpha(img, img_overlay, x, y, alpha_mask):
#     """Overlay `img_overlay` onto `img` at (x, y) and blend using `alpha_mask`.

#     `alpha_mask` must have same HxW as `img_overlay` and values in range [0, 1].
#     """
#     # Image ranges
#     y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
#     x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

#     # Overlay ranges
#     y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
#     x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

#     # Exit if nothing to do
#     if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
#         return

#     # Blend overlay within the determined ranges
#     img_crop = img[y1:y2, x1:x2]
#     img_overlay_crop = img_overlay[y1o:y2o, x1o:x2o]
#     alpha = alpha_mask[y1o:y2o, x1o:x2o, np.newaxis]
#     alpha_inv = 1.0 - alpha

#     img_crop[:] = alpha * img_overlay_crop + alpha_inv * img_crop


# # Prepare inputs
# x, y = 50, 0
# img = np.array(Image.open("before.png"))
# img_overlay_rgba = np.array(Image.open("after.png"))

# # Perform blending
# alpha_mask = img_overlay_rgba[:, :, 3] / 255.0
# img_result = img[:, :, :3].copy()
# img_overlay = img_overlay_rgba[:, :, :3]
# overlay_image_alpha(img_result, img_overlay, x, y, alpha_mask)

# # Save result
# Image.fromarray(img_result).save("img_result.jpg")
