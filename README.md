# Django Rest Framework(RestApi) Management System
## A django rest framework restaurant management system
### Built on an Ubuntu machine >= 18.04 - Commands will still run on windows(please read the wiki)

#### Visit the full installation instructions

Please visit the project wiki to properly configure the application or and to better understand the code

https://github.com/Ndhlovu1/django-crud-api-system/wiki

## Project Setup
#### Installing and activating Environments
##### This project will be using pipenv to handle all our files and dependencies
If you don't have pipenv installed follow the steps below to install and configure it, ensure you also have pip installed

```shell
> # If you don't have pip installed run the below command
> sudo apt install python3-pip
> pip3 --version

```
You should receive the version if everything went well

```shell
> pip3 install pipenv
> pipenv --version

```

follow the link to read more
https://pipenv.pypa.io/en/latest/

#### Install django and the Virtual Environment
```shell
# Run the command below to install the code needed for django
> pipenv install django
```

```shell
# To activate the virtual environment
> pipenv shell
# To deactivate the virtual environment
> deactivate
```

##### You should receive now be in a virtual environment with the name of the containing folder you are in (Screenshort below)
![Screenshot from 2023-01-07 01-24-52](https://user-images.githubusercontent.com/46927702/211116197-f62f1ead-30a9-419f-b448-81d285660eee.png)


## SIDE NOTE :
##### When you have more than one django projects setup and running with pipenv in visual studio code(vscode)


```shell 
django-admin startproject RestaurantProject
```
The code above will setup all the necessary files that you need to be able to run create the various applications. (Consider this the Heartbeat of your project, always make sure you know what's happening and where it is happening in these files.)

Navigate into the newly created "RestaurantProject" folder and run the above```startapp```  command.
The command allows you to setup your very own django application(You can view this as a section of the entire web application, i.e. the Comments Section)

```python3
python3 manage.py startapp usersApp
```
While in the same folder, run the above command to create your second app.
```python3
python3 manage.py startApp workersApp
```
The command ```install```  allows python and django to interpret the rest of your project as a Django Rest Framework

```shell
pipenv install djangorestframework
```
The ```settings.py``` file without the implemented changes

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
Start the server and see if it is running by typing the command below

Verify success project setup
```shell
#Ensure you are in the folder with the file manage.py
> python3 manage.py runserver
```
Type the code above to install and setup django as well as the virtual environment for you
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


## Projects Screenshots

### Images of the Project

#### The Listed Menu - affected directly by our Api-End points, the web-page updates on a page refresh
![Screenshot from 2022-12-29 21-46-26](https://user-images.githubusercontent.com/46927702/210011079-bc504e08-03a4-4e9a-8fe3-282233fa0194.png)


#### The Create['POST'] and fetch['GET'] Api(s) - Adding information to the database and pulling the information
![Screenshot from 2022-12-29 21-42-11](https://user-images.githubusercontent.com/46927702/210011332-a9d66d35-ca23-432c-b4cb-c8611504af44.png)


#### The Replace ['PUT'] and the Edit ['Patch'] are added into one button as we are utilizing the generics.RetrieveUpdateDestroyAPIView method
![Screenshot from 2022-12-29 21-42-38](https://user-images.githubusercontent.com/46927702/210011593-94afc907-2f8e-4a3a-b67f-99b487e018bc.png)


#### The full fetch ['GET'] API sharing the data available in our model or database table
![Screenshot from 2022-12-29 21-44-17](https://user-images.githubusercontent.com/46927702/210011673-0f24a1f8-aad6-44cd-9a04-f6c1a254b6ed.png)


#### The ['POST'] method available and ready to insert more information into the database
![Screenshot from 2022-12-29 21-44-21](https://user-images.githubusercontent.com/46927702/210011984-0266ab74-840e-48e4-ae96-47335941c8da.png)

#### The database recording all the installed records in real-time
![Screenshot from 2022-12-29 23-04-25](https://user-images.githubusercontent.com/46927702/210012043-948f925f-71e2-485d-978a-6ce8f9281177.png)


