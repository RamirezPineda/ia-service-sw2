import time
import requests

from fastapi import HTTPException
# import tensorflow as tf
# import cv2 as cv
# import numpy as np


from src.config.constants import HEADERS, API_URL_MICROSOFT
from src.utils.file_utils import FileUtils


# classes=['Bacterial', 'Hongos', 'Saludable', 'Hipersensibilidad']



class RecognitionService:


  # def __init__(self):
    # self.model = "./src/models/model_finetuned1_10-0.98.tflite"

  
  def get_breed(self, image_url):
    response_image = requests.get(image_url)
    
    if response_image.status_code != 200:
      raise HTTPException(status_code=404, detail="Error al descargar la imagen")
    
    local_path = FileUtils.save_file(image_url, response_image.content)

    data = FileUtils.read_file(local_path)

    max_attempts = 2
    current_attempt = 1

    while current_attempt <= max_attempts:
        response = requests.post(API_URL_MICROSOFT, headers=HEADERS, data=data)

        print(response.json())
        data_list = response.json()

        if 'error' not in data_list:
            # La solicitud fue exitosa, salimos del bucle
            break

        print(f"Intento {current_attempt} fallido. Esperando 21 segundos antes de reintentar.")
        time.sleep(21)  # Esperar 21 segundos

        current_attempt += 1

    
    if 'error' in data_list:
      raise HTTPException(status_code=404, detail=data_list['error'])


    FileUtils.remove_file(local_path)

    return data_list
  
  

  # def get_disease(self, image_url: str):
  #   response_image = requests.get(image_url)
    
  #   if response_image.status_code != 200:
  #     raise HTTPException(status_code=404, detail="Error al descargar la imagen")
    
  #   local_path = FileUtils.save_file(image_url, response_image.content)

  #   image_bytes = FileUtils.read_file(local_path)

  #    # Convertir los bytes de la imagen a un array numpy
  #   nparr = np.frombuffer(image_bytes, np.uint8)
  #   image = cv.imdecode(nparr, cv.IMREAD_COLOR)

  #   interpreter = tf.lite.Interpreter(model_path=self.model)

  #   input_details = interpreter.get_input_details()
  #   output_details = interpreter.get_output_details()

  #   interpreter.allocate_tensors()


  #   new_img = cv.resize(image, (224, 224))
  #   new_img = new_img.astype(np.float32)
  #   new_img = new_img / 255

  #   interpreter.set_tensor(input_details[0]['index'], [new_img])

  #   # run the inference
  #   interpreter.invoke()

  #   # output_details[0]['index'] = the index which provides the input
  #   output_data = interpreter.get_tensor(output_details[0]['index'])

  #   print(output_data)

  #   class_idx = np.argmax(output_data[0])

  #   print(class_idx)

  #   FileUtils.remove_file(local_path)
    
  #   return {
  #       'prediction': classes[class_idx],
  #       'accuracy': round(output_data[0][class_idx] * 100)
  #   }

    
