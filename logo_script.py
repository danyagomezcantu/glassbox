from PIL import Image, ImageDraw

# Image size
size = (512, 512)
background_color = (255, 255, 255)  # white

# Create image with white background
img = Image.new("RGBA", size, background_color)
draw = ImageDraw.Draw(img)

# Define a translucent light blue color
blue = (173, 216, 230, 100)  # light blue with transparency

# Coordinates for the cube (as a pseudo-3D isometric box)
# Front face
draw.polygon([(156, 200), (356, 200), (356, 400), (156, 400)], fill=blue, outline="purple")
# Top face
draw.polygon([(156, 200), (256, 100), (456, 100), (356, 200)], fill=blue, outline="purple")
# Side face
draw.polygon([(356, 200), (456, 100), (456, 300), (356, 400)], fill=blue, outline="purple")

# Convert to RGB (white background) for export
final_img = Image.new("RGB", size, background_color)
final_img.paste(img, mask=img.split()[3])  # Paste using alpha channel as mask

# Save image
image_path = "C:\\Users\\Danya\\Downloads\\glassbox_cube.png"
final_img.save(image_path)
