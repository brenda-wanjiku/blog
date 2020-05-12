## Bluebird

# Description
A flask-based application that allowd personal blogging where one can create and share one's opinions and other users can read and comment on them.

# By https://github.com/brenda-wanjiku/blog

# Setup/Installation Requirements
# Pre-requisites
* python3.8
* pip
* Virtual environment(virtualenv)
* Flask-Mail
* PostgreSQL

# Cloning and running
* Clone the application using git clone(this copies the app onto your device). In your   terminal:

$ git clone https://github.com/brenda-wanjiku/blog

$ cd blog

# Creating the virtual environment
* Use the following commands in your terminal to create virtual environment

$ python3.8 -m venv --without-pip virtual

$ source virtual/bin/env

$ curl https://bootstrap.pypa.io/get-pip.py | python

# Installing Flask and other Modules
$ python3.8 -m pip install Flask

$ python3.8 -m pip install Flask-Bootstrap

$ python3.8 -m pip install Flask-Script

$ python3.8 -m pip install Flask-Mail

# Testing the Application
* To run the tests for the class files:

$ python3.8 manage.py test

# Technologies Used
* Python 3.8
* Flask

## BDD
| Behavior- Our program should handle: | Input Example- When it receives: | Output Example- It should return: |
| :-------------: | :-------------: | :-------------: |
| Allow user to sign up | Click 'sign up'  | Created account |
| Show user blogs from other users | Open app | List blogs |
| Enable user to comment on a blog | Click 'comment' | written user comment |
| Enable delete a blog or comment | Click 'Delete Blog' or 'Delete Comment' | Deleted blog or comment |
| Enable user write a blog | Click 'new blog' | written user blog |

#Live Site
*Can be accessed here https://brenda-bluebird.herokuapp.com/

# Author's Contact
If you need any clarifications or have feedback on this project , contact the author at brendawanjiku@gmail.com

# License
This software is Licensed under MIT license Copyright (2018) https://raw.githubusercontent.com/brenda-wanjiku/blog/master/LICENSE
