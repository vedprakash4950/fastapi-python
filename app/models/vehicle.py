from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, String

from app.core.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(BigInteger, primary_key=True, index=True)

    stock_number = Column(String(191), nullable=False)
    vin_number = Column(String(191), nullable=False)

    year = Column(Integer, nullable=False)

    mileage = Column(Integer, nullable=True)
    price = Column(Float, nullable=True)

    inventory_status = Column(String(191), nullable=True)
    current_status = Column(String(255), nullable=True)

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)