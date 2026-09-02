from fastapi import APIRouter, Depends, File, Form, Query, UploadFile, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.vehicle import (
    VehicleCreate,
    VehiclePaginationResponse,
    VehicleResponse,
)
from app.services.vehicle_service import VehicleService

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"],
)

@router.post(
    "/",
    response_model=VehicleResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_vehicle(
    stock_number: str = Form(...),
    vin_number: str = Form(...),
    year: int = Form(...),
    mileage: int | None = Form(None),
    price: float | None = Form(None),
    inventory_status: str | None = Form(None),
    current_status: str | None = Form(None),
    main_image: UploadFile | None = File(None),
    db: Session = Depends(get_db),
):
    data = VehicleCreate(
        stock_number=stock_number,
        vin_number=vin_number,
        year=year,
        mileage=mileage,
        price=price,
        inventory_status=inventory_status,
        current_status=current_status,
    )

    return VehicleService.create(
        db=db,
        data=data,
        main_image=main_image,
    )

@router.get("/", response_model=VehiclePaginationResponse)
def get_vehicles(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),

    search: str | None = None,
    year: int | None = None,
    inventory_status: str | None = None,

    sort_by: str = Query(default="id"),
    sort_order: str = Query(default="desc"),

    db: Session = Depends(get_db),
):
    return VehicleService.get_all(
        db=db,
        page=page,
        limit=limit,
        search=search,
        year=year,
        inventory_status=inventory_status,
        sort_by=sort_by,
        sort_order=sort_order,
    )

@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db),
):
    return VehicleService.get_by_id(db, vehicle_id)