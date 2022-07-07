# Cinema reservations app

#### An application displaying the movie schedule for a specific day. Allows to reserve a place in the cinema hall.


Technologies used to create application:
[![Python Version](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0.5-brightgreen.svg)](https://djangoproject.com)
[![PostgreSQL Version](https://img.shields.io/badge/postgresql-14.0-brightgreen.svg)](https://www.postgresql.org)
[![Bootstrap Version](https://camo.githubusercontent.com/4ec342876a40b53ffc6230a41196528690f9f42b1098fd354df46c649720b4c6/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d446f636b657226636f6c6f723d323439364544266c6f676f3d446f636b6572266c6f676f436f6c6f723d464646464646266c6162656c3d)](https://www.docker.com/)

Application also uses javascript files to filter, sort movies, transfer data to server, change classes, 
parameters of html elements (reservation of indicated seats in the cinema room).
System allows a maximum of 6 sites to be selected during a single visit.  
It is not possible to book a ticket for movies earlier than the current day.  
Adding data to the database possible only in the admin panel by the administrator.  
Administrator account automatically created during first migration.  
Images (media) are stored on an external server - 'Cloudinary'.

#### Testing the application:
Aplication is available at: https://my-cinema-reservations.herokuapp.com/repertoire/

Ticket can only be booked after logging in. Test user accounts:
1. Email: test1@test1.com; Password: qwertyui123
2. Email: test2@test2.com; Password: qwertyui123

### Running project locally (without using a docker)
#### I strongly recommend using a docker because in this case you don't need to have a database (PostgreSQL) locally and it is generally much simpler. See instructions below.
Go in terminal to the place where you want to clone the repository.
First, clone the repository to your local machine (in specific directory):

```
git clone git@github.com:mefiuea/cinema_reservations.git
or
git clone https://github.com/mefiuea/cinema_reservations.git
```

Install pipenv:
```
pip install pipenv
```
Go in terminal to 'cinema_reservations' directory.  
Type in terminal:
```
pipenv shell
```
to create virtual environment.

Go to your IDE (for example PyCharm) and open project (indicate folder 'cinema_reservations').

Install the requirements:

```
pipenv install --system
```

Set all environment variables. 
Go to the env folder, then create an .env file and copy the contents of the .env-default file into it.  
Also do the same for the database.env-default file (this file is used by docker-compose).
Once this is done, fill the .env file (and database.env) with the appropriate data. 
In the terminal, load the environment variables from this file with the command:

```
source env/.env
```

Change DEBUG mode in settings.py:

```
DEBUG = True
```

Apply the migrations:

```
python manage.py migrate
```

Finally, run the development server:

```
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


### Running project locally (using a docker)
You must have docker installed on your local machine and running.
Website: https://www.docker.com/get-started/  

Remember to fill the .env files (for example in your IDE).
Go to the env folder, then create an .env file and copy the contents of the .env-default file into it.  
Also do the same for the database.env-default file (this file is used by docker-compose).
Once this is done, fill the .env file (and database.env) with the appropriate data. 
Fill example:  

.env
```
export SECRET_KEY='zBD9QgVBEHAMvbXVyfk4AQXBEe3uFVYgqFQxQQy7'

[//]: # (the same data as in the database.env file)
export POSTGRES_DATABASE_USER='my_user'
export POSTGRES_PASSWORD='vpNnh49u'
export POSTGRES_DATABASE_NAME='cinema_database'

export DJANGO_SU_EMAIL='su@su.com'
export DJANGO_SU_FIRST_NAME='su'
export DJANGO_SU_LAST_NAME='su'
export DJANGO_SU_PASSWORD='TU4xVkyn'

[//]: # (optional, you don't need to fill out if you don't have an account there. In that case, you will have to change the media storage path in the settings file (more on that later).)
export CLOUDINARY_CLOUD_NAME=''
export CLOUDINARY_API_KEY=''
export CLOUDINARY_API_SECRET=''
```
database.env  
```
POSTGRES_USER=my_user
POSTGRES_PASSWORD=vpNnh49u
POSTGRES_DB=cinema_database
```

Enter the terminal. Navigate to the folder where you downloaded the project. Go to the 'cinema_reservation' folder. Type:
```
docker-compose up
```

Enter to container. Type:
```
docker ps  [//]: # (to list all available containers)
docker exec -it <container id> bash  [//]: # ('cinema_reservations_container')
```

When you are inside container type:
```
python manage.py migrate
```

Then type:
```
python manage.py runserver
```

The project will be available at **0.0.0.0:8000**.


**  
Additionally, you can:
1. Turn on debug mode in settings.py: DEBUG = True,
2. If you don't have a cloudinary account, check the settings.py file and find: 
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage' and comment it out.
3. 