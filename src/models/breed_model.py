
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId


class BreedModel(BaseModel):
  _id: ObjectId
  id: int
  breedName: str
  breedType: str
  breedDescription: str
  furColor: str
  origin: Optional[str] = None
  minHeightInches: float
  maxHeightInches: float
  minWeightPounds: float
  maxWeightPounds: float
  minLifeSpan: int
  maxLifeSpan: int
  imgThumb: Optional[str] = None
  imgSourceURL: Optional[str] = None
  imgAttribution: Optional[str] = None
  imgCreativeCommons: bool = False

  class Config:
    orm_mode = True
    allow_population_by_field_name = True
    json_encoders = { ObjectId: str }