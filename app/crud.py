from sqlalchemy.orm import Session
from model import Book, RegisterClient
from schemas import BookSchema, RegisterSchema


def get_book(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: BookSchema):
    _book = Book(title=book.title, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book


def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)
    db.delete(_book)
    db.commit()


def update_book(db: Session, book_id: int, title: str, description: str):
    _book = get_book_by_id(db=db, book_id=book_id)
    _book.title = title
    _book.description = description
    db.commit()
    db.refresh(_book)
    return _book


def register_client(db: Session, register: RegisterSchema):
    _register_client = RegisterClient(name=register.name, email=register.email, tax_id=register.tax_id)
    db.add(_register_client)
    db.commit()
    db.refresh(_register_client)
    return _register_client

