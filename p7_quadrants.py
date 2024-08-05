import cv2

# Load the image
image = cv2.imread('Screenshot.png')

# Get the dimensions of the image
height, width, channels = image.shape

# Calculate the center of the image
center_y = height // 2
center_x = width // 2

# Split the image into four quadrants
top_left = image[0:center_y, 0:center_x]
top_right = image[0:center_y, center_x:width]
bottom_left = image[center_y:height, 0:center_x]
bottom_right = image[center_y:height, center_x:width]

# Display each quadrant
cv2.imshow('Top Left', top_left)
cv2.imshow('Top Right', top_right)
cv2.imshow('Bottom Left', bottom_left)
cv2.imshow('Bottom Right', bottom_right)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()