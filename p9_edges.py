import cv2

def display_image(image, title="Image"):
    cv2.imshow(title, image)

image_path = 'rose.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()

edges = cv2.Canny(img, 100, 200)
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow("Original Image", img)
cv2.imshow("Edges Detected", edges)
cv2.imshow("Blurred Image", blurred_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
