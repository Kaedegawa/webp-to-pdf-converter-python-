import os
from PIL import Image


input_folder = os.path.join(os.path.dirname(__file__), "input")
output_pdf = os.path.join(os.path.dirname(__file__), "output", "result.pdf")


os.makedirs(os.path.join(os.path.dirname(__file__), "output"), exist_ok=True)


webp_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".webp")]
if not webp_files:
    print("⚠ No .webp files found in the input folder.")
    exit()

images = []
for filename in sorted(webp_files):  
    webp_path = os.path.join(input_folder, filename)

    
    with Image.open(webp_path) as img:
        img = img.convert("RGB")
        images.append(img)


first_image, *rest_images = images
first_image.save(output_pdf, save_all=True, append_images=rest_images)

print(f" PDF created: {output_pdf}")