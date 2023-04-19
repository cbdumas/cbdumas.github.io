from PIL import Image

inp = Image.open("assets/nora_pup.jpg")
inp.save("assets/nora_pup.webp", format="webp", method=6)