from sqlalchemy import or_
from sqlalchemy.orm import Session
from datetime import datetime
from app.models import vehicle
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate



class VehicleRepository:

    @staticmethod
    def create(
        db: Session,
        data: VehicleCreate,
        main_image: str | None = None,
    ):
        vehicle = Vehicle(
            stock_number=data.stock_number,
            vin_number=data.vin_number,
            year=data.year,
            mileage=data.mileage,
            price=data.price,
            inventory_status=data.inventory_status,
            current_status=data.current_status,
            main_image=main_image,
            created_date=datetime.now(),
        )

        db.add(vehicle)
        db.flush()

        return vehicle
    
    @staticmethod
    def get_all(
        db: Session,
        page: int,
        limit: int,
        search: str | None,
        year: int | None,
        inventory_status: str | None,
        sort_by: str,
        sort_order: str,
    ):
        query = db.query(Vehicle)

        # Search
        if search:
            query = query.filter(
                or_(
                    Vehicle.stock_number.ilike(f"%{search}%"),
                    Vehicle.vin_number.ilike(f"%{search}%"),
                )
            )

        # Filters
        if year is not None:
            query = query.filter(Vehicle.year == year)

        if inventory_status is not None:
            query = query.filter(
                Vehicle.inventory_status == inventory_status
            )

        total = query.count()

        # Sorting whitelist
        allowed_sort_fields = {
            "id": Vehicle.id,
            "year": Vehicle.year,
            "price": Vehicle.price,
            "mileage": Vehicle.mileage,
            "created_at": Vehicle.created_at,
        }

        sort_column = allowed_sort_fields.get(
            sort_by,
            Vehicle.id
        )

        if sort_order.lower() == "asc":
            query = query.order_by(sort_column.asc())
        else:
            query = query.order_by(sort_column.desc())

        offset = (page - 1) * limit

        vehicles = (
            query
            .offset(offset)
            .limit(limit)
            .all()
        )

        return vehicles, total

    @staticmethod
    def get_by_id(db: Session, vehicle_id: int):
        return (
            db.query(Vehicle)
            .filter(Vehicle.id == vehicle_id)
            .first()
        )