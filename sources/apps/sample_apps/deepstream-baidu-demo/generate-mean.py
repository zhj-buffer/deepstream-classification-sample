import PIL
from PIL import Image
import numpy as np

z=np.array([123.675, 116.28, 103.53])               
z=np.expand_dims(np.expand_dims(np.array([124, 117, 104]), axis=0), axis=0)
z=np.broadcast_to(z, (224, 224, 3))
z.shape
Image.fromarray(np.array(z, dtype=np.uint8))
Image.fromarray(np.array(z, dtype=np.uint8)).save('test.ppm')
