from PIL import Image, ImageDraw

image = Image.open("timeline3.png")

width, height = image.size

bar_height = 5
bar_color = (255, 0, 0)

start_year = 157
end_year = 147.7


start_x = int(17 + 8.7 * (252 - start_year))
end_x = int(1638 + 8.7 * (66 - end_year))

bar_width = end_x - start_x
bar_image = Image.new('RGB', (bar_width, bar_height), color=bar_color)


image.paste(bar_image, (start_x, height - 2*bar_height))

image.save("timeline_with_bar.png")
