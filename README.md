# remarcable-take-home
Take home assignment for Remarcable by Kyle Friedt

## Requirements
- Python3.14
- pip
- django
- bable
- django money
- moneyed


## Setup Environment
Migrate to directory
```
  cd remarcable-take-home
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
.venv\Scripts\activate
```
Install dependencies
```
pip install -r requirements.txt
```

### Setup the App
Run migrations
```
python manage.py migrate
```

### Seed Database
Run the following to set up a superuser
```
  python manage.py createsuperuser
  username: remarcable
  email: kfriedt@gmail.com
  password: remarcable
```  



## Run

