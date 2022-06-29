# Auctions
#### Video Demo:  <https://youtu.be/1GPGL4Ez5Es>

#### Description:

Django application with sqlite database for listing and auctioning.

Functionalities:

- User account creation
- Listings with a title, optional photo, item description, category and starting price
- Possibility to comment on the listing
- Possibility to add and remove listings from the watch list
- End auction at any time, with the announcement of the winner

## How to run locally

### Download or clone repository

#### Archive download

[Download](https://github.com/Ziemii/Auctions/archive/refs/heads/main.zip) main branch ZIP file 

#### Git

```
git clone -b main https://github.com/Ziemii/Auctions.git
```

I also recommend using the python virtual environment.

### Create an environment

macOS/linux:
```
$ cd Auctions
$ python3 -m venv venv
```
Windows:
```
> cd Auctions
> py -3 -m venv venv
```

### Activate environment
macOS/linux:
```
$ . venv/bin/activate
```
Windows:
```
> venv\Scripts\activate
```
Your shell prompt will change to show the name of the activated environment.

### Install all dependencies in venv
In root folder:
```
$ pip install -r requirements.txt
```

### Run Django App
In root folder with file manage.py:
```
python manage.py runserver
```

# Project File Tree

* [auctions/](auctions) *Auctions Django application*
  * [static/](/auctions/static) *Static styles files*
    * [auctions/](/auctions/static/auctions)
      * [styles.css](/auctions/static/auctions/styles.css)
  * [templates/](/auctions/templates) *HTML templates*
    * [auctions/](/auctions/templates/auctions)
      * [categories.html](/auctions/templates/auctions/categories.html)
      * [category.html](/auctions/templates/auctions/category.html)
      * [create.html](/auctions/templates/auctions/create.html)
      * [error.html](/auctions/templates/auctions/error.html)
      * [index.html](/auctions/templates/auctions/index.html)
      * [layout.html](/auctions/templates/auctions/layout.html)
      * [listing.html](/auctions/templates/auctions/listing.html)
      * [login.html](/auctions/templates/auctions/login.html)
      * [register.html](/auctions/templates/auctions/register.html)
      * [user.html](/auctions/templates/auctions/user.html)
      * [watchlist.html](/auctions/templates/auctions/watchlist.html)
  * [admin.py](/auctions/admin.py) *Enable database manipulation from admin panel*
  * [apps.py](/auctions/apps.py)
  * [forms.py](/auctions/forms.py) *Django forms, mainly for listing creation fields*
  * [models.py](/auctions/models.py) *Database models are defined here*
  * [tests.py](/auctions/tests.py)
  * [urls.py](/auctions/urls.py) *All app routes are defined here*
  * [views.py](/auctions/views.py) *Responsible for database communication and views renders*
  * [__init__.py](/auctions/__init__.py)
* [commerce/](/commerce) *Root django app*
  * [asgi.py](/commerce/asgi.py)
  * [settings.py](/commerce/settings.py)
  * [urls.py](/commerce/urls.py)
  * [wsgi.py](/commerce/wsgi.py)
  * [__init__.py](/commerce/__init__.py)
* [.gitignore](/.gitignore)
* [db.sqlite3](/db.sqlite3) *SQLite db for demonstration simplicity*
* [manage.py](/manage.py)
