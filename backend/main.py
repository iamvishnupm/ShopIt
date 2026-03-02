from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import engine, Base, get_db
from auth import hash_password, verify_password, create_access_token
from models import User
from schemas import UserCreate, UserResponse, UserLogin

# ===========================================

api = FastAPI()

Base.metadata.create_all(bind=engine)


api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===========================================


@api.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# ===========================================


@api.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    # check if email exist
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    # check if username exist
    existing_username = db.query(User).filter(User.username == user.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already registered")

    # ----------------

    new_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ===========================================


@api.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid Credential")

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=401, detail="Invalid Credential - Wrong Password"
        )

    access_token = create_access_token(
        #
        data={"sub": str(db_user.id)}
    )

    return {"access_token": access_token, "token_type": "bearer"}
