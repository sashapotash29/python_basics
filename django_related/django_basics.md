# Django Information

##### Link: ***https://docs.djangoproject.com/en/1.11/***


### Taking a Step Back

#### Why should you use Django?

- A lot of features are already built in.
	- Middleware for sessions (storing client information as they are interacting with your site).
	- ORM for working with the database and saving information.
	- Apps are easily transferred to other Web Applications built in Django.
	- Circular Imports are difficult to work around and Django's framework avoids this in a relatively easy way.
	- Free!

### Installing Django

```
pip3 install django
```
- The command will install Django.


### Starting a Project

- In the command line at the directory of your choosing, run the following command:

```
$ django-admin startproject *name_of_your_project*

```

### What is created?

- A folder will be created with the name of your project.
- Inside that folder is a another folder with the same name and a file names *manage.py* . 
- *manage.py* contains configurations and settings to explain where certain things in your app and make sure then when the app runs the imports work as expected. (Circular Imports are a nightmare!!)
- The next folder also with your chosen name will contain many files.

#### settings.py

- This is where the settings for your app are stored.
- Most notably it contains,
	- INSTALLED_APPS which is where you add apps that you have created or want to incorporate into your project.
	- MIDDLEWARE is anything that sits between the client and backend. (Most if it comes from Django but as always you can add your own).
	- TEMPLATES is where your HTML templates are located.
	- DATABASES is where the database is located and where it should connect.

#### urls.py

- This file is where your urlpatterns are stored. 
- urlpatterns are recorded to explain to the app what route is meant for which app.
- To add access to an app's urls, enter code as follows:

```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	
	//NEW URLS
	url(r'^*newapp/', include('newapp.urls'), name = 'newapp')

]
```
- Be sure above to write the following code to allow for include.
```
from django.conf.urls import url, include
```


### Creating a new app within your project

- run this command at the level where your *manage.py* is placed.

```
$ python manage.py startapp polls
```
- This command will create a directory with the app you have chosen but **NOTE** it is not yet connected to your main project.
- In order to connect this to your project,
you need to attach the urls in the urls.py at the ***project level!!***





