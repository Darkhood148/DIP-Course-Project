from PIL import Image

def divide_to_grid(image):
    # Check if the image dimensions are compatible with an 8x8 grid of 8x8 squares
    width, height = image.size

    # Define the size of each square
    square_size = width // 8
    grid_size = 8  # 8x8 grid

    if width < square_size * grid_size or height < square_size * grid_size:
        raise ValueError("Image dimensions must be at least 64x64 pixels for an 8x8 grid of 8x8 squares.")

    # List to hold RGB data for each square
    grid_rgb_data = []

    # Loop through each square in the 8x8 grid
    for row in range(grid_size):
        for col in range(grid_size):
            # Calculate the bounding box for the current 8x8 square
            left = col * square_size
            top = row * square_size
            right = left + square_size
            bottom = top + square_size

            # Crop the square from the image
            square = image.crop((left, top, right, bottom))

            # Get RGB pixel values for the 8x8 square
            pixels = list(square.getdata())

            # Append the RGB data for this square to the list
            grid_rgb_data.append(pixels)

    # Now 'grid_rgb_data' contains 64 lists of RGB tuples, one for each 8x8 square
    # for i, square_pixels in enumerate(grid_rgb_data):
    #     print(f"Square {i + 1} pixels:", square_pixels)

    new_image = Image.new("RGB", (width // 8, height // 8))
    new_image.putdata(grid_rgb_data[63])
    # new_image.save("new_image.png")
    new_image.show()

    return grid_rgb_data

if __name__ == "__main__":
    image = Image.open("chessboard.png").convert("RGB")
    grid = divide_to_grid(image)