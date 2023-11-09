from PIL import Image, ImageDraw

# Open the timeline image
image = Image.open("timeline3.png")

# Get the width and height of the image
width, height = image.size

# Define the bar parameters
bar_height = 5
bar_color = (260, 260, 260)  # (255, 0, 0)

###############################################################################

# Define the start and end years
start_year = 155
end_year = 145
dino_name = "diplodocus"

###############################################################################

y_height = 68
# Calculate the X coordinates for the bar
start_x = int(17 + 8.7 * (252 - start_year))
end_x = int(1638 + 8.7 * (66 - end_year))

# Calculate the width of the bar
bar_width = end_x - start_x

# Create the bar image
bar_image = Image.new('RGB', (bar_width, bar_height), color=bar_color)

# Paste the bar onto the timeline image
image.paste(bar_image, (start_x, height - y_height))
# image.paste(bar_image, (start_x, height - 52))

# Create a draw object to draw vertical lines
draw = ImageDraw.Draw(image)

# Define the length of the vertical lines
vertical_line_length = 28

# Draw a vertical line at the start
start_line_x = start_x
start_line_y1 = height - 80
start_line_y2 = start_line_y1 + vertical_line_length
draw.line([(start_line_x, start_line_y1),
          (start_line_x, start_line_y2)], fill=bar_color, width=5)

# Draw a vertical line at the end
end_line_x = start_x + bar_width
end_line_y1 = height - 80
end_line_y2 = end_line_y1 + vertical_line_length
draw.line([(end_line_x, end_line_y1), (end_line_x, end_line_y2)],
          fill=bar_color, width=5)

# Save the final image
image.save(dino_name + "_timline.png")
