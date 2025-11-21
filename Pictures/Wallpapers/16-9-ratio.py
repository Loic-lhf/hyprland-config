from PIL import Image
import os

def convert_to_16_9(input_folder, output_folder=None, method='pad'):
    """
    Convert all images in a folder to 16:9 aspect ratio.
    
    Args:
        input_folder: Path to folder containing images
        output_folder: Path to save converted images (if None, overwrites originals)
        method: 'pad' to add padding (default) or 'crop' to crop the image
    """
    # Create output folder if specified and doesn't exist
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Target aspect ratio
    target_ratio = 16 / 9
    
    # Supported image formats
    formats = ('.jpg', '.jpeg', '.png')
    
    # Process each image
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(formats):
            input_path = os.path.join(input_folder, filename)
            
            try:
                # Open image
                img = Image.open(input_path)
                width, height = img.size
                current_ratio = width / height
                
                # Check if already 16:9 (with small tolerance)
                if abs(current_ratio - target_ratio) < 0.01:
                    print(f"Skipping {filename} - already 16:9")
                    continue
                
                if method == 'crop':
                    # CROP METHOD: Remove excess to fit 16:9
                    if current_ratio > target_ratio:
                        # Image is wider - crop width
                        new_width = int(height * target_ratio)
                        new_height = height
                        crop_x = (width - new_width) // 2
                        crop_y = 0
                    else:
                        # Image is taller - crop height
                        new_width = width
                        new_height = int(width / target_ratio)
                        crop_x = 0
                        crop_y = (height - new_height) // 2
                    
                    # Crop the image (centered)
                    new_img = img.crop((crop_x, crop_y, crop_x + new_width, crop_y + new_height))
                    
                else:
                    # PAD METHOD: Add padding to fit 16:9
                    if current_ratio > target_ratio:
                        # Image is wider - add padding to height
                        new_height = int(width / target_ratio)
                        new_width = width
                    else:
                        # Image is taller - add padding to width
                        new_width = int(height * target_ratio)
                        new_height = height
                    
                    # Create new image with 16:9 ratio (black background)
                    new_img = Image.new('RGB', (new_width, new_height), (0, 0, 0))
                    
                    # Calculate position to paste original image (centered)
                    paste_x = (new_width - width) // 2
                    paste_y = (new_height - height) // 2
                    
                    # Handle transparency for PNG images
                    if img.mode in ('RGBA', 'LA'):
                        new_img = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 255))
                        new_img.paste(img, (paste_x, paste_y), img)
                    else:
                        if img.mode != 'RGB':
                            img = img.convert('RGB')
                        new_img.paste(img, (paste_x, paste_y))
                
                # Determine output path
                if output_folder:
                    output_path = os.path.join(output_folder, filename)
                else:
                    output_path = input_path
                
                # Save with appropriate format
                if filename.lower().endswith('.png'):
                    new_img.save(output_path, 'PNG')
                else:
                    # Convert RGBA to RGB for JPEG
                    if new_img.mode == 'RGBA':
                        rgb_img = Image.new('RGB', new_img.size, (0, 0, 0))
                        rgb_img.paste(new_img, mask=new_img.split()[3])
                        rgb_img.save(output_path, 'JPEG', quality=95)
                    else:
                        new_img.save(output_path, 'JPEG', quality=95)
                
                print(f"Converted {filename}: {width}x{height} -> {new_width}x{new_height} ({method})")
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Example usage
    input_folder = "."  # Change to your folder path
    output_folder = None  # Optional: set to None to overwrite originals
    method = "crop"  # Options: "pad" (add black bars) or "crop" (remove excess)
    
    convert_to_16_9(input_folder, output_folder, method)