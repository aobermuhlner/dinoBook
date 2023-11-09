from PIL import Image, ImageDraw

# Open the timeline image
image = Image.open("timeline3.png")

# Get the width and height of the image
width, height = image.size

# Define the bar parameters
bar_height = 5
bar_color = (260, 260, 260)  # (255, 0, 0)

###############################################################################

# Define the year
end_year = 70
dino_name = "therizinosaurus"

###############################################################################
start_x = int(17 - 55 + 8.7 * (252 - end_year))

# Load the image to paste
# Replace with your image file
image_to_paste = Image.open("timeline_rex.jpeg")

# Resize the image while maintaining aspect ratio
aspect_ratio = image_to_paste.width / image_to_paste.height
new_width = int(28 * aspect_ratio)
resized_image = image_to_paste.resize((new_width, 28))

# Calculate the position to paste
# Assuming you want to center the image between start_x and end_x
paste_x = start_x
paste_y = image.height - 80

# Paste the image onto the timeline image
if resized_image.mode in ('RGBA', 'LA') or (resized_image.mode == 'P' and 'transparency' in resized_image.info):
    # Use alpha channel as a mask
    mask = resized_image.split()[3]
    image.paste(resized_image, (paste_x, paste_y), mask)
else:
    # Paste without a mask
    image.paste(resized_image, (paste_x, paste_y))

# Save the final image
image.save(dino_name + "_timline.png")
