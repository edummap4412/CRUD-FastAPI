# CRUD-FastAPI



## POST a Book

- **Endpoint:** `POST /create`
- **Description:** Creates a new book.
- **Request Body:**
  - `title` (string): Title of the book
  - `description` (string): Description of the book
- **Example Request:**
  ```http
  POST /create HTTP/1.1
  Host: example.com
  Content-Type: application/json

  {
    "title": "New Book",
    "description": "This is a new book."
  }
- **Example Resposta:**
  ```http
  HTTP/1.1 204 No Content
  Content-Type: application/json

  {
    "code": 204,
    "status": "Created",
    "message": "Book created successfully",
    "result": {}
  }
  ```
## GET all Books

- **Endpoint:** `GET`
- **Description:** Get all books.

- **Example Response:**
 ```http
    HTTP/1.1 201 Created
    Content-Type: application/json

    {
      "code": 201,
      "status": "OK",
      "message": "Success Fetch all data",
      "result": [
        {
          "id": 1,
          "title": "Book 1",
          "description": "Description of Book 1"
        },
        {
          "id": 2,
          "title": "Book 2",
          "description": "Description of Book 2"
        }
      ]
    }
  ```
## UPDATE a Book

- **Endpoint:** `UPDATE`
- **Description:** UPDATE a book.
- **Request Body:**
  - `title` (string): Title of the book
  - `description` (string): Description of the book

**Example Request:**
  ```{
  "parameter": {
    "id": 1,
    "title": "Livro Atualizado",
    "description": "Descrição atualizada do livro"
  }
}
```
- **Example Response:**
```http
{
  "code": "200",
  "status": "Updated",
  "message": "Success update data",
  "result": {
    "id": 1,
    "title": "Livro Atualizado",
    "description": "Descrição atualizada do livro"
  }
}
````

## Get a Book by ID

- **Endpoint:** `GET`
- **Description:** Get a book by ID.
- **Request Body:**
  - `id` (integer): ID of the book
  - 
**Example Request:**
  ```{
  "parameter": {
    "id": 1,
  }
}
```
- **Example Response:**
```http
  {
  "code": "201",
  "status": "OK",
  "message": "Success get data",
  "result": {
    "id": 1,
    "title": "Livro 1",
    "description": "Descrição do Livro 1"
  }
}
```

## DELETE a Book

- **Endpoint:** `DELETE`
- **Description:** Get a book by ID.
- **Request Body:**
  - `id` (integer): ID of the book
  - 
**Example Request:**
  ```{
  "parameter": {
    "id": 1,
  }
}
```
- **Example Response:**
```http
{
  "code": "200",
  "status": "OK",
  "message": "Success delete data",
  "result": null
}
```
