from pydantic import BaseModel, Field

class AddressCreate(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    address:str = Field(min_length=3, max_length=255)

class AddressResponse(AddressCreate):
    id: int

    class Config:
        from_attributes = True

class AddressWrapperResponse(BaseModel):
    status: str
    status_code: int
    data: AddressResponse
