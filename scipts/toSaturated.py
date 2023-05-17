from PIL import Image, ImageEnhance

def staturate_image(image_path, output_path,saturation_level):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Color(image)
    saturated_s = enhancer.enhance(saturation_level)
    saturated_s.save(output_path)

input_image_path = "galleryImages/beforeImages/viewBefore.jpg"
output_image_path = "galleryImages/afterImages/viewAfter.jpg"

staturate_image(input_image_path, output_image_path,saturation_level=3)