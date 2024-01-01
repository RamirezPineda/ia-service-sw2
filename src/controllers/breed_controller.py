
from src.services.breed_service import BreedService

class BreedController:
  
  def __init__(self) -> None:
    self.breed_service = BreedService()

  def get_all_breed(self) -> list:
    breeds = self.breed_service.get_all_breed()
    return breeds
  

  def get_breed_by_name(self, name: str):
    breed = self.breed_service.get_breed_by_name(name)
    return breed