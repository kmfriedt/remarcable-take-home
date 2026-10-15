# remarcable-take-home
Take home assignment for Remarcable by Kyle Friedt

## Requirements
- Python3.14
- pip


## Setup Environment
Migrate to directory
```
  cd remarcable-take-home
```
Install Python 3.14 Mac/Linux
```
brew install python@3.14
```
Install Python 3.14 Windows
- Navigate to https://www.python.org/downloads/windows/
- Download and install the .exe for your system
- Check python version in PowerShell
```
python --version
```

Create virtual environment
```
python3.14 -m venv .venv
```
Activate virtual environment
  - Mac/Linux
```
source .venv/bin/activate 
```
  - Windows
```
.venv\Scripts\activate.ps1
```

Upgrade pip
```
python -m pip install --upgrade pip
```

Install dependencies
```
pip install -r requirements.txt
```

## Database

This project uses SQLite, no separate database server is required.
Running `python manage.py migrate` will create the database.


## Setup the App
Run migrations
```
python manage.py migrate
```

## Seed Database
Run the following to set up a superuser
```
  python manage.py createsuperuser
```
- username: remarcable
- email: kfriedt@gmail.com
- password: remarcable123


Seed the database with example data
```
python manage.py seed_products
```

## Run
Start the server
```
python manage.py runserver
```

Navigate to admin and sign in to view Products, Categories, and Tags.
```
localhost:8000/admin
```

Navigate to the search page
```
localhost:8000/products
```

Use the search page
- Search is used to look through description and name
- Choose a Category
- Choose any number of Tags

## Testing
Run tests for the product admin page and the product search page with
```
python manage.py test apps.product.tests
```

# Changes Required to use in Production
I will fill this section out after submission