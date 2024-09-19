# controllers/user_controller.py

from sqlalchemy.orm import Session
from models import User

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: dict):
    new_user = User(
        nav_code=user.get('nav_code'),
        send_email=user.get('send_email', 0),
        active=user.get('active', 0),
        view_encrypt=user.get('view_encrypt', 1),
        name=user.get('name'),
        email=user.get('email'),
        password=user.get('password'),  # You should hash this password in a real application
        category_id=user.get('category_id'),
        branch_id=user.get('branch_id', 0),
        department_id=user.get('department_id'),
        image=user.get('image'),
        teachlist=user.get('teachlist', 0),
        api_token=user.get('api_token'),
        availability_sent=user.get('availability_sent', 0),
        faker=user.get('faker')
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user_id: int, user_data: dict):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in user_data.items():
            setattr(user, key, value)
        db.commit()
        return user
    return None

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
