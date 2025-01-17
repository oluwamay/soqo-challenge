# Soqo Coding Challenge

## Simple weather API
This application allows users to add and retrieve weather data for a particular city using python
and an SQL database.

#### Language : Python
#### Framework: Django REST Framework
#### Database: SQLite

### HOW TO SET UP PROJECT LOCALLY:
* Install django, django rest framework and SQLAlchemy
  - ```pip install django djangorestframework sqlalchemy```
* Run unit tests to ensure that the app is working as expected
  - ```python manage.py test```
> [!NOTE]
> Ensure you navigate to ~/soqo-challenge/sogoweather directory where the manage.py is located
* Run the application
  - ```python3 manage.py runserver 9092```

> [!NOTE]
> On project start-up an SQLite database file is created 'soqo_weather.db'

### API DOC
#### POST /weather
REQUEST
```json
  {
    "city": "Paris",
    "date": "2023-11-13",
    "temperature": 10.5,
    "description": "Chilled atmosphere"
  }
```
RESPONSE\
Status code: 201 Created\
BODY
```json
{
    "id": 2
  }
```

#### GET /weather/Paris
Response
Status 200 Ok
```json
  {
    "city": "Paris",
    "date": "2023-11-13",
    "temperature": 10.5,
    "description": "Chilled atmosphere"
  }
```
