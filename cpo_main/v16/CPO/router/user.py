from fastapi import APIRouter, status, Depends
from v16.CPO import schemas, oauth2, hashing
from database.database import get_db
from database import models
from sqlalchemy.orm import Session



router = APIRouter(tags=["User"])



@router.post('/user', status_code=status.HTTP_201_CREATED)
async def user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(username=request.username, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.User)
async def get_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id ==
         id).delete(synchronize_session=False)
    db.commit()
    return {'status': 'User deleted'}