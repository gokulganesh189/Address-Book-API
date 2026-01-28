import logging

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from geopy.distance import geodesic

from ..database import SessionLocal
from .. import crud, models, schemas

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/addresses", tags=["Addresses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add-address", response_model=schemas.AddressWrapperResponse)
def create(address:schemas.AddressCreate,response:Response, db:Session=Depends(get_db)):
    """
    Docstring for create
    
    :param address: Description
    :type address: schemas.AddressCreate
    :param response: Description
    :type response: Response
    :param db: Description
    :type db: Session
    """
    logger.info("Creating address | lat=%s lon=%s", address.latitude, address.longitude)
    try:
        result = crud.create_address(db, address)
        logger.info("Address created successfully | id=%s", result.id)
        response.status_code = 201
        return {"status":"Success", "data":result, "status_code":response.status_code}
    except Exception as e:
        logger.exception("Failed to create address")
        response.status_code=500
        return {"status":"Failed", "message":"Failed to create address", "error":str(e), "status_code":response.status_code}

@router.get("/nearby-address")
def nearby(lat:float, lon:float, distance_km:float,response:Response, db:Session=Depends(get_db)):
    """
    Docstring for nearby
    
    :param lat: Description
    :type lat: float
    :param lon: Description
    :type lon: float
    :param distance_km: Description
    :type distance_km: float
    :param response: Description
    :type response: Response
    :param db: Description
    :type db: Session
    """
    logger.info("Fetching nearby addresses | lat=%s lon=%s distance_km=%s",lat,lon,distance_km)
    try:
        results = []
        for addr in db.query(models.Address).filter(models.Address.status == True).all():
            dist = geodesic((lat, lon), (addr.latitude, addr.longitude)).km
            if dist <= distance_km:
                results.append(addr)
        response.status_code = 200
        logger.info("Nearby search completed | results_count=%s", len(results))
        return {"status":"Success", "data":results, "status_code":response.status_code}
    except Exception as e:
        response.status_code = 500
        logger.exception("Failed during nearby address search")
        return {"status":"Failed", 
                "message":"Failed to fetch nearby addresses",
                "error":str(e), 
                "status_code":response.status_code}
    
@router.delete("/delete/{address-id}")
def delete(address_id:int,response:Response, db:Session=Depends(get_db)):
    """
    Docstring for delete
    
    :param address_id: Description
    :type address_id: int
    :param response: Description
    :type response: Response
    :param db: Description
    :type db: Session
    """
    try:
        address = crud.delete_address(db, address_id)
        if not address:
            response.status_code = status_code=404
            return {"status":"Failed", "data":[], "status_code":response.status_code, "message":"Address not found",}
        response.status_code = 200
        return {"status":"Success", "data":[], "status_code":response.status_code, "message":"Deleted successfully"}
    except Exception as e:
        response.status_code = 500
        logger.exception(f"Failed during deleting address {e}")
        return {"status":"Failed", "message":"Failed to delete address", "error":str(e), "status_code":response.status_code}

