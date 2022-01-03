#Simple interface build using Flask

Flask is a micro web framework written in python. It is most probably backend part of the website. To know more about flask :
https://flask.palletsprojects.com/en/2.0.x/

The above program is the simple interface of the game where user is registered and registered user is displayed. Before running the flask app you need to install following dependencies:
```
pip install flask
pip install yaml
pip install flask_mysqldb
```
The next task is to go to file db.yaml and fill in the configuration information i.e.
```
mysql_host: 'localhost'
mysql_user: 'root'
mysql_password: 'abcxs'
mysql_db: 'flaskapp'
```
After updating everything run following command:
```python app.py```

##Structure of app.py
We create a route for each path and then define what happens in specified path using functions.
So, first function is used to connect to database 
```return redirect('/users', 'success')```
instructs that after successful execution, it should go to the following route '/users' and then we follow the function defined in that route to understand what happens afterwards

it fetches the data and displays the data as instructed.

