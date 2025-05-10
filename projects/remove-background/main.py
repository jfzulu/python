from rembg import remove
from PIL import Image
input_path= "photo.jpg"
output_path= "photoBG.png"
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open("photoBG.png")