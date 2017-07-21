# bucketlist
Quickly and easily arrange your dreams and goals in an achievable manner where you only have to check what you have achieved and what you have not.
The bucketlist application allows for creation, deletion and update of dreams achieved and those yet to be achieved
# Getting Started
- Clone the repository from github
- unzip your repository to your desired folder in your local machine
- Run the application using git bash commands
- Register your credentials in the application to allow for authentication
- Once authenticated, you will be redirected to the create bucketlist page where you can create your bucketlist items. 
- To view or edit a bucket list, go to view link and use the buttons to either edit or delete a bucketlist
# Prerequisites
Ensure that you have the following applications installed your local machine before running the application.
- Python 3.6
- Flask 
- Git
# Installing
To run the application: follow the following guidelines on installing the application
- Create a github account incase you dont have one
- Install python 3.6 and check on the checkbox for git environments
- Once installed, run the pip install virtualenv to allow for virtual environments
- For TDD, run pip install flask nosetests to install nosetests that will be used to check local tests
- Install heroku by downloading the .exe file
- To add an app to the git environment, run git add __init__ thehn run git add appname
- Run the git commit with some commit message to commit the changes
# Running Tests
- Write a tests file that shall be run against with some dummy data to check for correctness of the application to be built
- Run the tests against nosetest by running the nosetests testsfile command
- [[Code Climate]] https://codeclimate.com/github/betkibet/bucketlist
- [![Coverage Status](https://coveralls.io/repos/github/betkibet/bucketlist/badge.svg?branch=master)](https://coveralls.io/github/betkibet/bucketlist?branch=master)
# Deployment
- Create a heroku account
- Once the tests have been ascertained to be okay, create an origin file by running the git remote add origin github_url command
- Run a git push command to push the application to both github and heroku
# Authors
- This app was originally created by Namanga
# Acknowledgements
- Andela NBO20 Team 7
- Andela Team 7 Fascilitator Sharon
