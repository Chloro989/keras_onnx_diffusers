import random
import datetime
import os
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import numpy as np
import matplotlib.pyplot as plt
from diffusers import StableDiffusionOnnxPipeline

# Check if directory exists
if os.path.exists("output/"):
    print("ouput path confirmed")
else:
    # Create directory
    os.makedirs("output/")

# Height and Width
H = 512
W = 512

# Set Pipe
pipe = StableDiffusionOnnxPipeline.from_pretrained("model/stable_diffusion_onnx", provider="DmlExecutionProvider")

# Negative Prompt
NP = ("NSFW,watermark,bad face,bad hand,bad face shape,extra hands,extra fingers,bad arm,extra arms,missing leg,detached arm,"
      "inverted hand,ugly,bad eyes,logo,worst quality,blurry,bad anatomy,awful,separated,unpleasant quality")

# Text to Image
def text_to_image(text,num_images_per_prompt=1):
    text = "best quality,master piece,ultra detailed,4K quality,breathtaking,authentic" + text
    for _ in range(num_images_per_prompt):
        image = pipe(str(text),
                     negative_prompt = NP,
                     height= H, width= W,
                     num_inference_steps = 96,  # Number of iterations (controls image quality)
                     guidance_scale = 7.2,
                     eta = 0.1,
                     num_images_per_prompt = 1,
                    ).images[0]
    
        # Display each image
        plt.imshow(image)
        plt.axis('off')  # to hide the axis
        plt.show()

        # Save Image
        pnginfo = PngInfo()
        pnginfo.add_text('prompt', text)
        image.save("output/" + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')) + ".png", pnginfo=pnginfo)
        print("***"\
             " saved at 'output/' "\
             "***")
# Execution
text = input("Enter Prompt Here"\
             " Use Coron ->, to separate words:" )
cnt = int(input("Enter the Number of Images You Want to Create: "))
text_to_image(text,num_images_per_prompt=cnt)