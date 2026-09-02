from datetime import datetime

from pydantic import BaseModel, ConfigDict


class VehicleResponse(BaseModel):
    id: int
    stock_number: str
    vin_number: str
    year: int
    mileage: int | None = None
    price: float | None = None
    inventory_status: str | None = None
    current_status: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)