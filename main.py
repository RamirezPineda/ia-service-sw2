
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import recognition_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(prefix="/api",router=recognition_route.router)



# from transformers import ViTImageProcessor, ViTForImageClassification
# from PIL import Image
# import requests

# url = 'https://blog.mascotaysalud.com/wp-content/uploads/2019/05/CARA-ROTTWEILER.jpg'
# image = Image.open(requests.get(url, stream=True).raw)

# processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
# model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

# inputs = processor(images=image, return_tensors="pt")
# outputs = model(**inputs)
# logits = outputs.logits
# # model predicts one of the 1000 ImageNet classes
# predicted_class_idx = logits.argmax(-1).item()
# print("Predicted class:", model.config.id2label[predicted_class_idx])

import json
import requests
    
    

