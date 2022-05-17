from sqlalchemy.orm import Session
from models import Friend

def create_friend(db: Session, first_name, last_name, age):
    new_friend = Friend(first_name=first_name, last_name=last_name, age=age)
    db.add(new_friend)
    db.commit()
    db.refresh(new_friend)
    return new_friend

def get_friend(db:Session, id:int):
    db_friend = db.query(Friend).filter(Friend.id == id).first()
    return db_friend

def list_friends(db:Session):
    all_friends = db.query(Friend).all()
    return all_friends

def update_friends(db:Session, id:int, first_name: str, last_name: str, age:int):
    db_friend = get_friend(db=db, id=id)
    db_friend.first_name = first_name
    db_friend.last_name = last_name
    db_friend.age = age

    db.commit()
    db.refresh(db_friend)
    return db_friend

def delete_friend(db:Session, id:int):
    db_friend = get_friend(db=db, id=id)
    db.delete(db_friend)
    db.commit()

