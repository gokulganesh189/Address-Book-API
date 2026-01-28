from sqlalchemy.orm import Session
from .models import Address
from .schemas import AddressCreate

def create_address(db:Session, address:AddressCreate):
    db_address = Address(**address.model_dump())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def delete_address(db:Session, address_id:int):
    address = db.query(Address).filter(Address.id == address_id).first()
    if not address:
        return None
    address.status = False
    db.commit()
    db.refresh(address)
    return address
