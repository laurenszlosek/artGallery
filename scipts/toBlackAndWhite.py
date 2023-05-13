from PIL import Image

def convert_to_bw(image_path, output_path):
    image = Image.open(image_path)
    bw_image = image.convert("L")
    bw_image.save(output_path)

input_image_path = "galleryImages/beforeImages/meBefore.jpeg"
output_image_path = "galleryImages/afterImages/meAfter.jpeg"

convert_to_bw(input_image_path, output_image_path)