import cv2


def eb():
    # Load the image
    image = cv2.imread('./chessboard_up.png')

    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Save or display the result
    cv2.imwrite('blurred_image.png', blurred_image)
    cv2.imshow('Blurred Image', blurred_image)

if __name__ == '__main__':
    eb()