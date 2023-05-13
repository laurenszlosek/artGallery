from PIL import Image, ImageOps

def invert_colors(image_path, output_path):
    image = Image.open(image_path)
    inverted_image = ImageOps.invert(image)
    inverted_image.save(output_path)

image_path = "galleryImages/beforeImages/starrynightBefore.jpeg"
output_path = "galleryImages/afterImages/starrynightAfter.jpeg"

invert_colors(image_path, output_path)

