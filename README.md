# Address-Book-API
This repo is the backend for an Address Book manipulation and retrival his app incude logic for adding addresses retrive address based on longitude latitude and distance parameters this app also incude logic for soft deleting an address

# Tech Stack
**Python==3.13**
**fastapi==0.128.0**
**uvicorn==0.40.0**
**SQLAlchemy==2.0.46**
**pydantic==2.12.5**
**geopy==2.4.1**

# Api's
## Create Address
## Delete Address
## Fetch Address based on distance , latitude and longitude

# Installation
1. Use `git clone https://github.com/gokulganesh189/Address-Book-API.git` to clone the repo.
2. `cd Address-Book-API`
3. `python -m venv env`
4.  ## Windows:
    `env\Scripts\activate`
    ## Linux/Mac:
    `source env/bin/activate`
5. `pip install --upgrade pip`
6. `pip install -r requirements.txt`
7. run the app `uvicorn app.main:app --reload`

# Local Host URL

App will be available at: `http://127.0.0.1:8000`
Swagger UI: `http://127.0.0.1:8000/docs`

# Api endpoint

## Health check 
method = GET
URL = `http://127.0.0.1:8000/`
response = {
  "status": "Address Book Api is working fine"
}

## Add address
method = POST
URL = `http://127.0.0.1:8000/addresses/add-address`
payload = {
  "latitude": "latitude", 
  "longitude":"longitude",
  "address": "address"
}
response = {
  "status": "string",
  "status_code": 0,
  "data": {
    "latitude": -90,
    "longitude": -180,
    "address": "string",
    "id": 0
  }
}

## Get Nearby addresses
method = POST
URL = `http://127.0.0.1:8000/addresses/nearby-address?lat=9.250007617943718&lon=76.5648040441125&distance_km=3`
response = {
  "status": "Success",
  "data": [
    {
      "address": "address",
      "status": true,
      "id": 2,
      "latitude": 'latitude',
      "longitude": 'longitude'
    }
  ],
  "status_code": 200
}

## Delete Address
method = DELETE
URL = `http://127.0.0.1:8000/addresses/delete/{address-id}?address_id=1`
response = {
  "status": "Success",
  "data": [],
  "status_code": 200,
  "message": "Deleted successfully"
}