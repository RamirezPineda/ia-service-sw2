from fastapi import APIRouter, UploadFile

from src.controllers.recognition_controller import RecognitionController
from src.controllers.breed_controller import BreedController

controller = RecognitionController()
breedController = BreedController()

router = APIRouter()

from pydantic import BaseModel


class Image(BaseModel):
    image_url: str


@router.get('/hello')
def read_root():
  return {"Hello": "World"}

@router.post("/recognition/breed", tags=["Breed Recognition"])
def get_breed(image: Image):
  print(image)
  return controller.get_breed(image.image_url)


@router.get("/breeds", tags=["Breeds"])
def get_all_breed():
  return breedController.get_all_breed()

@router.get("/breeds/{name}", tags=["Breed Name"])
def get_breed_by_name(name: str):
  return breedController.get_breed_by_name(name)


# @router.post("/recognition/disease", tags=["Disease Recognition"])
# def get_disease(image: Image):
#   return controller.get_disease(image.image_url)


# @router.post("/recognition/skin_disease", tags=["Skin Disease Recognition"])
# async def get_skin_disease(image: UploadFile):
#     return await controller.get_skin_disease(image)