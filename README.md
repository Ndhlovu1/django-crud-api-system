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

```shell
python3 manage.py runserver
```
#### The above shell command can be expected to add the load the below image, if yes then the entire setup was a success! Congrats!!!

![django_successful_install](https://user-images.githubusercontent.com/46927702/210017141-7324a12d-3cd8-455a-9df2-48e6eda83f01.png)


### Files to be created
#### <li>Project level urls.py , as the name implies it is found in the RestaurantProject folder within the container folder (Read the Commit comments)</li>

![Screenshot from 2022-12-30 00-32-03](https://user-images.githubusercontent.com/46927702/210017428-511292f8-53e2-4aa1-902e-2aa36d8263f3.png)

 
 #### <li>App level urls.py , You will have to create this one as it isn't provided by default when creating an app with manage.py</li>
 
 ![Screenshot from 2022-12-30 00-38-45](https://user-images.githubusercontent.com/46927702/210017870-aefa1706-e7a9-436e-a480-098d5feffb71.png)
![Screenshot from 2022-12-30 00-38-54](https://user-images.githubusercontent.com/46927702/210017896-d03bb2a8-5648-49b8-8c9e-f72e935b061c.png)













