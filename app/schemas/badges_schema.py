from pydantic import BaseModel

class BadgeResponse(BaseModel):
    id: int
    name: str
    description: str
    score: int

    class Config:
        orm_mode = True

class BadgeCreateRequest(BaseModel):
    badge_name: str
    description: str
    score: int

    class Config:
        orm_mode = True

class PointsResponse(BaseModel):
    points: int

class LevelsResponse(BaseModel):
    level: int

    class Config:
        orm_mode = True
