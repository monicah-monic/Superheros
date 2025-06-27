# Superheroes API
A Flask API for tracking superheroes and their respective superpowers.

# Description
This API enables the user perform CRUD operations on the heroes and powers through endpoints, and provides relationships between them through the hero_powers entity.

# Features
View all heroes and their details
View all powers, get specific power details and update power descriptions.
Hero-Power-Creates associations between heros and powers with strength levels therefore being the join table
Data Validation-Ensures correct data is entered else throws an error

# Structure
Superheros
└── server/
    ├── app.py              
    ├── models.py           
    ├── migrations        
    └── instance/
        └── superheroes.db  
├── Pipfile                 
├── Pipfile.lock           
└── README.md               

# Setup and Installation
1. Clone the repository:
git clone repository-url
cd superheroes
2. Create and activate virtual environment:
pipenv install && pipenv shell
3. Initialize the database:
cd server
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
4. Seed the database with sample data:
python server/seed.py
5. Run the application:
python server/app.py
The API will be available at http://localhost:5555/

# API Endpoints
Heroes
-GET /heroes - Get all heroes
-GET /heroes/:id - Get a specific hero with their powers
Powers
-GET /powers - Get all powers
-GET /powers/:id - Get a specific power
-PATCH /powers/:id - Update a power's description
Hero Powers
-POST /hero_powers - Create a new hero-power relationship

# Data Models
Hero
-id: Primary key
-name: Hero's name
-super_name: Hero's superhero name
Power
-id: Primary key
-name: Power name
-description: Power description (must be at least 20 characters)
HeroPower
-id: Primary key
-strength: Power strength level ('Strong', 'Weak', or 'Average')
-hero_id: Foreign key to Hero
-power_id: Foreign key to Power

# Validations
Power description: Must be present and at least 20 characters long
HeroPower strength: Must be one of 'Strong', 'Weak', or 'Average'

# Responses
All successful responses return JSON data with appropriate HTTP Status Codes:
200: Success
201: Created
404: Not Found
400: Bad Request (validation errors)

# Owner
Monicah Wanjiru


