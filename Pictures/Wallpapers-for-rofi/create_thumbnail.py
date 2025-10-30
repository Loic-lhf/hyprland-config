import os
import sys
from PIL import Image

def crop_image(image_path, crop_box, output_path="Pictures/Wallpapers-for-rofi/thumbnail.jpg"):
    """Crop an image using the given coordinates and save the result."""
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"❌ Error: File '{image_path}' not found.")
        return

    if image_path.endswith("png"):
        image = image.convert('RGB')

    cropped = image.crop(crop_box)
    cropped.save(os.path.expanduser(os.path.join('~', output_path)))
    print(f"✅ Cropped image saved as '{output_path}'")

if __name__ == "__main__":
    # Check if the user passed an argument
    if len(sys.argv) < 2:
        print("Usage: python crop.py <image_path> [left top right bottom]")
        sys.exit(1)

    image_path = sys.argv[1]

    # If the user provides crop coordinates, use them
    if len(sys.argv) == 6:
        try:
            crop_box = tuple(map(int, sys.argv[2:6]))
        except ValueError:
            print("❌ Coordinates must be integers.")
            sys.exit(1)
    else:
        # Default crop box
        image = Image.open(image_path)
        width, height = image.size  # returns a tuple (width, height)
        print(image.size)
        x_start = round(width*(403/1920))
        y_start = round(height*(316/1080))
        x_width = round(width*(555/1920))
        y_height = round(height*(490/1080))
        crop_box = (x_start, y_start, x_start+x_width, y_start+y_height)

    crop_image(image_path, crop_box)
    
# 3840, 2160