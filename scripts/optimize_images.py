import os
import subprocess
import sys

def optimize_images():
    raw_dir = "assets/images/raw"
    web_dir = "assets/images/web"

    os.makedirs(web_dir, exist_ok=True)

    if not os.path.exists(raw_dir):
        print(f"Error: {raw_dir} does not exist.")
        return

    images = [f for f in os.listdir(raw_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    print(f"Found {len(images)} images to process...")

    # Try PIL (Pillow) first
    try:
        from PIL import Image
        print("Using Pillow for image processing.")
        for img_name in images:
            raw_path = os.path.join(raw_dir, img_name)
            name_without_ext = os.path.splitext(img_name)[0]

            with Image.open(raw_path) as img:
                # Resize if larger than 1920px wide
                max_width = 1920
                if img.width > max_width:
                    height = int((max_width / float(img.width)) * img.height)
                    img = img.resize((max_width, height), Image.Resampling.LANCZOS)

                # Save as WebP
                webp_path = os.path.join(web_dir, f"{name_without_ext}.webp")
                img.save(webp_path, "WEBP", quality=82)

                # Save as optimized JPEG fallback
                jpg_path = os.path.join(web_dir, f"{name_without_ext}.jpg")
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.save(jpg_path, "JPEG", quality=82, optimize=True)

                raw_size = os.path.getsize(raw_path) / (1024 * 1024)
                webp_size = os.path.getsize(webp_path) / 1024
                jpg_size = os.path.getsize(jpg_path) / 1024
                print(f"Optimized {img_name}: {raw_size:.1f}MB -> WebP: {webp_size:.1f}KB | JPG: {jpg_size:.1f}KB")

    except ImportError:
        print("Pillow not installed. Using macOS 'sips' utility.")
        for img_name in images:
            raw_path = os.path.join(raw_dir, img_name)
            name_without_ext = os.path.splitext(img_name)[0]
            jpg_out = os.path.join(web_dir, f"{name_without_ext}.jpg")
            webp_out = os.path.join(web_dir, f"{name_without_ext}.webp")

            # Compress JPG with sips
            subprocess.run(["sips", "-z", "1280", "1920", "--resampleWidth", "1920", "-s", "format", "jpeg", "-s", "formatOptions", "80", raw_path, "--out", jpg_out], check=False)
            # Try webp with sips
            subprocess.run(["sips", "-s", "format", "webp", raw_path, "--out", webp_out], check=False)

            raw_size = os.path.getsize(raw_path) / (1024 * 1024)
            jpg_size = os.path.getsize(jpg_out) / 1024 if os.path.exists(jpg_out) else 0
            print(f"Processed {img_name}: {raw_size:.1f}MB -> JPG: {jpg_size:.1f}KB")

if __name__ == "__main__":
    optimize_images()
