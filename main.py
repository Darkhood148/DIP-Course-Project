from PIL import Image
import grid
import eb

THRESHOLD_VALUE = 72
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def binary_thresholding(im):
    up_pixels = []
    for i in pixels:
        bw = (i[0] + i[1] + i[2]) / 3
        if bw > THRESHOLD_VALUE:
            up_pixels.append(WHITE)
        else:
            up_pixels.append(BLACK)
    return up_pixels


image_path = 'chessboard.png'
image = Image.open(image_path)
width, height = image.size

image = image.convert('RGB')

pixels = list(image.getdata())

up_pixels = binary_thresholding(pixels)

new_image = Image.new("RGB", (width, height))
new_image.putdata(up_pixels)
new_image.save("chessboard_up.png")
eb.eb()

blurred_image_path = 'blurred_image.png'
blurred_image = Image.open(blurred_image_path).convert("RGB")

grid_img = grid.divide_to_grid(blurred_image)





