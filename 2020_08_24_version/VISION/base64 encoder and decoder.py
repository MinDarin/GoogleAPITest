import base64

with open('./temperate4.png', 'rb') as img:
    base64_string = base64.b64encode(img.read())

print(base64_string)
        
############img -> base64##############3


############base64->img
# import base64
# from PIL import Image
# from io image BytesIO
# import matplotlib.pyplot as plt

# img = Image.open(BytesIO(base64.b64decode(base64_string)))
# plt.imshow(img)
