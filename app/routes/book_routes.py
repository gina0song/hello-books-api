from flask import Blueprint
from app.models.book import books
from werkzeug.exceptions import BadRequest, NotFound

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

def raise_bad_request(message="Invalid input data for book ID."):
    raise BadRequest(message)

def raise_not_found(book_id):
    message = f"Book with ID {book_id} not found."
    raise NotFound(message) 

@books_bp.get("")
def get_all_books():
    books_response = []
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return books_response




@books_bp.get("/<book_id>")
def get_one_book(book_id):
    book_id = int(book_id)

    try:
        book_id = int(book_id)
    except ValueError:
        raise_bad_request()


    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description,
            }
        
    raise_not_found(book_id)