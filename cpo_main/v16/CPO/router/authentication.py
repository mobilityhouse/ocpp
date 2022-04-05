from hashlib import new
from fastapi import APIRouter, Depends, status, HTTPException
from v16.CPO import token
from database.database import get_db
from database import models
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from v16.CPO.hashing import Hash


router = APIRouter(tags=["Authentication"])

@router.post('/auth')
async def auth(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials")

    access_token = token.create_access_token(
        data={"sub": user.username}
    )
    new_token = models.Token(username = user.username, password = user.password, token = access_token)
    db.add(new_token)
    db.commit()
    db.refresh(new_token)
    return {"access_token": access_token, "token_type": "bearer"}