# Vibes-News App
___
## Technology:
[![My Skills](https://skillicons.dev/icons?i=docker,py,flask,css,html,bootstrap)](https://skillicons.dev)

## Describtion
### Docker image with Flask application and two separately database (PostgreSQL). Application allow to create and manage articles with full admin, editor, user panel.
---
#### Created based on Python 3, Flask 2.2.2 and PostgreSQL 12 image from Docker Hub.
### Docker compose using: 
#### port 5000 - Python app
#### port 5432 - PostgreSQL database for page content
#### port 5433 - PostgreSQL database for password reset tokens  
## Features
* [x] Resset Password through email and tokens
* [x] Contact to Admin through email
* [x] Admin Panel
    * [x] User Managment
        * [x] Create User
        * [x] Edit User
        * [x] Delete User
    * [x] Post Managment
        * [x] Create Post
        * [x] Edit Post
        * [x] Delete Post
* [x] Editor Panel
    * [x] User Managment
        * [x] Edit User
    * [X] Post Managment
        * [X] Create Post
        * [X] Edit Post
        * [X] Delete Post
* [X] User Panel
    * [X] Edit Account
    * [X] Post Managment
        * [X] Create Post
        * [X] Edit Post
        * [X] Delete Post
* [x] Post View
* [X] View Post by Category
---
## How to Lunch
### In order to lunch apllication make sure that you have free free ports 5432, 5433 and 5000 and have installed Docker Desktop
### Packages  used in Python/Flask app
1. Flask [(docs)](https://flask.palletsprojects.com/en/2.2.x/)
1. Flask_Bcrypt [(docs)](https://flask-bcrypt.readthedocs.io/en/1.0.1/)
1. Flask_Login [(docs)](https://flask-login.readthedocs.io/en/latest/)
1. Flask_Mail [(docs)](https://pythonhosted.org/Flask-Mail/)
1. Flask_SQLAlchemy [(docs)](https://flask-sqlalchemy.palletsprojects.com/en/latest/) 
1. Flask_WTF [(docs)](https://flask-wtf.readthedocs.io/en/1.0.x/)
1. itsdangerous [(docs)](https://itsdangerous.palletsprojects.com/en/2.1.x/)
1. Pillow [(docs)](https://pillow.readthedocs.io/en/stable/)
### Docker Images
1. Newest Python 3 [(docs)](https://hub.docker.com/_/python)
1. PostgreSQL 12 [(docs)](https://hub.docker.com/_/postgres)


### To run application make sure that Docker Desktop is runing, then type on conosle while being inside folder contains app

```bash
  docker-compose build --no-cache # Build image
  docker-compose up -d db_first # Run first db in background on port 5432
  docker-compose up -d db_second # Run second db in background on port 5433
  docker-compose up pythonapp # Run python app on port 5000
```
