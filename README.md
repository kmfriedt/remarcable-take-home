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
## This is not an exhaustive list just a list of all the things I thought of while building this.
### Build
Application Server Builds
- I would deploy Django using a production-grade application server such as Gunicorn. 
- If any async workflows were created then I would Uvicorn workers
- I would containerize the application using Docker. This would provide a consistent runtime environment between development, CI, staging, and production.

The container would:
- Install the application's Python dependencies.
- Run Django using Gunicorn/Uvicorn rather than runserver.
- Receive configuration through environment variables, environment variables would be stored in a parameter store.

I would place the application behind a load balancer or reverse proxy.

This would provide:

- TLS/HTTPS termination.
- Health checks.
- Load balancing across multiple application instances.
- Protection from directly exposing application servers.

I would also create separate development, staging, and production environments.

### Database
I would move to a PostgreSQL Database
Production database work would include:
- Managed PostgreSQL instance.
- Automated backups.
- Point-in-time recovery.
- Database monitoring.
- Migration management.

I would likely use Postgres GIN to perform the description searches and EasticSearch if the scale required it.

### Security
- Add rules for robots
- CSRF protection
- OAuth 2.0
- Define Application level permissions
- Parameter Store for
  - API Tokens
  - Django Secret Key
  - Credentials
  - etc.

### Code Quality
- I would install MyPy as a type checker
- Setup linting rules

### Monitoring
- Add logging and setup Datadog dashboards
- Add error tracking with Sentry
- Setup metrics to track
  - Request rate.
  - Error rate.
  - Response latency.
  - Database query latency.
  - CPU and memory utilization.
  - Database connections.
  - Application instance health.

### Testing
I would expand current tests to include the Category and Tag models.

### CI/CD
I would add a CI/CD pipeline to every pull request
- Install dependencies.
- Run linting.
- Run MyPy.
- Run Django system checks.
- Run migrations against a test database.
- Run the test suite.
- Build the Docker image, AMI, etc.

