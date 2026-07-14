import os
from PIL import Image
import pillow_heif

# Activar soporte HEIC
pillow_heif.register_heif_opener()

# Rutas
INPUT_FOLDER = r"C:\iphone_input"
OUTPUT_FOLDER = r"C:\iphone_output_videos"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    input_path = os.path.join(INPUT_FOLDER, filename)
    name, ext = os.path.splitext(filename.lower())

    # Solo fotos HEIC del iPhone
    if ext == ".heic":
        output_path = os.path.join(OUTPUT_FOLDER, name + ".png")

        try:
            img = Image.open(input_path)
            img.save(output_path, "PNG")
            print(f"OK → {filename}")
        except Exception as e:
            print(f"ERROR con {filename}: {e}")