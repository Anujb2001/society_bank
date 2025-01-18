# Flask Application with MySQL

This project is a Flask-based RESTful API application following the MVC (Model-View-Controller) design pattern. It uses SQLAlchemy for database interactions and connects to a MySQL database.

## Features
- REST API endpoints for managing two tables:
  - `MasterMemberTransaction`
  - `DetailMemberTransaction`
- Follows the MVC architecture to separate concerns.
- Easily extendable and maintainable structure.

## Prerequisites
- Python 3.8+
- Docker and Docker Compose

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Up the Environment
Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Database Configuration
Update the MySQL database credentials in `app.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<host>:<port>/<database>'
```

### 4. Run the Application
Start the Flask application:
```bash
python app.py
```

The application will run on `http://localhost:5000`.

## Docker Setup

### 1. Build and Run Docker Containers
Use Docker Compose to set up the application and database:
```bash
docker-compose up --build
```

### 2. Access the Application
The Flask app will be available at `http://localhost:5000`.

## Project Structure
```
├── app.py               # Application entry point
├── models.py            # Database models
├── routes.py            # API routes and controllers
├── requirements.txt     # Python dependencies
├── Dockerfile           # Dockerfile for Flask app
├── docker-compose.yml   # Docker Compose configuration
├── README.md            # Project documentation
```

## Endpoints

### Master Member Transaction
- **POST** `/api/master-member-transaction`
  - Add a new record to the `MasterMemberTransaction` table.
  
### Detail Member Transaction
- **POST** `/api/detail-member-transaction`
  - Add a new record to the `DetailMemberTransaction` table.

## License
This project is licensed under the MIT License.

