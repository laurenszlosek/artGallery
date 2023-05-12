from PIL import Image

def convert_to_bw(image_path, output_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to black and white
    bw_image = image.convert("L")

    # Save the black and white image
    bw_image.save(output_path)
input_image_path = "galleryImages/beforeImages/meBefore.jpeg"  # Replace with the path to your input image file
output_image_path = "galleryImages/afterImages/meAfter.jpeg"  # Replace with the desired output image file path

convert_to_bw(input_image_path, output_image_path)