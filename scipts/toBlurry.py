from PIL import Image, ImageFilter

def blur_image(image_path, output_path):
    # reading Image
    image = Image.open(image_path)

    # blurring using GaussianBlur
    # radius decides the intesity of blur
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=15)) 
    
    # saving the image
    blurred_image.save(output_path)

image_path = "galleryImages/beforeImages/signBefore.jpg"
output_path = "galleryImages/afterImages/signAfter.jpg"

blur_image(image_path, output_path)