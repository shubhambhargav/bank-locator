# Bank Locator
This application helps in discovering the bank location details.

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

# Download data (please run it outside the repo setup)
git clone https://github.com/snarayanank2/indian_banks.git

# Upload data to postgres (please run this from the root directory of the above downloaded data)
psql -h localhost -p 5432 -U banker postgres < indian_banks.sql
```

## Deploy

### Locally (without heroku)
```
python manage.py runserver 8080
```

### Locally (with heroku)
```
# Assuming that heroku login is already done
heroku local
```

### Remote
```
# Please skip the following if already done
heroku login
heroku createapp bank-locator
heroku config:set DISABLE_COLLECTSTATIC=1

# Deploy from master
git push heroku master

# [Optional] Deploy from a custom branch
git push heroku <branch-name>:master
```