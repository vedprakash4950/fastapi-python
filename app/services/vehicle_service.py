import math
import logging
from fastapi import HTTPException, UploadFile, Request, status
from sqlalchemy.orm import Session
from app.services.file_service import FileService
from app.repositories.vehicle_repository import VehicleRepository
from app.schemas.vehicle import VehicleCreate
from sqlalchemy.exc import SQLAlchemyError
from app.utils.url_helper import build_file_url
logger = logging.getLogger(__name__)


class VehicleService:

    @staticmethod
    def create(
        db: Session,
        data: VehicleCreate,
        main_image: UploadFile | None = None,
    ):
        image_path = None

        try:
            if main_image:
                image_path = FileService.save_vehicle_image(main_image)

            vehicle = VehicleRepository.create(
                db=db,
                data=data,
                main_image=image_path,
            )

            db.commit()
            db.refresh(vehicle)
            vehicle.main_image = build_file_url(
                request,
                vehicle.main_image,
            )


            return vehicle

        except SQLAlchemyError:
            db.rollback()

            logger.exception("Failed to create vehicle")

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create vehicle",
            )
        
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
        vehicles, total = VehicleRepository.get_all(
            db=db,
            page=page,
            limit=limit,
            search=search,
            year=year,
            inventory_status=inventory_status,
            sort_by=sort_by,
            sort_order=sort_order,
        )

        last_page = math.ceil(total / limit) if total else 1

        if total == 0:
            from_record = None
            to_record = None
        else:
            from_record = ((page - 1) * limit) + 1
            to_record = min(page * limit, total)

        return {
            "current_page": page,
            "per_page": limit,
            "total": total,
            "last_page": last_page,
            "from": from_record,
            "to": to_record,
            "data": vehicles,
        }

    @staticmethod
    def get_by_id(db: Session, vehicle_id: int):
        vehicle = VehicleRepository.get_by_id(db, vehicle_id)

        if vehicle is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vehicle not found",
            )

        return vehicle