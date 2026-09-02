# FastAPI Vehicle Inventory API

A FastAPI-based REST API for working with vehicle inventory data using MySQL and SQLAlchemy.

## Requirements

Make sure the following are installed:

* Python 3.10+
* MySQL
* pip
* Python `venv`

## Project Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd fastapi-inventory
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

After activation, the terminal should show `(venv)`.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root:

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=your_database_name
DB_USER=root
DB_PASSWORD=your_database_password
```

Do not commit the `.env` file to Git.

## Database

The application currently uses an existing MySQL database and the existing `vehicles` table.

The SQLAlchemy `Vehicle` model maps to this table.

## Run the Application

Make sure the virtual environment is activated:

```bash
source venv/bin/activate
```

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## API Version

Current API version:

```text
/api/v1
```

## Available Endpoints

### Get Vehicles

```http
GET /api/v1/vehicles/
```

Returns vehicle records from the database.

### Get Vehicle by ID

```http
GET /api/v1/vehicles/{vehicle_id}
```

Example:

```http
GET /api/v1/vehicles/1
```

Returns `404 Not Found` if the vehicle does not exist.

## Project Structure

```text
fastapi-inventory/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── router.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   └── vehicle.py
│   ├── routers/
│   │   └── vehicles.py
│   ├── schemas/
│   │   └── vehicle.py
│   ├── repositories/
│   └── services/
├── tests/
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Generate `requirements.txt`

If dependencies are added or updated, regenerate the requirements file:

```bash
pip freeze > requirements.txt
```

## Current Tech Stack

* Python 3.10
* FastAPI
* Uvicorn
* SQLAlchemy
* PyMySQL
* Pydantic
* Pydantic Settings
* MySQL
