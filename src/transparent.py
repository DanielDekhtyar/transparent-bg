"""
Code to make a given color in the picture transparent
"""

from PIL import Image


def main():
    image, path = get_original_image()

    red, green, blue = get_color_rgb()

    modified_file_name = input("Enter the name of the modified file: ")
    
    # Get rid of the last part of the path. eg. C:\Pictures\image.png -> C:\Pictures
    path = path.rsplit('\\', 1)[0]

    # Get the image data as a list of RGBA tuples
    image_data: list = list(image.getdata())

    # Iterate through each pixel in the image
    for i, pixel in enumerate(image_data):
        # Check if the pixel is white (R=255, G=255, B=255)
        if pixel[0] == red and pixel[1] == green and pixel[2] == blue:
            # Set the pixel to transparent (alpha = 0)
            image_data[i] = (0, 0, 0, 0)

    # Update the image data
    image.putdata(image_data)

    # Save the modified image
    image.save(f"{path}\\{modified_file_name}")


def get_color_rgb():

    rgb_to_change = input(
        "Enter the RGB value of the color you want to change (eg. 255, 255, 255): ")

    red, green, blue = rgb_to_change.split(",")

    red = int(red)
    green = int(green)
    blue = int(green)

    return red, green, blue


def get_original_image():
    # Get the path to the image
    path_to_original_photo = input("Enter the path to the original photo: ")

    # Open the image
    image = Image.open(path_to_original_photo)

    # Convert the image to RGBA mode (if it's not already)
    image = image.convert("RGBA")

    return image, path_to_original_photo


if __name__ == "__main__":
    main()
