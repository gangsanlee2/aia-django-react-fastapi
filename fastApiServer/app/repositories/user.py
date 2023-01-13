from app.database import conn
from app.models.user import User
import pymysql
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()
from app.schemas.user import UserDTO

def join(userDTO: UserDTO, db: Session)->str:
    user = User(**userDTO.dict())
    db.add(user)
    db.commit()
    return "success"

def login(id: str, item: User, db: Session):
    return None

def update(id, item, db):
    return None

def delete(id, item, db):
    return None


def find_users(page:int, db: Session):
    print(f" type of Session is {Session}")
    print(f" page number is {page}")
    return db.query(User).all()

def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()

def find_user(id, db):
    return None

def find_users_by_job(search, page, db):
    return None
