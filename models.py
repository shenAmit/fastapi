# models.py

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "tka_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nav_code = Column(String(20), nullable=True)
    send_email = Column(TINYINT(1), default=0)
    active = Column(TINYINT(3, unsigned=True), default=0)
    view_encrypt = Column(TINYINT(3, unsigned=True), nullable=False, default=1)
    name = Column(String(255), nullable=True)
    email = Column(String(191), nullable=False, index=True)
    password = Column(String(191), nullable=False)
    remember_token = Column(String(100), nullable=True)
    category_id = Column(INTEGER(unsigned=True), nullable=True, index=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    last_login_at = Column(TIMESTAMP, nullable=True)
    branch_id = Column(INTEGER(unsigned=True), nullable=False, default=0)
    department_id = Column(INTEGER(unsigned=True), nullable=True)
    image = Column(Text, nullable=True)
    teachlist = Column(TINYINT(1), default=0)
    api_token = Column(String(80), nullable=True)
    availability_sent = Column(TINYINT(1), nullable=False, default=0)
    faker = Column(TINYINT(1), nullable=True)
