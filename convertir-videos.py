import os
import subprocess

# Rutas
INPUT_FOLDER = r"C:\iphone_input"
OUTPUT_FOLDER = r"C:\iphone_output_videos"

# Crear carpeta de salida si no existe
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Recorrer archivos
for filename in os.listdir(INPUT_FOLDER):
    input_path = os.path.join(INPUT_FOLDER, filename)
    name, ext = os.path.splitext(filename.lower())

    # Conversión
    if ext == ".mov":
        output_path = os.path.join(OUTPUT_FOLDER, name + ".mp4")

        command = [
            "ffmpeg", # Abre FFmpeg.
            "-i", input_path, # Input = lee el vídeo que metamos
            "-c:v", "libx264", # Transforma el vídeo usando códec H.264      
            "-preset", "medium", # Velocidad de conversión media
            "-crf", "23", # Calidad           
            "-c:a", "aac", # Transforma el audio al formato AAC          
            "-movflags", "+faststart", # Optimización para subidas a internet
            output_path
        ]

        print(f"Convirtiendo: {filename}")

        try:
            subprocess.run(command, check=True)
            print(f"OK → {output_path}")
        except subprocess.CalledProcessError:
            print(f"ERROR con {filename}")