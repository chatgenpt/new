import cv2

# Function to display an image
def display_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load and process the image
image_path = 'input_image.jpg'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

display_image(img, "Contoured Image")
