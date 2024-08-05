import cv2

# Function to display an image
def display_image(image, title="Image"):
    cv2.imshow(title, image)

# Load an image
image_path = 'input_image.jpg'
img = cv2.imread(image_path)

# Check if image loading was successful
if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()

# Apply Gaussian Blur
blurred_img_gaussian = cv2.GaussianBlur(img, (11, 11), 0)  # Kernel size (11, 11), sigma = 0

# Apply Median Blur
blurred_img_median = cv2.medianBlur(img, 5)  # Kernel size 5x5

# Display all images in separate windows
display_image(img, "Original Image")
display_image(blurred_img_gaussian, "Gaussian Blur")
display_image(blurred_img_median, "Median Blur")

# Wait for user input to close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
