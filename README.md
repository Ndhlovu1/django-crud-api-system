# Django Rest Framework(RestApi) Management System
## A django rest framework restaurant management system with 2 working apps utilizing a single database and one as to many ccommunication

### STEPS TO RUN THIS PROJECT SUCCESSFULLY
THE COMMANDS BELOW ARE ALL RUN IN THE SHELL/TERMINAL
```shell
python3 install pip or python3 install pip3 
```
The code above allows you to install pip/pip3 if you don't have it installed on your pc run it in the teminal

```shell
pip3 install pipenv 
```
I utilized pipenv to setup this repo, it auto creates your shell environment and manages your packages for you read more
 here -> https://pipenv.pypa.io/en/latest/

```shell
pipenv install django
```
Type the code above to install and setup django as well as the virtual environment for you

```shell 
django-admin startproject RestaurantProject
```
The code above will setup all the necessary files that you need to be able to run create the various applications. (Consider this the Heartbeat of your project, always make sure you know what's happening and where it is happening in these files.)

```python3
python3 manage.py startapp usersApp
```
Navigate into the newly created "RestaurantProject" folder and run the above command.
The command allows you to setup your very own django application(You can view this as a section of the entire web application, i.e. the Comments Section)

```python3
python3 manage.py startApp workersApp
```
While in the same folder, run the above command to create your second app.

```shell
pipenv install djangorestframework
```
The above command allows python and django to interpret the rest of your project as a Django Rest Framework
```python3
# go into the RestaurantProject/settings.py file 
# Look for :
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#then change it to add(text after space), be certain to not forget the , at the end and to remove the space

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'usersApp',
    'workersApp',
    'rest_framework',
]

```







