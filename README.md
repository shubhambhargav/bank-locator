# Bank Locator
This application helps in discovering the bank details across a variety of locations and ISFC codes.

## Contribute

### Local Setup

1. Install python 3.7 or create a virtual environment for the same. Please make sure that the virtual env is activated before going through the next steps. [#ToDo: Add reference docs to install]
2. Install the requirements for the project using following command:
```
pip install requirements_dev.txt
```
3. Install and run postgres locally
```
# Pull required postgres image
docker pull postgres:12.1

# Run postgres locally
docker run --name banker-postgres -p 5432:5432 -e POSTGRES_PASSWORD=not-so-secure -d postgres
```
4. Log into postgres instance [#ToDo: Add reference to SQLWorkbench]
5. Setup postgres to keep application user and data isolated locally
```
CREATE USER banker WITH PASSWORD 'still-not-secure';

psql -h localhost -p 5432 -U banker postgres < indian_banks.sql
```

#### Run Locally
```
python manage.py runserver 8080
```
