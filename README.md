# django-template

## Requirements
Tools and packages required to successfully install this project.

For Windows 

1) Linux [Install](https://youtu.be/xzgwDbe7foQ) 

2) Python 3.8 and up [Install](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)

For MacOS
1) Python 3.8 and up [Install](https://docs.python-guide.org/starting/install3/osx/)

NOTE! Skip step 1 if you are a MacOS user.

## Set up

`apt-get install python3-venv`
<br>
`python -m venv venv`
<br>
`source venv/bin/activate`
<br>
`pip install -r core/requirements.txt`
<br>
<br>

## Start Your Applications
`cd core`
<br>
`./app APP_NAME`
<br>
This command auto-generates the following code:
- Adds the new app to the installed apps list
- A new urls.py file is created for the new app
- The urls.py is registered in the core/urls.py file
- A new testing directory is generated
- A new templates directory is generated
- A new template .html is generated that inherits from the base template 
- New css/js static files are generated and linked from to the html file 