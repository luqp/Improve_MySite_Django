# Improve MySite
This project show a menu set, in which you can see them all in a list,
and you can search each menu to see the details and their elements.

The objective of this project is to reduce the number of queries and the queries time of load on each page.

## To use
* You need python 3.5 version
* Create a new Python virtual environment.

## Requirements
This project use some requirements located on requirements.txt file:
```
(env) ...\Improve_MySite_Django> cd .\improve_django_v3\
(env) ...\Improve_MySite_Django\improve_django_v3> pip install -r requirements.txt
```

## Run app
To run the application you need to enter the catalog folder and run the server as follows:
```
(env) ...\Improve_MySite_Django\improve_django_v3> python manage.py migrate
(env) ...\Improve_MySite_Django\improve_django_v3> python manage.py runserver
```

## To load data
The project provides test data that can be loaded with the following command:
```
(env) ...\Improve_MySite_Django\improve_django_v3> python manage.py loaddata .\fixtures\menu.json
```

To see the webpage you have to make `ctrl + click` in `http://127.0.0.1:8000/`this open a new window in your browser
```
...
Django version 1.9.9, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## Menu set

<p align="center">
  <img src="https://github.com/windyludev/Improve_MySite_Django/blob/master/images/Menu.jpg">
</p>

## Item detail

<p align="center">
  <img src="https://github.com/windyludev/Improve_MySite_Django/blob/master/images/Item_detail.jpg">
</p>
