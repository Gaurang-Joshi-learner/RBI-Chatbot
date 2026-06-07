from fastapi import APIRouter, Depends
print("AUTH.PY LOADED")
from sqlalchemy.orm import Session
from sqlalchemy import DateTime

from app.db.deps import get_db
import random

from datetime import (
    datetime,
    timedelta
)

from app.models.user import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# -------------------------
# SIGNUP
# -------------------------

@router.post("/signup")
def signup(
    payload: dict,
    db: Session = Depends(get_db)
):

    username = payload.get("username")
    email = payload.get("email")
    password = payload.get("password")

    if not username or not email or not password:

        return {
            "error": "All fields required"
        }

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:

        return {
            "error": "Email already exists"
        }

    hashed_password = hash_password(password)

    new_user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }
@router.post("/login")
def login(
    payload: dict,
    db: Session = Depends(get_db)
):

    email = payload.get("email")
    password = payload.get("password")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return {
            "error": "Invalid credentials"
        }
    
    if not verify_password(
        password,
        user.hashed_password
    ):
        return {
            "error": "Invalid credentials"
        }

    token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@router.post("/forgot-password")
def forgot_password(
    payload: dict,
    db: Session = Depends(get_db)
):

    email = payload.get("email")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return {
            "error": "User not found"
        }

    otp = str(
        random.randint(
            100000,
            999999
        )
    )

    user.otp = otp

    user.otp_expiry = (
        datetime.utcnow()
        + timedelta(minutes=5)
    )

    db.commit()

    print(
        f"OTP for {email}: {otp}"
    )

    return {
        "message":
        "OTP generated"
    }
@router.post("/verify-otp")
def verify_otp(
    payload: dict,
    db: Session = Depends(get_db)
):

    email = payload.get("email")
    otp = payload.get("otp")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return {
            "error": "User not found"
        }

    if user.otp != otp:
        return {
            "error": "Invalid OTP"
        }

    if (
        user.otp_expiry <
        datetime.utcnow()
    ):
        return {
            "error": "OTP expired"
        }

    return {
        "message":
        "OTP verified"
    }
@router.post("/reset-password")
def reset_password(
    payload: dict,
    db: Session = Depends(get_db)
):

    email = payload.get("email")

    new_password = payload.get(
        "new_password"
    )

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return {
            "error": "User not found"
        }

    user.hashed_password = (
        hash_password(
            new_password
        )
    )

    user.otp = None
    user.otp_expiry = None

    db.commit()

    return {
        "message":
        "Password reset successful"
    }