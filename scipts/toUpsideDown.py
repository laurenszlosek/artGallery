from PIL import Image

def flip_image(image_path, output_path):
    # Open an image file
    image = Image.open(image_path)
    # Flip the image
    flipped_image = image.rotate(180)
    # Save the flipped image
    flipped_image.save(output_path)

image_path = "galleryImages/beforeImages/monalisaBefore.jpg"
output_path = "galleryImages/afterImages/monalisaAfter.jpg"

flip_image(image_path, output_path)
