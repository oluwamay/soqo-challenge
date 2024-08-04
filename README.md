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
* Run the application
  - ```python manage.py startapp weather```


#### NOTE:
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
RESPONSE STATUS CODE: 201 Created

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




