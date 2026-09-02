from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

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
    created_date: datetime | None = None
    updated_at: datetime | None = None
    main_image: str | None = None

    model_config = ConfigDict(from_attributes=True)


class VehiclePaginationResponse(BaseModel):
    current_page: int
    per_page: int
    total: int
    last_page: int
    from_: int | None = Field(alias="from")
    to: int | None
    data: list[VehicleResponse]

    model_config = ConfigDict(populate_by_name=True)

class VehicleCreate(BaseModel):
    stock_number: str = Field(min_length=1, max_length=191)
    vin_number: str = Field(min_length=1, max_length=191)
    year: int
    mileage: int | None = Field(default=None, ge=0)
    price: float | None = Field(default=None, ge=0)
    inventory_status: str | None = None
    current_status: str | None = None