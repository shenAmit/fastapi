
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.user_controller import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)
from database import get_db

router = APIRouter()

@router.get("/users")
def read_users(item: int = None,page: int = 1,db: Session = Depends(get_db)):
    users = get_all_users(db,item,page)
    return {'status':True,"msg":"Data get successfully","data":users}

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/")
def add_user(user: dict, db: Session = Depends(get_db)):
    new_user = create_user(db, user)
    return new_user

@router.put("/users/{user_id}")
def modify_user(user_id: int, user: dict, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
