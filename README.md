# FoodSite

## Table of contents
* [General info](#general-info)
* [Setup](#setup)

## General info
This project is online Reataurant Ordering Site built with Django.
It comes along with user-friendly admin interface .


## Key Features
* google login authentication system.
* providing feedback to indivisual orders.
* Sending Discount Mail to Authenticated Users from Admin Site.
* And Many More




## Setup
To install all the dependencies run: 

```
$ pip install -r requirements.txt
```
### Note:
* Specify Username And Password for Admin Mail in setings.py .
* Specify Google Oath client id Credentials in settings.py
## Run :
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## To start the server:
```
$ python manage.py runserver
```
### Now , you can start deploying at your local host.

