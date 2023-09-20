from typing import Union
from fastapi import FastAPI, Body
import handler as helper
import datetime
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# Model
class Item(BaseModel):
    isActive: int
    connectedCount: int
    connectedData: Union[list , None] = None

class Each_device_data(BaseModel):
    ip: str = Field(..., example="192.168.1.1")
    mac: str = Field(..., example="00:1A:2B:3C:4D:5E")
    device: int = Field(..., example=123)

# class Connection_data(BaseModel):
#     dict[each_device_data]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Server start
@app.on_event("startup")
async def startup_event():

    helper.create_config()
    print('Server started :', datetime.datetime.now())

@app.on_event("shutdown")
async def shutdown_event():
    print('server Shutdown :', datetime.datetime.now())

@app.get("/")
async def health_check():
    return {"message": "Server is Active"}

@app.get("/status/now")
async def current_status():
    status_of_router = helper.get_data()
    json_compatible_item_data = jsonable_encoder(status_of_router)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/status/activate")
async def device_active():
    is_activated = helper.update_device_status(is_active = True)
    if(is_activated):
        return {"message": "activated successfully"}

@app.get("/status/deactivate")
async def device_deactive():
    is_deactivated = helper.update_device_status(is_active = False)
    if(is_deactivated):
        return {"message": "deactivated successfully"}

@app.post("/connection/update")
async def update_connection(connection_data : List[Each_device_data]):
    is_updated = helper.update_device_connected_data(connection_data)
    if (is_updated):
        return {"message": "Updated successfully"}
    else:
        return {"message": "failed"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=3000)
