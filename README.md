# Django Rest Framework(RestApi) Management System
## A django rest framework restaurant management system with two working apps utilizing a single database and "one as to many" relationship

## Building the project
#### Setting up all the file dependencies
```shell
#Download the full project, together with the Pipfiles then run the following commands
#Setup the virtual environment
> pipenv shell
```

#### Ensure your python is 3.8
```shell
#Run the command below to install the code
> pipenv install
```
#### Verify success project setup
```shell
#Ensure you are in the folder with the file manage.py
> python3 manage.py runserver
```


#### Visit the full installation instructions

Please visit the installation Branch to properly configure the app or to understand the code better 

https://github.com/Ndhlovu1/django-crud-api-system/tree/Ndhlovu1-installation-instructions-1

Type the code above to install and setup django as well as the virtual environment for you

```shell
pipenv shell
```
The code above will activate the virtual environment

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


### Files to be edited
#### <li>Project level urls.py , as the name implies it is found in the RestaurantProject folder within the container folder (Read the Commit comments)</li>

![Screenshot from 2022-12-30 00-55-36](https://user-images.githubusercontent.com/46927702/210018920-47381fe5-4a18-46f4-b1a5-12d8325b883c.png)


 
 ### Files to be created
 #### <li>App level urls.py , You will have to create this one as it isn't provided by default when creating an app with manage.py</li>

![Screenshot from 2022-12-30 00-51-00](https://user-images.githubusercontent.com/46927702/210018700-805d9a42-4317-44f4-b589-e87d7479ab97.png)
![Screenshot from 2022-12-30 00-50-52](https://user-images.githubusercontent.com/46927702/210018697-336119df-cdcd-47e0-a3e4-d18f7c82db06.png)


#### <li> serializers.py , this file must be created as it is needed to utilize the API's</li>

![Screenshot from 2022-12-30 00-50-46](https://user-images.githubusercontent.com/46927702/210018751-ed8269c5-34c1-4afa-a8eb-864e712fb857.png)
![Screenshot from 2022-12-30 00-50-40](https://user-images.githubusercontent.com/46927702/210018746-bfccd773-aca7-4a1b-b71e-54de31ff0fff.png)


