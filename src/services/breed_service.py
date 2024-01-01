import re

from src.database.database import db_mongo
from src.models.breed_model import BreedModel


class BreedService:

  def get_all_breed(self) -> list:
    breeds = []
    cursor = db_mongo['breed'].find({})
    for document in cursor:
      print(document)
      breeds.append(BreedModel(**document))

    print(breeds)
    return breeds
  
  def get_breed_by_name(self, name: str) -> BreedModel:
    print(name)
    regex_pattern = re.compile(f"^{re.escape(name)}$", re.IGNORECASE)
    breed = db_mongo['breed'].find_one({"breedName": {"$regex": regex_pattern}})
    # breed = db_mongo['breed'].find_one({'breedName': name})

    if breed is None:
      return None

    return BreedModel(**breed)