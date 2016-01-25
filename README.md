# portal
This is a tool to help make community engagement easier. It is also a projec aid in learning Python and Django web developement.

## Proposed feature list (Arranged in order of priority)
* Membership
* News/Blog
* Events management
* Calendar
* Community Forum

### Technology stack
* [Django Framework](https://www.djangoproject.com/)
* [PostgreSQL](http://www.postgresql.org/)

#### Setting up
1. Make sure you have installed Python,
   [pip](https://pip.pypa.io/en/latest/) and [virtualenv](http://www.virtualenv.org/en/latest/).
1. Make sure you have PostgreSQL installed. For a tutorial on installing
   Postgres, [Django Girls'](http://djangogirls.org) ebook,
   [Tutorials Extension](http://djangogirls.org/resources/), is a reference.
   The info is also on [Django Girls GitHub repository](https://github.com/DjangoGirls/tutorial-extensions/blob/master/optional_postgresql_installation/README.md).
1. Clone the repo - `https://github.com/Python-Mombasa/portal.git` and cd into
  the `portal` directory.
1. Create a virtual environment with Python and install dependencies:
 ```bash
 $ virtualenv venv
 $ source venv/bin/activate
 $ pip install -r requirements.txt
 ```   
1. Create `portal` database, where `portal` might be any suitable name.
1. Run `export SECRET_KEY=random_string` also `export DB_PASSWORD='your_db_username'` in your terminal
1. Run `python manage.py migrate`
1. Run `python manage.py createsuperuser` to create superuser for the admin
1. Run `python manage.py runserver` to run your server
