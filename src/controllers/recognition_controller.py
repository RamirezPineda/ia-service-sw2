

from src.services.recognition_service import RecognitionService

class RecognitionController:

  def __init__(self) -> None:
      self.recognition_service = RecognitionService()

  def get_breed(self, image_url: str) -> dict:
    breed_dog = self.recognition_service.get_breed(image_url)
    return breed_dog


  # def get_disease(self, image_url: str) -> dict:
  #   disease_dog = self.recognition_service.get_disease(image_url)
  #   return disease_dog